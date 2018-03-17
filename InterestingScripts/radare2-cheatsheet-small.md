# Cheatsheet
I personally like to use GDB. When I try r2, I got shocked by how I was unable to map old GDB commands to be used in r2.
My favourite commands are mapped to r2 in this way especially the debugging part. 

dynamic analysis with `-d`
static analysis without `-d`

## Must run command
|command|description|
|----|---|
|`aaa`|analyse all
|`s sym.main`| seek main function
|`pdf`| disassemble

## Some r2 Representations

- `sym.main`              => local function
- `sym.imp.printf`        => imported function
- `local_4h`              => same as `rbp-0x4`

## Useful static analysis
|command|description|
|----|---|
|`VV`| Graph|
|`px` / `pxw` / `pxq` | hexdump|
|`/ <string>`|search a string in the entire binary|

## Useful debugging (dynamic)


|command|description|
|----|---|
|`ood` <arg1> <arg2> ...| set args like in gdb |
|`db main`| break main|
|`dc`| continue |

run above before going into Visual Debug mode (V -> p -> p).

    Visual Debug mode will show registers + disass + highlightings

Command Mode with `:`

|command|description|
|----|---|
|`ds`| step|
|`dso`| step over without entering a function |
|`dsf`| step until end of frame (used accidentally enters a function but want to skip)|

Back to visual mode with [Enter]

`s` to step
[shift] + r  to randomize colors (easier to see)

## View registers and data at addresses

### View data
Similar to GDB's examine `x/s` or `x/d` or `x/x`

|command|description|
|----|---|
|`ps @ addr/reg/reg+offset`| print string at the address |
|`pfi @ addr/reg/reg+offset`| print integer at the address |
|`pfx @ addr/reg/reg+offset`| print hex at the address |


### View Registers

|command|description|
|----|---|
| `dr` | see all register (similar to GDB's `info reg`) |
| `dr=` | see registers in more compact form |
| `dr eax` | see value of register in hex |

## String patching

|command|description|
|----|---|
|`s <address>`|seek the addr|
|`oo+`|open in read-write mode|
|`w <string>`|overwrite location with string|


