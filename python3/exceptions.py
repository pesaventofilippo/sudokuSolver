# Board Exceptions

class InvalidSizeBoardError(Exception):
    def __init__(self):
        self.message = "The provided board has an invalid size. It must be a 9x9 matrix."


class InvalidCharactersError(Exception):
    def __init__(self):
        self.message = "The board contains invalid characters. They must be 1-9 or 0 to represent empty space."


class InvalidCombinationError(Exception):
    def __init__(self):
        self.message = "The board has an invalid state, and it is breaking the Sudoku rules."


class FullBoardError(Exception):
    def __init__(self):
        self.message = "The board is already full."
