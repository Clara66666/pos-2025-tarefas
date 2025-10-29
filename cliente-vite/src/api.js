
const API_BASE = "https://pokeapi.co/api/v2/pokemon";

export async function getPokemons(limit = 20) {
  const response = await fetch(`${API_BASE}?limit=${limit}`);
  const data = await response.json();
  return data.results;
}

export async function getPokemonDetails(url) {
  const response = await fetch(url);
  const data = await response.json();
  return data;
}
