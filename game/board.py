#! /usr/bin/env python3
from itertools import groupby, chain

NONE = '.'
RED = 'R'
YELLOW = 'Y'

def diagonalsPos (matrix, cols, rows):
    """Get positive diagonals, going from bottom-left to top-right."""
    for di in ([(j, i - j) for j in range(cols)] for i in range(cols + rows -1)):
        yield [matrix[i][j] for i, j in di if i >= 0 and j >= 0 and i < cols and j < rows]

def diagonalsNeg (matrix, cols, rows):
    """Get negative diagonals, going from top-left to bottom-right."""
    for di in ([(j, i - cols + j + 1) for j in range(cols)] for i in range(cols + rows - 1)):
        yield [matrix[i][j] for i, j in di if i >= 0 and j >= 0 and i < cols and j < rows]

class Board:
    def __init__ (self, cols = 7, rows = 6, requiredToWin = 4):
        """Create a new game."""
        self.cols = cols
        self.rows = rows
        self.win = requiredToWin
        self.board = [[NONE] * rows for _ in range(cols)]

    def insert (self, column, color):
        """Insert the color in the given column."""
        if column not in self.getValidMoves():
            raise Exception('Invalid Entry')
        c = self.board[column]
        if c[0] != NONE:
            raise Exception('Column is full')

        i = -1
        while c[i] != NONE:
            i -= 1
        c[i] = color


    def getValidMoves(self):
        moves = []
        for i in range(self.cols):
            c = self.board[i]
            if c[0] == NONE:
                moves.append(i)
        return moves

    def isValid(self, column):
        c = self.board[column]
        if c[0] == NONE:
            return True
        else:
            return False

    def stillGoing(self):
        moves = self.getValidMoves()
        if moves and (not self.getWinner()):
            return True
        else:
            return False

    def checkForWin(self):
        """Check the current board for a winner."""
        w = self.getWinner()
        if w:
            self.printBoard()
            raise Exception(w + ' won!')

    def getWinner(self):
        """Get the winner on the current board."""
        lines = (
            self.board, # columns
            zip(*self.board), # rows
            diagonalsPos(self.board, self.cols, self.rows), # positive diagonals
            diagonalsNeg(self.board, self.cols, self.rows) # negative diagonals
        )

        for line in chain(*lines):
            for color, group in groupby(line):
                if color != NONE and len(list(group)) >= self.win:
                    return color


        return None

    def printBoard (self):
        """Print the board."""
        print('  '.join(map(str, range(self.cols))))
        for y in range(self.rows):
            print('  '.join(str(self.board[x][y]) for x in range(self.cols)))
        print()


if __name__ == '__main__':
    g = Board()
    turn = RED
    while True:
        g.printBoard()
        row = input('{}\'s turn: '.format('Red' if turn == RED else 'Yellow'))
        g.insert(int(row), turn)
        turn = YELLOW if turn == RED else RED