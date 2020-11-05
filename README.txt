Jun Sung Tak (jtak01)
comp131
HW3 CSP approach to a sudoku solver

run with: python csp.py
Tested with: Easy puzzle, Evil puzzle (board, board1 respectively), various
other puzzles from online

Currently only 9x9 sudokus are supported
The program takes extra amount of time to complete because it prints the
entire board each iteration to show which values are filled in at each step.

Conflict-directed Backjumping may be used but it is not a great approach for
this specific problem. Since there are 9 possible values it takes a greater
time to calculate the conflict sets and do operations. In practice normal
backtracking is actually faster for this problem. 

Sudokus are represented in a 2 dimensional array and each 0 denotes an empty
cell. When printing, the empty cell is printed as a space.
