<script setup>
defineProps({ open: Boolean })
defineEmits(['close'])
</script>
<template>
  <button v-if="open" class="sidebar-scrim" aria-label="Tutup menu" @click="$emit('close')"></button>
  <aside class="sidebar" :class="{ 'is-open': open }">
    <div class="brand"><span class="brand-icon">BG</span><div><strong>BankGuard<span>.</span></strong><small>RISK MONITORING</small></div></div>
    <div class="sidebar-label">WORKSPACE</div>
    <nav aria-label="Navigasi utama">
      <RouterLink to="/dashboard" @click="$emit('close')"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7"><rect x="3" y="3" width="7" height="7" rx="1.5"/><rect x="14" y="3" width="7" height="7" rx="1.5"/><rect x="3" y="14" width="7" height="7" rx="1.5"/><rect x="14" y="14" width="7" height="7" rx="1.5"/></svg>Dashboard</RouterLink>
      <RouterLink to="/simulator" @click="$emit('close')"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7"><path d="M3 7h17m-4-4 4 4-4 4M21 17H4m4-4-4 4 4 4"/></svg>Simulator transaksi</RouterLink>
    </nav>
    <div class="sidebar-bottom"><div class="sidebar-label">LINGKUNGAN</div><div class="demo-note"><span class="status-dot"></span><div><strong>Mode simulasi</strong><small>Data fiktif · SQLite lokal</small></div></div><small class="side-credit">CLOUD COMPUTING / 03</small></div>
  </aside>
</template>
