<script setup>
import { computed, onMounted, ref } from 'vue'
import { useRouter } from 'vue-router'
import RiskBadge from '../components/RiskBadge.vue'
import { protectedApi } from '../services/session.js'
const router = useRouter()
const data = ref(null), busy = ref(false), error = ref(''), filter = ref('SEMUA'), search = ref('')
const rows = computed(() => (data.value?.transactions || []).filter(x =>
  (filter.value==='SEMUA'||x.level===filter.value) &&
  x.user_id.toLowerCase().includes(search.value.trim().toLowerCase())))
const stats = computed(() => [
  { label:'Total transaksi', count:data.value?.total, type:'total', hint:'Maksimal 100 terbaru' },
  { label:'Risiko tinggi', count:data.value?.high_count, type:'high', hint:'Perlu ditinjau' },
  { label:'Risiko sedang', count:data.value?.medium_count, type:'medium', hint:'Perlu perhatian' },
  { label:'Risiko rendah', count:data.value?.low_count, type:'low', hint:'Indikator terbatas' },
])
const money = n => new Intl.NumberFormat('id-ID',{style:'currency',currency:'IDR',maximumFractionDigits:0}).format(n)
const time = s => new Intl.DateTimeFormat('id-ID',{dateStyle:'medium',timeStyle:'short',timeZone:'Asia/Jakarta'}).format(new Date(s))
const percent = n => data.value?.total ? Math.round(n/data.value.total*100) : 0
async function load() {
  busy.value=true; error.value=''
  try { data.value=await protectedApi('/api/transactions') }
  catch(e) { data.value=null; if(e.status===401) await router.replace('/login'); else error.value=e.message }
  finally { busy.value=false }
}
onMounted(load)
</script>
<template>
  <div class="page-heading"><div><div class="eyebrow">01 / RINGKASAN TRANSAKSI</div><h1>Dashboard risiko</h1><p class="muted">Pantau transaksi terbaru dan prioritas peninjauan pada VM ini.</p></div><div class="d-flex gap-2 flex-wrap"><button class="btn btn-outline-secondary" @click="load" :disabled="busy">{{ busy?'Memuat…':'↻ Muat ulang' }}</button><RouterLink class="btn btn-primary" to="/simulator">+ Simulasi baru</RouterLink></div></div>
  <div v-if="error" class="alert alert-danger" role="alert">{{ error }}</div>
  <div v-if="busy" role="status" class="small muted mb-3">Mengambil data dari server…</div>
  <div class="stats-grid"><article v-for="item in stats" :key="item.type" class="stat-card" :class="item.type"><span class="stat-label">{{ item.label }}</span><strong>{{ item.count ?? '—' }}</strong><small>{{ item.hint }}</small></article></div>
  <div class="overview-grid">
    <section class="panel"><div class="panel-heading"><div><h2>Distribusi risiko</h2><p>Proporsi berdasarkan transaksi yang ditampilkan</p></div><span class="soft-label">LOKAL</span></div>
      <div v-if="data" class="distribution"><div v-for="item in stats.slice(1)" :key="item.type" class="distribution-row"><div><span>{{ item.label }}</span><b>{{ item.count }} · {{ percent(item.count) }}%</b></div><div class="bar-track"><i :class="item.type" :style="{width:percent(item.count)+'%'}"></i></div></div></div><p v-else class="muted">Data belum tersedia.</p>
    </section>
    <section class="panel notice-panel"><div class="eyebrow">PANDUAN PENINJAUAN</div><h2>Skor bukan bukti penipuan.</h2><p>BankGuard memberi peringatan berbasis tiga aturan sederhana. Gunakan hasil untuk latihan peninjauan transaksi, bukan keputusan pemblokiran rekening.</p><div class="notice-legend"><RiskBadge level="RENDAH"/> 0–39 <RiskBadge level="SEDANG"/> 40–59 <RiskBadge level="TINGGI"/> 60–100</div></section>
  </div>
  <section class="panel transaction-panel"><div class="panel-heading"><div><h2>Riwayat transaksi</h2><p>Data terbaru dahulu · waktu WIB</p></div><span class="soft-label">{{ data?.instance_name || '—' }}</span></div>
    <div class="filters"><div><label for="search" class="form-label">Cari ID pengguna</label><input id="search" v-model="search" class="form-control" placeholder="Contoh USER-001"></div><div><label for="filter" class="form-label">Kategori risiko</label><select id="filter" v-model="filter" class="form-select"><option>SEMUA</option><option>RENDAH</option><option>SEDANG</option><option>TINGGI</option></select></div></div>
    <div class="table-responsive"><table class="table align-middle"><thead><tr><th>Pengguna / waktu</th><th>Nominal</th><th>Skor</th><th>Risiko</th><th>Alasan</th></tr></thead><tbody><tr v-for="tx in rows" :key="tx.id"><td><b>{{ tx.user_id }}</b><small class="d-block muted">{{ time(tx.created_at) }}</small></td><td class="text-nowrap">{{ money(tx.amount) }}</td><td><span class="score-number">{{ tx.score }}</span><small class="muted"> / 100</small></td><td><RiskBadge :level="tx.level"/></td><td class="reason-cell">{{ tx.reasons.join(' · ') || 'Tidak ada indikator aktif' }}</td></tr></tbody></table></div>
    <div v-if="!rows.length" class="empty-state"><strong>{{ busy?'Memuat riwayat…':!data?'Riwayat belum tersedia':data.total?'Tidak ada hasil sesuai filter':'Belum ada transaksi' }}</strong><p v-if="data && !data.total">Mulai dengan memasukkan transaksi fiktif.</p><RouterLink v-if="data && !data.total" to="/simulator" class="btn btn-primary btn-sm">Buat simulasi</RouterLink></div><small v-if="data" class="muted">Menampilkan {{ rows.length }} dari {{ data.total }} transaksi terbaru.</small>
  </section>
</template>
