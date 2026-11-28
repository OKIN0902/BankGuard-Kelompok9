import { reactive } from 'vue'
import { api } from './api.js'

export const auth = reactive({ authenticated: false, username: null, csrf_token: '', instance_name: '', ready: false, error: '' })
function apply(data) {
  Object.assign(auth, data, { ready: true, error: '' })
}
export function forgetSession() {
  Object.assign(auth, { authenticated: false, username: null, csrf_token: '', ready: false })
}
export async function refreshSession() {
  try { apply(await api('/api/session')) }
  catch (e) { forgetSession(); auth.error = e.message; throw e }
}
export async function signIn(username, password) {
  await refreshSession()
  apply(await api('/api/login', { method: 'POST', body: { username, password }, csrfToken: auth.csrf_token }))
}
export async function signOut() {
  try {
    await refreshSession()
    if (auth.authenticated) apply(await api('/api/logout', { method: 'POST', body: {}, csrfToken: auth.csrf_token }))
  } catch (e) {
    if (e.status === 401) forgetSession()
    else throw e
  }
}
export async function protectedApi(path, options = {}) {
  try {
    if (options.method === 'POST') {
      await refreshSession()
      if (!auth.authenticated) { const e = new Error('Sesi berakhir. Silakan login kembali.'); e.status = 401; throw e }
    }
    return await api(path, { ...options, csrfToken: auth.csrf_token })
  } catch (e) {
    if (e.status === 401) forgetSession()
    throw e
  }
}
