const pokemonList = document.getElementById("pokemonList");
const pokemonDetails = document.getElementById("pokemonDetails");

// Buscar lista de Pokémons
fetch("https://pokeapi.co/api/v2/pokemon?limit=20")
  .then(res => res.json())
  .then(data => {
    data.results.forEach(pokemon => {
      let li = document.createElement("li");
      li.className = "list-group-item list-group-item-action";
      li.textContent = pokemon.name.toUpperCase();
      li.style.cursor = "pointer";

      // Ao clicar, carrega detalhes
      li.addEventListener("click", () => {
        loadPokemonDetails(pokemon.url);
      });

      pokemonList.appendChild(li);
    });
  });

// Função para carregar detalhes do Pokémon
function loadPokemonDetails(url) {
  pokemonDetails.innerHTML = "<p>Carregando...</p>";

  fetch(url)
    .then(res => res.json())
    .then(pokemon => {
      let abilities = pokemon.abilities
        .map(a => a.ability.name)
        .join(", ");
      let types = pokemon.types
        .map(t => t.type.name)
        .join(", ");

      pokemonDetails.innerHTML = `
        <h4>${pokemon.name.toUpperCase()}</h4>
        <img src="${pokemon.sprites.front_default}" alt="${pokemon.name}">
        <p><strong>Altura:</strong> ${pokemon.height}</p>
        <p><strong>Peso:</strong> ${pokemon.weight}</p>
        <p><strong>Tipos:</strong> ${types}</p>
        <p><strong>Habilidades:</strong> ${abilities}</p>
      `;
    });
}
