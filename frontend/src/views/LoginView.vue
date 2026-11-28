<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { auth, signIn } from '../services/session.js'
const router=useRouter()
const username=ref('petugas'), password=ref(''), busy=ref(false), error=ref('')
async function submit() {
  error.value=''; busy.value=true
  try { await signIn(username.value,password.value); password.value=''; await router.replace('/dashboard') }
  catch(e) { error.value=e.message; password.value='' }
  finally { busy.value=false }
}
</script>
<template>
  <main class="login-shell">
    <section class="login-story">
      <div class="brand"><span class="brand-icon">BG</span><div><strong>BankGuard<span>.</span></strong><small>RISK MONITORING</small></div></div>
      <div class="story-content"><div class="story-kicker"><span class="status-dot"></span> PROTOTYPE PERBANKAN</div><h1>Kenali risiko.<br><em>Ambil keputusan<br>lebih terinformasi.</em></h1><p>Pantau transaksi simulasi, pahami indikator risiko, dan lihat hasil analisis dalam satu dashboard.</p><div class="story-visual" aria-hidden="true"><div class="story-line"><span>01 / INDIKATOR</span><b>3 aturan risiko</b></div><div class="story-bars"><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i></div><div class="story-line"><span>02 / INFRASTRUKTUR</span><b>1 template · 3 VM</b></div></div></div>
      <small class="story-footer">KELOMPOK 3 / CLOUD COMPUTING / 2026</small>
    </section>
    <section class="login-panel">
      <div class="login-card"><div class="mobile-brand">BankGuard.</div><div class="eyebrow mb-3">AKSES PETUGAS DEMO</div><h2>Selamat datang.</h2><p class="muted mb-4">Masukkan akun petugas untuk membuka pusat pemantauan risiko.</p>
      <div v-if="error || auth.error" class="alert alert-danger" role="alert">{{ error || auth.error }}</div>
      <form @submit.prevent="submit"><div class="mb-3"><label for="username" class="form-label">Nama pengguna</label><input id="username" v-model="username" class="form-control" autocomplete="username" required maxlength="128"></div><div class="mb-4"><label for="password" class="form-label">Password</label><input id="password" v-model="password" type="password" class="form-control" autocomplete="current-password" required maxlength="1024"></div><button class="btn btn-primary w-100 py-3" :disabled="busy">{{ busy ? 'Memeriksa akses…' : 'Masuk ke dashboard →' }}</button></form>
      <div class="login-notice"><strong>Lingkungan simulasi</strong><p>Gunakan password demo yang dibuat saat instalasi. Jangan masukkan kredensial bank asli.</p></div>
      <small class="muted">VM: {{ auth.instance_name || 'belum terhubung' }}</small></div>
    </section>
  </main>
</template>
