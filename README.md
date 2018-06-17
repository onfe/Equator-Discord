# Equator for Discord
A simple bot for Discord, designed to make discussion around equations much less stressful.

## Syntax
Equator follows a simple syntax designed to be easy to understand.

Call Equator to format an equation with `/equation` or the shorthand `/eq`.

### Subscript
`sub( <numbers and/or charge> )`
e.g. `Clsub(2)` produces Cl₂

Numbers [0-9] and charges [+/-] are replaced with their subscript equivalents.

### Superscript
`sup( <numbers and/or charge> )` (or alias `^( <numbers and/or charge> )`).
e.g. `Mgsup(2+)` produces Mg²

Numbers [0-9] and charges [+/-] are replaced with their superscript equivalents.

### Equilibrium and Reaction arrows
`[to]` gives →

`[equil]` gives ⇌

### Protons and Electrons

`[e]` gives *e⁻*

`[h]` gives H⁺

`[oh]` gives OH⁻

### Greek Symbols

`[D]` gives Δ (uppercase delta)

`[d]` gives δ (lowercase delta)

`[pi]` gives π

`[S]` gives Σ

### State Symbols
Due to limitations with the Unicode standard, and no way to implement HTML-based subscript in discord, state symbols such as Solid, Liquid, Gas and Aqueous are not available at this time.

TODO: Use tables instead of `xyz` gives xyz.

## Credits
Code by [Onfe](https://www.onfe.co.uk)

Equator's Discord icon contains art by [Freepik](http://www.freepik.com), licensed under [CC 3.0 BY](https://creativecommons.org/licenses/by/3.0/).
