from copy import deepcopy
from exceptions import *


class Board(object):
    __board = None
    __emptyChar = 'x'
    __rowDiv = '-'
    __colDiv = '|'
    
    def __init__(self):
        self.__board = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]

    def __str__(self):
        outStr = ""
        for row in range(9):
            for col in range(9):
                outStr += self.charAt(row, col) + ' '
                if (col == 2) or (col == 5):
                    outStr += self.__colDiv + ' '
            outStr = outStr.strip() + '\n'
            if (row == 2) or (row == 5):
                outStr += (self.__rowDiv * 21) + '\n'
        return outStr

    @staticmethod
    def isValidMatrix(matrix: list):
        # General checks
        if len(matrix) != 9:
            raise InvalidSizeBoardError
        for row in matrix:
            if len(row) != 9:
                raise InvalidSizeBoardError
            try:
                if not all([0 <= x <= 9 for x in row]):
                    raise InvalidCharactersError
            except TypeError:
                raise InvalidCharactersError

        # Check rows and colums
        for index in range(9):
            thisRow = matrix[index]
            thisCol = [matrix[x][index] for x in range(9)]
            if not all([(thisRow.count(x) <= 1) and (thisCol.count(x) <= 1) for x in range(1, 10)]):
                raise InvalidCombinationError

        # Check 3x3 squares
        for squareX in range(0, 9, 3):
            for squareY in range(0, 9, 3):
                squareList = []
                for innerX in range(squareX, squareX+3):
                    for innerY in range(squareY, squareY+3):
                        squareList.append(matrix[innerX][innerY])
                if not all([squareList.count(x) <= 1 for x in range(1, 10)]):
                    raise InvalidCombinationError

        # No errors!
        return True

    def fromMatrix(self, matrix: list):
        if self.isValidMatrix(matrix):
            # Deepcopy array to prevent memory overlapping
            self.__board = deepcopy(matrix)

    def toMatrix(self):
        return deepcopy(self.__board)

    def numberAt(self, row: int, column: int):
        return self.__board[row][column]

    def charAt(self, row: int, column: int):
        digit = self.numberAt(row, column)
        return str(digit) if digit else self.__emptyChar

    def print(self):
        print(self)

    def changeFormat(self, emptyChar: str=__emptyChar, rowDiv: str=__rowDiv, colDiv: str=__colDiv):
        self.__emptyChar = emptyChar
        self.__rowDiv = rowDiv
        self.__colDiv = colDiv

    def reset(self):
        self.__init__()

    def validate(self):
        return self.isValidMatrix(self.__board)

    def nextFree(self):
        for row in range(9):
            for col in range(9):
                if self.numberAt(row, col) == 0:
                    return row, col
        raise FullBoardError

    def isFull(self):
        try:
            self.nextFree()
            return False
        except FullBoardError:
            return True

    def solved(self):
        if not self.validate():
            return False

        # Check rows and colums
        for index in range(9):
            thisRow = self.__board[index]
            thisCol = [self.numberAt(x, index) for x in range(9)]
            if not all([(thisRow.count(x) == 1) and (thisCol.count(x) == 1) for x in range(1, 10)]):
                return False

        # Check 3x3 squares
        for squareX in range(0, 9, 3):
            for squareY in range(0, 9, 3):
                squareList = []
                for innerX in range(squareX, squareX + 3):
                    for innerY in range(squareY, squareY + 3):
                        squareList.append(self.numberAt(innerX, innerY))
                if not all([squareList.count(x) == 1 for x in range(1, 10)]):
                    return False
        return True

    def insertAt(self, number: int, row: int, column: int):
        self.__board[row][column] = number

    def tryInsert(self, number: int, row: int, column: int):
        prevState = self.toMatrix()
        self.insertAt(number, row, column)
        try:
            self.validate()
            return True
        except:
            self.fromMatrix(prevState)
            return False
