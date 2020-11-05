# Jun Sung Tak 
# Comp131
# Csp hw3 
# Coords are in i, j
# Empty cell is denoted as 0


# Easy puzzle
board = [
    [6,0,8,7,0,2,1,0,0],
    [4,0,0,0,1,0,0,0,2],
    [0,2,5,4,0,0,0,0,0],
    [7,0,1,0,8,0,4,0,5],
    [0,8,0,0,0,0,0,7,0],
    [5,0,9,0,6,0,3,0,1],
    [0,0,0,0,0,6,7,5,0],
    [2,0,0,0,9,0,0,0,8],
    [0,0,6,8,0,5,2,0,3]
]

# Evil puzzle
board1 = [
    [0,7,0,0,4,2,0,0,0],
    [0,0,0,0,0,8,6,1,0],
    [3,9,0,0,0,0,0,0,7],
    [0,0,0,0,0,4,0,0,9],
    [0,0,3,0,0,0,7,0,0],
    [5,0,0,1,0,0,0,0,0],
    [8,0,0,0,0,0,0,7,6],
    [0,5,4,8,0,0,0,0,0],
    [0,0,0,6,1,0,0,5,0]
]


# Takes a 2D array and prints in sudoku form. Empty spaces are printed as " "
def print_board(board):
    print("->  0 1 2   3 4 5   6 7 8 ")
    print("  -------------------------")
    for i in range(len(board)):
        j = 0
        print(str(i) + " ", end="")
        for j in range(len(board[0])):
            if j % 3 == 0:
                print("| ", end="")
            if board[i][j] == 0:
                print("  ", end="")
                continue
            print(str(board[i][j]) + " ", end="")
            if j == 8:
                print("|", end="")
        print("")
        if i % 3 == 2 and i != 0:
            print("  -------------------------")
            continue


# Constraint checker block, row, col major fashion
def constaint_checker(board, val, coord):
    row = coord[0]
    col = coord[1]
    #Checking box constraint
    box_i = col // 3
    box_j = row // 3
    for i in range(box_j * 3, box_j * 3 + 3): #Traverse 3x3 box
        for j in range(box_i * 3, box_i * 3 + 3):
            if (i, j) != coord and board[i][j] == val:
                return False
    #Checking row and col constraints
    for i in range(len(board[0])):
        if col != i and board[row][i] == val: 
            return False
    for j in range(len(board)):
        if row != j and board[j][col] == val: 
            return False
    return True

# Gets the coordinate of the next empty cell
# Returns in tuple
def get_next_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)
    return None


# Main backtracking recursion
# Takes the 2D array to work on and a counter variable to count iterations
def backtrack(board, count):
    #basecase:
    print_board(board)
    count += 1
    coord = get_next_empty(board)
    if coord == None:
        print(f"Took {count} recursive calls")
        print("Sudoku solved!")
        return True
    else: 
        row = coord[0]
        col = coord[1]
    for i in range(1, 10): #Checks 1 through 9
        if constaint_checker(board, i, coord): #Looking for possible values
            board[row][col] = i
            if backtrack(board, count) != False:
                return True
            board[row][col] = 0 #reset value because it was not valid.
            print("Backtracking...")
    return False



backtrack(board, 0)









