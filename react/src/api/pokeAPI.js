const BASE = 'https://pokeapi.co/api/v2';

export async function fetchPokemonList(limit = 20, offset = 0) {
  const res = await fetch(`${BASE}/pokemon?limit=${limit}&offset=${offset}`)
  if (!res.ok) throw new Error('Erro ao buscar lista')
  return res.json()
}

// aceita url (ex: result.url) ou name (string)
export async function fetchPokemonDetails(urlOrName) {
  const url = urlOrName.startsWith('http') ? urlOrName : `${BASE}/pokemon/${urlOrName}`
  const res = await fetch(url)
  if (!res.ok) throw new Error('Erro ao buscar detalhes')
  return res.json()
}
