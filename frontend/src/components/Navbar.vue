<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { auth, signOut } from '../services/session.js'
defineEmits(['toggle'])
const router = useRouter()
const busy = ref(false), error = ref('')
async function logout() {
  busy.value = true; error.value = ''
  try { await signOut(); await router.replace('/login') }
  catch (e) { error.value = e.message }
  finally { busy.value = false }
}
</script>
<template>
  <header class="topbar">
    <div class="d-flex align-items-center gap-3"><button class="btn btn-outline-secondary mobile-menu" @click="$emit('toggle')" aria-label="Buka menu">☰</button><div><small class="eyebrow">BANKGUARD / PERBANKAN</small><div class="topbar-title">Pusat pemantauan risiko</div></div></div>
    <div class="topbar-actions"><span class="vm-chip"><span class="status-dot"></span>{{ auth.instance_name || 'VM lokal' }}</span><span class="operator"><span class="avatar">{{ (auth.username || 'P').slice(0,1).toUpperCase() }}</span><span>{{ auth.username || 'Petugas' }}</span></span><button class="btn btn-outline-secondary btn-sm" :disabled="busy" @click="logout">{{ busy ? '...' : 'Keluar' }}</button></div>
  </header>
  <div v-if="error" class="alert alert-danger mx-3 mt-2 mb-0" role="alert">{{ error }}</div>
</template>
