import { getPokemonList, getPokemonDetails } from "./api.js";

const pokemonList = document.getElementById("pokemonList");
const pokemonDetails = document.getElementById("pokemonDetails");

export async function renderPokemonList() {
  try {
    const pokemons = await getPokemonList();
    pokemonList.innerHTML = "";

    pokemons.forEach((pokemon) => {
      const li = document.createElement("li");
      li.className = "list-group-item list-group-item-action";
      li.textContent = pokemon.name.toUpperCase();
      li.style.cursor = "pointer";

      li.addEventListener("click", () => renderPokemonDetails(pokemon.url));
      pokemonList.appendChild(li);
    });
  } catch (error) {
    pokemonList.innerHTML = `<li class="text-danger">Erro ao carregar Pokémons.</li>`;
  }
}

async function renderPokemonDetails(url) {
  pokemonDetails.innerHTML = "<p>Carregando...</p>";

  try {
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
  } catch (error) {
    pokemonDetails.innerHTML = `<p class="text-danger">Erro ao carregar detalhes.</p>`;
  }
}
