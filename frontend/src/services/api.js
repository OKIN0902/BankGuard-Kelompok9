// Semua permintaan melalui alamat browser yang sama.
export async function api(path, { method = 'GET', body, csrfToken } = {}) {
  if (!path.startsWith('/api/')) throw new Error('Alamat API tidak valid')
  const headers = { Accept: 'application/json' }
  if (body !== undefined) headers['Content-Type'] = 'application/json'
  if (csrfToken) headers['X-CSRF-Token'] = csrfToken
  let response
  try {
    response = await fetch(path, { method, headers, credentials: 'same-origin',
      cache: 'no-store', ...(body === undefined ? {} : { body: JSON.stringify(body) }) })
  } catch {
    throw new Error('Tidak dapat terhubung ke server. Periksa jaringan dan layanan BankGuard.')
  }
  const data = await response.json().catch(() => null)
  if (!response.ok || data === null) {
    const error = new Error(data?.error || 'Server belum siap atau respons tidak valid.')
    error.status = response.status
    throw error
  }
  return data
}
