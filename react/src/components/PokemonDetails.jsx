import React from 'react'

export default function PokemonDetails({ pokemon }) {
  if (!pokemon) return null

  const sprite = pokemon.sprites?.front_default || ''
  const types = pokemon.types?.map(t => t.type.name).join(', ') || ''
  const abilities = pokemon.abilities?.map(a => a.ability.name).join(', ') || ''
  const stats = pokemon.stats || []

  return (
    <div className="pokemon-details">
      <h2 style={{textTransform:'capitalize'}}>{pokemon.name} <small>#{pokemon.id}</small></h2>
      <div style={{display:'flex', gap:16, alignItems:'center'}}>
        <div className="sprite">{sprite ? <img src={sprite} alt={pokemon.name} /> : '—'}</div>
        <div>
          <p><strong>Tipos:</strong> {types}</p>
          <p><strong>Habilidades:</strong> {abilities}</p>
          <p><strong>Altura:</strong> {pokemon.height} — <strong>Peso:</strong> {pokemon.weight}</p>
        </div>
      </div>

      <h3>Stats</h3>
      <ul>
        {stats.map(s => (
          <li key={s.stat.name}>{s.stat.name}: {s.base_stat}</li>
        ))}
      </ul>
    </div>
  )
}
