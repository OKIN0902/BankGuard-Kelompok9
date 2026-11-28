# Full Clone template Ubuntu dengan VirtualBox pada Windows.
# Default hanya dapat diakses dari host. Isi -BindIP dengan IP LAN host untuk demo LAN.
[CmdletBinding()]
param(
  [string]$TemplateName = "BankGuard-Template",
  [string]$BindIP = "127.0.0.1",
  [string]$VBoxManage = "$env:ProgramFiles\Oracle\VirtualBox\VBoxManage.exe"
)
$ErrorActionPreference = "Stop"
if (-not (Test-Path -LiteralPath $VBoxManage)) {
  $cmd = Get-Command VBoxManage -ErrorAction SilentlyContinue
  if (-not $cmd) { throw "VBoxManage tidak ditemukan. Instal VirtualBox." }
  $VBoxManage = $cmd.Source
}
$parsed = $null
if (-not [System.Net.IPAddress]::TryParse($BindIP, [ref]$parsed) -or
    $parsed.AddressFamily -ne [System.Net.Sockets.AddressFamily]::InterNetwork -or
    $BindIP -eq "0.0.0.0") {
  throw "Gunakan IP IPv4 tertentu (127.0.0.1 atau IP LAN/VPN laptop host)."
}
if ($BindIP -ne "127.0.0.1" -and -not (Get-NetIPAddress -AddressFamily IPv4 -IPAddress $BindIP -ErrorAction SilentlyContinue)) {
  throw "IP tersebut tidak terpasang pada laptop host."
}
function Invoke-VBox {
  param([Parameter(ValueFromRemainingArguments=$true)][string[]]$Arguments)
  $output = & $VBoxManage @Arguments 2>&1
  if ($LASTEXITCODE -ne 0) { throw "VBoxManage gagal: $($Arguments -join ' '): $output" }
  return $output
}
$templateInfo = Invoke-VBox showvminfo $TemplateName --machinereadable
if (-not ($templateInfo -match '^VMState="poweroff"$')) {
  throw "Matikan VM template sepenuhnya sebelum Full Clone."
}
$registered = Invoke-VBox list vms
foreach ($n in 1..3) {
  $name = "BankGuard-{0:D2}" -f $n
  if ($registered -match ('^"' + [regex]::Escape($name) + '" ')) {
    throw "$name sudah ada. Script tidak akan menimpa VM."
  }
  $port = 8080 + $n
  if (Get-NetTCPConnection -State Listen -LocalPort $port -ErrorAction SilentlyContinue) {
    throw "Port host $port sudah digunakan."
  }
}
foreach ($n in 1..3) {
  $name = "BankGuard-{0:D2}" -f $n
  $port = 8080 + $n
  # --mode machine, tanpa opsi link = Full Clone, MAC baru secara default.
  Invoke-VBox clonevm $TemplateName --name $name --mode machine --register | Write-Host
  # Adapter 1 NAT. Hapus aturan forwarding yang diwarisi clone jika ada.
  Invoke-VBox modifyvm $name --nic1 nat | Write-Host
  $info = Invoke-VBox showvminfo $name --machinereadable
  foreach ($line in $info) {
    if ($line -match '^Forwarding\(\d+\)="([^,]+),') {
      Invoke-VBox modifyvm $name --natpf1 delete $Matches[1] | Write-Host
    }
  }
  $rule = "bankguard,tcp,$BindIP,$port,,80"
  Invoke-VBox modifyvm $name --natpf1 $rule | Write-Host
  Write-Host "$name -> http://${BindIP}:$port (belum dinyalakan)"
}
Write-Host "Full Clone dibuat. Nyalakan satu per satu dan jalankan init-instance.sh di console masing-masing."
Write-Host "Jangan membuka router ke internet. Untuk LAN, batasi Windows Firewall ke jaringan demo."
