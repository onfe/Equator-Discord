# Equator for Discord
A simple bot for Discord that implements the custom chemquation formatter.  
Designed to streamline the writing of chemical equations with a keyboard and improves readability.

## Syntax
Equator follows a simple syntax designed to be easy to understand.

Call Equator to format an equation with `/equation` or the shorthand `/eq`.

# Equator 0.1 syntax
Equator 1 is now depreciated. Please use the Equator 0.2 chemquation syntax.

### Subscript
`sub( <numbers and/or charge> )`
e.g. `Clsub(2)` produces Cl₂

Numbers [0-9] and charges [+/-] are replaced with their subscript equivalents.

### Superscript
`sup( <numbers and/or charge> )` (or alias `^( <numbers and/or charge> )`).
e.g. `Mgsup(2+)` produces Mg²

Numbers [0-9] and charges [+/-] are replaced with their superscript equivalents.

### Equilibrium and Reaction arrows
`=>` | →
`<=>` | ⇌

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


## Credits
Code by [Onfe](https://www.onfe.co.uk)

Equator's Discord icon contains art by [Freepik](http://www.freepik.com), licensed under [CC 3.0 BY](https://creativecommons.org/licenses/by/3.0/).
