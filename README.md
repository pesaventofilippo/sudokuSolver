# sudokuSolver
Fast Sudoku solver, written using the "recursion with backtracking" technique.  
*Disclaimer*: this program isn't designed to be super-efficient, but rather to explicitly use the backtracking algorithm.
With that said, boards up to 9x9 still get solved pretty easily.

## Features
- Can support boards of all sizes (4x4, 9x9, 16x16...)
- Boards larger than 16x16 are not available by default, given the long time required to solve them (see debug flags)
- Quite fast solving time for 4x4 and 9x9 boards
- Generate all solutions, but print one as soon as it's been found
- CLI mode is highly interactive

## Debug flags
- `--empty` - Do not ask for rows, generate empty table
- `--first` - Generate only first solution, then exit
- `--all` - Keep generating solutions without waiting for user input (overrides `--first`)
- `--unlock` - Allow for boards larger than 16x16.  
  **Warning**: large boards take *extremely* long to solve.

## Available in
- [x] Python CLI
- [ ] Python GUI

I don't know if or when I'll publish the other versions listed above, but I plan to finish them sooner or later.
