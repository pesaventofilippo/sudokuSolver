from board import Board
import sys


def solve(board):
    if not board.isFull():
        x, y = board.nextFree()
        for i in range(1, len(board) + 1):
            if board.tryInsert(i, x, y):
                solve(board)
                board.insertAt(0, x, y)
        return
    else:
        askMore(board)


def askMore(board):
    if board.solved():
        print(board)
        if "--all" not in sys.argv:
            print(" * Solution found!")
            if "--first" in sys.argv:
                sys.exit(0)
            retry = input("   Search for other solutions? (Y/n): ")
            if retry.lower() in ["n", "no"]:
                sys.exit(0)


def main():
    print("--- Python Sudoku Solver ---")

    sizeStr = input(" * Enter board size (4, 9, or 16) [9]: ")
    if not sizeStr: sizeStr = "9"
    try:
        board = Board(size=int(sizeStr))
        if len(board) > 16 and "--unlock" not in sys.argv:
            print(" ** The specified board size is too large.")
            sys.exit(1)
        print(f" * Created board of size {sizeStr}x{sizeStr}.")
        if len(board) > 9:
            print(" * WARNING: Large boards can take extremely long to solve.")
    except Exception:
        print(" ** Error: the provided size is not valid.\n"
              "    Supported boards are: 4x4, 9x9 or 16x16.")
        sys.exit(1)

    if "--empty" not in sys.argv:
        print("\n"
              " * Insert the numbers on the table, one row at a time.\n"
              "   Use '0' to signal emtpy spaces.\n"
              "   IMPORTANT: if the board size is 16, separate single numbers by a space, eg. \"11 2 15 7\"\n")

        mat = []
        for i in range(len(board)):
            rowStr = input(f"Row {i+1}: ")
            digits = rowStr.split(" ")
            if len(digits) == 1:
                digits = [x for x in rowStr]
            try:
                rowArr = [int(x) for x in digits]
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
    input(" * Press enter to start solving!")
    print("   Solving...\n")
    solve(board)

    print(" ** No solutions found.")


if __name__ == '__main__':
    main()
