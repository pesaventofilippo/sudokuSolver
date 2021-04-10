from copy import deepcopy
from exceptions import *


class Board(object):
    __board = None
    __sizeLen = None
    __squareLen = None
    __emptyChar = 'x'
    __rowDiv = '-'
    __colDiv = '|'
    
    def __init__(self, size: int=9):
        newTab = []
        for x in range(size):
            row = []
            for y in range(size):
                row.append(0)
            newTab.append(row)
        self.__board = newTab
        self.__sizeLen = size
        self.__squareLen = int(size**0.5)
        if (size**0.5) % 1 > 0:
            raise InvalidSizeBoardError

    def __str__(self):
        outStr = ""
        for row in range(self.__sizeLen):
            for col in range(self.__sizeLen):
                outStr += self.charAt(row, col) + ' '
                if (col % self.__squareLen == self.__squareLen-1) and not (col == self.__sizeLen-1):
                    outStr += self.__colDiv + ' '
            outStr = outStr.strip() + '\n'
            if (row % self.__squareLen == self.__squareLen-1) and not (row == self.__sizeLen-1):
                if self.__sizeLen > 9:
                    div = self.__rowDiv * (3*self.__sizeLen + 2*self.__squareLen -3)
                else:
                    div = self.__rowDiv * (2*self.__sizeLen + 2*self.__squareLen -3)
                outStr += div + '\n'
        return outStr

    def __sizeof__(self):
        return self.__sizeLen * self.__sizeLen

    def __len__(self):
        return self.__sizeLen

    def __eq__(self, other):
        return self.toMatrix() == other.toMatrix()

    def isValidMatrix(self, matrix: list):
        # General checks
        if len(matrix) != self.__sizeLen:
            raise InvalidSizeBoardError
        for row in matrix:
            if len(row) != self.__sizeLen:
                raise InvalidSizeBoardError
            try:
                if not all([0 <= x <= self.__sizeLen for x in row]):
                    raise InvalidCharactersError
            except TypeError:
                raise InvalidCharactersError

        # Check rows and colums
        for index in range(self.__sizeLen):
            thisRow = matrix[index]
            thisCol = [matrix[x][index] for x in range(self.__sizeLen)]
            if not all([(thisRow.count(x) <= 1) and (thisCol.count(x) <= 1) for x in range(1, self.__sizeLen+1)]):
                raise InvalidCombinationError

        # Check squares
        for squareX in range(0, self.__sizeLen, self.__squareLen):
            for squareY in range(0, self.__sizeLen, self.__squareLen):
                squareList = []
                for innerX in range(squareX, squareX+self.__squareLen):
                    for innerY in range(squareY, squareY+self.__squareLen):
                        squareList.append(matrix[innerX][innerY])
                if not all([squareList.count(x) <= 1 for x in range(1, self.__sizeLen+1)]):
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
        if digit and self.__sizeLen > 9:
            return str(digit) if digit > 9 else "0" + str(digit)
        elif not digit and self.__sizeLen > 9:
            return 2 * self.__emptyChar
        else:
            return str(digit) if digit else self.__emptyChar

    def print(self):
        print(self)

    def changeFormat(self, emptyChar: str=__emptyChar, rowDiv: str=__rowDiv, colDiv: str=__colDiv):
        self.__emptyChar = emptyChar
        self.__rowDiv = rowDiv
        self.__colDiv = colDiv

    def reset(self):
        self.__init__(self.__sizeLen)

    def validate(self):
        return self.isValidMatrix(self.__board)

    def nextFree(self):
        for row in range(self.__sizeLen):
            for col in range(self.__sizeLen):
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
        for index in range(self.__sizeLen):
            thisRow = self.__board[index]
            thisCol = [self.numberAt(x, index) for x in range(self.__sizeLen)]
            if not all([(thisRow.count(x) == 1) and (thisCol.count(x) == 1) for x in range(1, self.__sizeLen+1)]):
                return False

        # Check squares
        for squareX in range(0, self.__sizeLen, self.__squareLen):
            for squareY in range(0, self.__sizeLen, self.__squareLen):
                squareList = []
                for innerX in range(squareX, squareX + self.__squareLen):
                    for innerY in range(squareY, squareY + self.__squareLen):
                        squareList.append(self.numberAt(innerX, innerY))
                if not all([squareList.count(x) == 1 for x in range(1, self.__sizeLen+1)]):
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
