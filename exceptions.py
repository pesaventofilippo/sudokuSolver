# Board Exceptions

class InvalidSizeBoardError(Exception):
    def __init__(self):
        self.message = "Cannot create a board of this size. Size must be either 4, 9, or 16."


class InvalidCharactersError(Exception):
    def __init__(self):
        self.message = "The board contains invalid characters. They must be a valid number or 0 to represent empty space."


class InvalidCombinationError(Exception):
    def __init__(self):
        self.message = "The board has an invalid state, and it is breaking the Sudoku rules."


class FullBoardError(Exception):
    def __init__(self):
        self.message = "The board is already full."
