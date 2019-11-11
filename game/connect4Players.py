import random

class HumanPlayer:
    def __init__(self, symbol):
        self.symbol = symbol

    def get_move(self, board):
        #takes player's move input
        #returns move as an int
        movelist= board.getValidMoves()
        move = int(input("Enter column number:"))
        while move not in movelist:
            print("Invalid move")
            move = int(input("Enter column number:"))
        return move

class RandomComputerPlayer:

    def __init__(self, symbol):
        self.symbol = symbol

    def get_move(self, board):
        return random.choice(board.getValidMoves())


class TestAgent0:
    def __init__(self, symbol):
        self.symbol = symbol

    def get_move(self, board):
        return 0










