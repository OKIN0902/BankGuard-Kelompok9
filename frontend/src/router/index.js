import { createRouter, createWebHistory } from 'vue-router'
import { auth, refreshSession } from '../services/session.js'
import LoginView from '../views/LoginView.vue'
import DashboardView from '../views/DashboardView.vue'
import SimulatorView from '../views/SimulatorView.vue'
const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', redirect: '/dashboard' },
    { path: '/login', component: LoginView },
    { path: '/dashboard', component: DashboardView, meta: { requiresAuth: true } },
    { path: '/simulator', component: SimulatorView, meta: { requiresAuth: true } },
    { path: '/:pathMatch(.*)*', redirect: '/dashboard' },
  ],
})
router.beforeEach(async (to) => {
  try { await refreshSession() } catch { /* login tetap bisa dibuka untuk mencoba ulang */ }
  if (to.meta.requiresAuth && !auth.authenticated) return '/login'
  if (to.path === '/login' && auth.authenticated) return '/dashboard'
})
export default router
