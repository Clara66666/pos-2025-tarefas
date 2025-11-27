import React from 'react'

export default function PokemonList({ pokemons = [], onSelect, selectedUrl }) {
  if (!pokemons.length) return <p>Nenhum pokémon encontrado.</p>

  return (
    <ul className="pokemon-list">
      {pokemons.map(p => (
        <li
          key={p.name}
          onClick={() => onSelect(p.url)}
          className={p.url === selectedUrl ? 'selected' : ''}
          role="button"
          tabIndex={0}
          onKeyDown={(e) => { if (e.key === 'Enter') onSelect(p.url) }}
        >
          <div className="small"><strong>{p.name}</strong></div>
          <div className="small">#{p.name}</div>
        </li>
      ))}
    </ul>
  )
}
