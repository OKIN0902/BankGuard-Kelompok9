<script setup>
import { reactive, ref } from 'vue'
import { useRouter } from 'vue-router'
import RiskBadge from '../components/RiskBadge.vue'
import { protectedApi } from '../services/session.js'
const router=useRouter()
const blank=()=>({user_id:'',amount:null,historical_average:null,destination_new:false,transfers_10min:1})
const form=reactive(blank()), busy=ref(false), error=ref(''), result=ref(null)
function example(){ Object.assign(form,{user_id:'USER-001',amount:10000000,historical_average:500000,destination_new:true,transfers_10min:1});error.value='';result.value=null }
function reset(){ Object.assign(form,blank());error.value='';result.value=null }
async function submit(){
  busy.value=true;error.value='';result.value=null
  try {
    const payload={user_id:form.user_id.trim(),amount:form.amount,historical_average:form.historical_average,destination_new:form.destination_new,transfers_10min:form.transfers_10min}
    result.value=(await protectedApi('/api/transactions',{method:'POST',body:payload})).transaction
  } catch(e){if(e.status===401)await router.replace('/login');else error.value=e.message}
  finally{busy.value=false}
}
</script>
<template>
  <div class="page-heading"><div><div class="eyebrow">02 / SIMULASI RISIKO</div><h1>Simulator transaksi</h1><p class="muted">Masukkan data fiktif. Server akan menghitung dan menyimpan skor.</p></div><RouterLink to="/dashboard" class="btn btn-outline-secondary">← Kembali ke dashboard</RouterLink></div>
  <div class="sim-grid">
    <section class="panel"><div class="panel-heading"><div><h2>Informasi transaksi</h2><p>Semua kolom wajib diisi.</p></div><button class="btn btn-outline-secondary btn-sm" type="button" @click="example" :disabled="busy">Isi contoh demo</button></div>
      <div v-if="error" class="alert alert-danger" role="alert">{{ error }}</div>
      <form @submit.prevent="submit">
        <fieldset :disabled="busy">
          <div class="mb-3"><label for="user" class="form-label">ID pengguna fiktif</label><input id="user" v-model="form.user_id" class="form-control" required maxlength="64" placeholder="USER-001"></div>
          <div class="row g-3 mb-3"><div class="col-md-6"><label for="amount" class="form-label">Nominal transfer (Rp)</label><input id="amount" v-model.number="form.amount" type="number" class="form-control" required min="1" max="1000000000000" step="1"></div><div class="col-md-6"><label for="average" class="form-label">Rata-rata historis (Rp)</label><input id="average" v-model.number="form.historical_average" type="number" class="form-control" required min="1" max="1000000000000" step="1"></div></div>
          <div class="mb-3"><label for="frequency" class="form-label">Jumlah transfer dalam 10 menit</label><input id="frequency" v-model.number="form.transfers_10min" type="number" class="form-control" required min="1" max="1000000" step="1"><small class="muted">Termasuk transaksi saat ini. Nilai diisi sebagai simulasi.</small></div>
          <div class="form-check form-switch destination-switch"><input id="destination" v-model="form.destination_new" type="checkbox" class="form-check-input" role="switch"><label class="form-check-label" for="destination">Rekening tujuan baru</label></div>
          <div class="d-flex gap-2 flex-wrap mt-4"><button class="btn btn-primary" type="submit">{{ busy?'Menganalisis…':'Analisis & simpan transaksi' }}</button><button class="btn btn-outline-secondary" type="button" @click="reset">Reset</button></div>
        </fieldset>
      </form>
    </section>
    <section class="panel"><div class="eyebrow mb-2">ATURAN PENILAIAN</div><h2>Indikator risiko</h2><p class="muted">Skor resmi dihitung di Flask.</p><div class="rule-row"><span>Rekening tujuan baru</span><b>+40</b></div><div class="rule-row"><span>Nominal &gt; 3× rata-rata</span><b>+35</b></div><div class="rule-row"><span>Transfer &gt; 3 kali / 10 menit</span><b>+25</b></div><p class="muted mt-3 small">Nilai tepat 3× atau tepat 3 kali tidak menambah skor pada indikator tersebut.</p>
      <div v-if="result" class="result-box" role="status"><div class="d-flex justify-content-between align-items-center"><span class="eyebrow">HASIL TERSIMPAN</span><RiskBadge :level="result.level"/></div><div class="result-score">{{ result.score }}<small>/100</small></div><div class="bar-track"><i :class="result.level==='TINGGI'?'high':result.level==='SEDANG'?'medium':'low'" :style="{width:result.score+'%'}"></i></div><div class="mt-3"><strong>Alasan analisis</strong><ul v-if="result.reasons.length" class="mt-2 mb-2"><li v-for="reason in result.reasons" :key="reason">{{reason}}</li></ul><p v-else>Tidak ada indikator aktif.</p><small class="muted text-break">ID: {{ result.id }}</small></div><RouterLink to="/dashboard" class="btn btn-primary mt-3 w-100">Lihat di dashboard</RouterLink></div>
      <div v-else class="result-placeholder">Hasil analisis akan muncul setelah transaksi dikirim ke server.</div>
    </section>
  </div>
</template>
