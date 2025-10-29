
import { getPokemons, getPokemonDetails } from "./api.js";

export async function renderPokemonList() {
  const pokemonList = document.getElementById("pokemonList");
  const pokemons = await getPokemons();

  pokemons.forEach(pokemon => {
    const li = document.createElement("li");
    li.className = "list-group-item list-group-item-action";
    li.textContent = pokemon.name.toUpperCase();
    li.style.cursor = "pointer";

    li.addEventListener("click", async () => {
      await renderPokemonDetails(pokemon.url);
    });

    pokemonList.appendChild(li);
  });
}

export async function renderPokemonDetails(url) {
  const pokemonDetails = document.getElementById("pokemonDetails");
  pokemonDetails.innerHTML = "<p>Carregando...</p>";

  const pokemon = await getPokemonDetails(url);
  const abilities = pokemon.abilities.map(a => a.ability.name).join(", ");
  const types = pokemon.types.map(t => t.type.name).join(", ");

  pokemonDetails.innerHTML = `
    <h4>${pokemon.name.toUpperCase()}</h4>
    <img src="${pokemon.sprites.front_default}" alt="${pokemon.name}">
    <p><strong>Altura:</strong> ${pokemon.height}</p>
    <p><strong>Peso:</strong> ${pokemon.weight}</p>
    <p><strong>Tipos:</strong> ${types}</p>
    <p><strong>Habilidades:</strong> ${abilities}</p>
  `;
}
