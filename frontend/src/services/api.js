// Pembantu fetch JSON. TODO tim frontend: panggil dari halaman dan kelola token CSRF dalam memori.
export async function api(path, { method = 'GET', body, csrfToken } = {}) {
  if (!path.startsWith('/api/') || path.startsWith('//')) throw new Error('Alamat API tidak valid')
  const headers = { Accept: 'application/json' }
  if (body !== undefined) headers['Content-Type'] = 'application/json'
  if (csrfToken) headers['X-CSRF-Token'] = csrfToken
  const response = await fetch(path, { method, headers, credentials: 'same-origin', ...(body === undefined ? {} : { body: JSON.stringify(body) }) })
  const data = await response.json().catch(() => null)
  if (!response.ok || data === null) {
    const error = new Error(data?.error || 'Server belum siap atau respons tidak valid.')
    error.status = response.status
    throw error
  }
  return data
}
