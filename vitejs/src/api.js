const API_BASE = "https://pokeapi.co/api/v2";

export async function getPokemonList(limit = 20) {
  const res = await fetch(`${API_BASE}/pokemon?limit=${limit}`);
  if (!res.ok) throw new Error("Erro ao buscar lista de Pokémons");
  const data = await res.json();
  return data.results;
}

export async function getPokemonDetails(url) {
  const res = await fetch(url);
  if (!res.ok) throw new Error("Erro ao buscar detalhes do Pokémon");
  return await res.json();
}
