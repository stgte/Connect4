#! /usr/bin/env python3
from itertools import groupby, chain
import copy

NONE = '.'

def diagonalsPos (matrix, cols, rows):
    """Get positive diagonals, going from bottom-left to top-right."""
    for di in ([(j, i - j) for j in range(cols)] for i in range(cols + rows -1)):
        yield [matrix[i][j] for i, j in di if i >= 0 and j >= 0 and i < cols and j < rows]

def diagonalsNeg (matrix, cols, rows):
    """Get negative diagonals, going from top-left to bottom-right."""
    for di in ([(j, i - cols + j + 1) for j in range(cols)] for i in range(cols + rows - 1)):
        yield [matrix[i][j] for i, j in di if i >= 0 and j >= 0 and i < cols and j < rows]

class Board:
    def __init__ (self, symbol, cols = 7, rows = 6, requiredToWin = 4):
        """Create a new game."""
        self.cols = cols
        self.rows = rows
        self.win = requiredToWin
        self.board = [[NONE] * rows for _ in range(cols)]
        self.player = symbol

    def Clone(self):
        clone = Board(self.player)
        clone.board = copy.deepcopy(self.board)
        clone.player = self.player

        return clone

    def insert1 (self, column, color):
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

    def insert (self, column):
        """Insert the color in the given column."""
        # if column not in self.getValidMoves():
        #     print(column)
        #     raise Exception('Invalid Entry')
        c = self.board[column]
        # if c[0] != NONE:
        #     raise Exception('Column is full')

        i = -1
        while c[i] != NONE:
            i -= 1
        self.player ^= 1
        c[i] = self.player


    def result(self, player):
        if self.winner(player):
            return 1  # player wins
        elif self.winner(player^1):
            return 0  # if opponent wins
        elif self.draw():
            return 0.5
        # if not self.stillGoing():
        #     if self.getWinner()==player: return 1 # player wins
        #     elif self.getWinner()==player^1: return 0 # if opponent wins
        #     else: return 0.5
        # return 0


    def getValidMoves(self):
        if self.getWinner() != None:
            return []
        # if self.winner(self.player) or self.winner(self.player ^ 1): return []
        moves = []
        for i in range(self.cols):
            c = self.board[i]
            if c[0] == NONE:
                moves.append(i)
        # random.shuffle(moves)
        # print(moves)
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

    def draw(self):  # is it draw?
        return not self.getValidMoves() and not self.winner(self.player) and not self.winner(self.player^1)

    def winner(self, c):
        lines = (
            self.board,  # columns
            zip(*self.board),  # rows
            diagonalsPos(self.board, self.cols, self.rows),  # positive diagonals
            diagonalsNeg(self.board, self.cols, self.rows)  # negative diagonals
        )

        for line in chain(*lines):
            for color, group in groupby(line):
                if color != NONE and len(list(group)) >= self.win:
                    # print(color)
                    return c==color
        return False

    def gotWinner(self, player):
        if self.winner(player):
            return 'player '+str(self.player)  # player wins
        elif self.winner(player^1):
            return 'player ' +str(self.player)# if opponent wins
        elif self.draw():
            return 'TIE'

    def find_winner(self, player):
        if self.winner(player):
            return player  # player wins
        elif self.winner(player^1):
            return player^1 # if opponent wins
        elif self.draw():
            return 'TIE'


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
        curr_board = copy.deepcopy(self.board)
        for y in range(self.rows):
            for x in range(self.cols):
                if curr_board[x][y]==1: curr_board[x][y]= "R"
                if curr_board[x][y] == 0: curr_board[x][y] = "Y"
        for y in range(self.rows):
            print('  '.join(str(curr_board[x][y]) for x in range(self.cols)))
        print()


if __name__ == '__main__':
    g = Board()
    turn = RED
    while True:
        g.printBoard()
        row = input('{}\'s turn: '.format('Red' if turn == RED else 'Yellow'))
        g.insert(int(row), turn)
        turn = YELLOW if turn == RED else RED