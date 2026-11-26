<template>
  <main class="container py-4">
    <h1 class="h3">BankGuard</h1>
    <p class="text-muted">Kerangka frontend — belum terhubung ke backend.</p>
    <nav class="nav mb-3"><RouterLink class="nav-link" to="/login">Login</RouterLink><RouterLink class="nav-link" to="/dashboard">Dashboard</RouterLink><RouterLink class="nav-link" to="/simulator">Simulator</RouterLink></nav>
    <RouterView />
  </main>
</template>
