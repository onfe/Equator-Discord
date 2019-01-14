# Equator for Discord
A simple bot for Discord that implements the custom chemquation formatter.  
Designed to streamline the writing of chemical equations with a keyboard and improves readability.

## Syntax
Equator follows a simple syntax designed to be easy to understand.  
The new syntax aims to be quicker to learn as it's much closer to writing equations normally.

Call Equator to format an equation with `/equation` or the alias `/eq`.

**Equator v0.1 is now depreciated. Please use the Equator v0.2 (chemquation) syntax below.**

### Basics
Equator formats equations assuming they are written with correct spacing and capitalisation.  
An equation is built from compounds (e.g. `H2O`) and symbols (e.g. `=>`), with spaces between each item.

#### Compounds
Within each compound, Equator looks for the following attributes:
- **Quantity** *(Optional)*  
  The integer before the first element denotes the quantity of the compound.  
  *Defaults to 1 if not specified.*

- **Constituent elements**  
  A sequence of elements (see below) with their respective quantities.  
  Every compound must contain at least one (1) element.

- **State** *(Optional)*  
  The state of the compound, in brackets (e.g. `(s)`)  
  Supported states: solid `(s)`, liquid `(l)`, gas `(g)`, aqueous `(aq)` and plasma `(p)`.  

- **Charge** *(Optional)*  
  Denoted by `+/-<integer>` at the end of the compound. (e.g. `+1`)

#### Elements
Elements are the foundation of equations in equator. They must start with a capital letter. The quantity of the element is placed after the element. (e.g `Cl2` for a chlorine molecule)

### Superscript
Docs coming soon...

### Symbols and Shorthand
  In  |  Out  |  Example Input         | Example Output
:----:|:-----:|:-----------------------|----------------
 `=>` |   →   | `/eq 2H2 + O2 => 2H2O` | 2H₂ + O₂ → 2H₂O
 `<=>`|   ⇌   | `/eq A + B <=> AB`     | A + B ⇌ AB
 `[e]`|  *e⁻* ||
 `[h]`|   H⁺  ||
`[oh]`|  OH⁻  ||
 `[D]`|   Δ   ||
 `[d]`|   δ   ||
`[pi]`|   π   ||
 `[S]`|   Σ   ||

### State Symbols
State symbols are finally here! Each compound can have a state, check it out!


## Credits
Code by [Onfe](https://www.onfe.co.uk)

Equator's Discord icon contains art by [Freepik](http://www.freepik.com), licensed under [CC 3.0 BY](https://creativecommons.org/licenses/by/3.0/).
