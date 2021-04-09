from board import Board
from exceptions import FullBoardError
import sys


def solve(board):
    try:
        row, col = board.nextFree()
    except FullBoardError:
        return True

    for i in range(1,10):
        if board.tryInsert(i, row, col):
            if solve(board):
                return True

            board.insertAt(0, row, col)

    return False


def main():
    board = Board()
    mat = []
    print("--- Python Sudoku Solver ---")
    print(" * Insert the numbers on the table, one row at a time.")
    print(" * Use '0' to signal emtpy spaces.\n")

    for i in range(9):
        rowStr = input(f"Row {i+1}: ")
        try:
            rowArr = [int(x) for x in rowStr]
        except ValueError:
            print(" ** Error: invalid digits entered.")
            sys.exit(1)
        mat.append(rowArr)

    try:
        board.fromMatrix(mat)
    except Exception:
        print(" ** Error in creating board. Please check your input.")
        sys.exit(1)

    print("\nLoaded board:")
    print(board)
    print(" * Press enter to start solving!")
    input()
    print(" * Solving...")

    result = solve(board)
    print(board)
    if result:
        print(" * Board solved!")
        print(" * Verifying board...")
        if board.solved():
            print("Board solved correctly!")
            sys.exit(0)
        else:
            print(" ** The solution is incorrect. Please check it by hand.\n"
                  "If you think it should be correct, please file a pull request!")
            sys.exit(1)
    else:
        print(" ** The board could not be solved. Either the board is impossible to solve or there is a bug in the program.\n"
              "If you think it should be solvable, please file a pull request!")
        sys.exit(1)


if __name__ == '__main__':
    main()
