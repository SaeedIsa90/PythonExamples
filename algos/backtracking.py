# Creating helper functions
def print_sudoku(board):
    """
    Print sudoku board as matrix 9x9 with 3x3 each box
    """
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


def find_next_empty_cell(board):
    """
    Finds next empty cell in all the board and returns row, col tuple
    """
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)  # row, col

    return None


ex_board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

# print example
print_sudoku(ex_board)
# find example
print('\nfind empty cell example', find_next_empty_cell(ex_board))


# validation
def valid_board(board, num, pos):
    """
    pos: (row, col)

    Checks if assiging num in position gives valid board or not.
    """
    # Check row - if any number in the row == num
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column - if any number in the col == num
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box - if any number in 3x3 box == num
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True


# check row example
print('\ninvalid row ex', valid_board(ex_board, 4, (0, 2)))
# check column example
print('invalid col ex', valid_board(ex_board, 7, (0, 2)))
# check box example
print('invalid box ex', valid_board(ex_board, 6, (0, 2)))
# Valid example
print('valid', valid_board(ex_board, 3, (0, 2)))


def solve_sudoku(board):
    # Find next cell to solve
    find = find_next_empty_cell(board)
    if not find:
        return True       # did not find any empty cell - filled all cells ==> solved
    else:
        row, col = find   # found empty cell --> assigning to row, col

    for i in range(1,10):
        # Checking if assigning i in (row, col) gives valid solution
        if valid_board(board, i, (row, col)):
            # here --> means i gave valid solution
            board[row][col] = i              # assigning i to (row, col) cell

            if solve_sudoku(board):                 # Solve the next empty cell
                return True

            board[row][col] = 0              # here --> means this approach does not give valid solution, assiging 0 back to this cell

    return False


print('\n----------------before solving-------------------------')
print_sudoku(ex_board)
print('-----------------after solving--------------------------')
solve_sudoku(ex_board)
print_sudoku(ex_board)
