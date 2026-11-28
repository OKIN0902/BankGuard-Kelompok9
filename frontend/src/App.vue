<script setup>
import { ref } from 'vue'
import { useRoute } from 'vue-router'
import Sidebar from './components/Sidebar.vue'
import Navbar from './components/Navbar.vue'
const route = useRoute()
const menu = ref(false)
</script>
<template>
  <RouterView v-if="route.path === '/login'" />
  <div v-else class="app-shell">
    <Sidebar :open="menu" @close="menu=false" />
    <div class="workspace">
      <Navbar @toggle="menu=!menu" />
      <main class="content" id="main-content"><RouterView /></main>
      <footer class="site-footer">BankGuard · Kelompok 3 · Praktikum Cloud Computing <span>Data simulasi, bukan transaksi bank nyata.</span></footer>
    </div>
  </div>
</template>
