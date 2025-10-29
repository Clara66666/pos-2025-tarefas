
import "./style.css";
import { renderPokemonList } from "./dom.js";

document.addEventListener('DOMContentLoaded', () => {
  document.querySelector("#app").innerHTML = `
 
    <h1 class="text-center mb-4">⚡ Cliente Web - PokeAPI (Vite)</h1>

    <div class="row">
      <div class="col-md-4">
        <h3>Pokémons</h3>
        <ul id="pokemonList" class="list-group"></ul>
      </div>

      <div class="col-md-8">
        <h3>Detalhes</h3>
        <div id="pokemonDetails" class="card p-3">
          <p>Selecione um Pokémon para ver os detalhes.</p>
        </div>
      </div>
    </div>

`;

renderPokemonList();

})
