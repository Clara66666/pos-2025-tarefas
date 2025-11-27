import React, { useEffect, useState } from "react";
import { fetchPokemonList, fetchPokemonDetails } from "./api/pokeAPI";
import PokemonList from "./components/PokemonList";
import PokemonDetails from "./components/PokemonDetails";

export default function App() {
  const [pokemons, setPokemons] = useState([]);
  const [selectedUrl, setSelectedUrl] = useState(null);
  const [selectedPokemon, setSelectedPokemon] = useState(null);
  const [loadingList, setLoadingList] = useState(false);
  const [loadingDetails, setLoadingDetails] = useState(false);
  const [error, setError] = useState(null);
  const [limit] = useState(20);
  const [offset, setOffset] = useState(0);

  useEffect(() => {
    setLoadingList(true);
    fetchPokemonList(limit, offset)
      .then(data => setPokemons(data.results || []))
      .catch(() => setError("Erro ao carregar lista"))
      .finally(() => setLoadingList(false));
  }, [limit, offset]);

  useEffect(() => {
    if (!selectedUrl) {
      setSelectedPokemon(null);
      return;
    }
    setLoadingDetails(true);
    fetchPokemonDetails(selectedUrl)
      .then(data => setSelectedPokemon(data))
      .catch(() => setError("Erro ao carregar detalhes"))
      .finally(() => setLoadingDetails(false));
  }, [selectedUrl]);

  return (
    <div className="app">
      <header>
        <h1>Cliente PokeAPI — React</h1>
        <p>Lista de pokémons (clique para ver detalhes)</p>
      </header>

      <main className="container">
        <section className="left">
          <div className="controls">
            <button onClick={() => setOffset(o => Math.max(0, o - limit))} disabled={offset === 0}>
              ◀ Anterior
            </button>
            <button onClick={() => setOffset(o => o + limit)}>Próxima ▶</button>
          </div>

          {loadingList ? (
            <p>Carregando lista...</p>
          ) : error ? (
            <p className="error">{error}</p>
          ) : (
            <PokemonList
              pokemons={pokemons}
              onSelect={(url) => setSelectedUrl(url)}
              selectedUrl={selectedUrl}
            />
          )}
        </section>

        <section className="right">
          {loadingDetails ? (
            <p>Carregando detalhes...</p>
          ) : selectedPokemon ? (
            <PokemonDetails pokemon={selectedPokemon} />
          ) : (
            <p>Selecione um Pokémon para ver os detalhes.</p>
          )}
        </section>
      </main>

      <footer>
        Fonte: <a href="https://pokeapi.co" target="_blank">PokeAPI</a>
      </footer>
    </div>
  );
}
