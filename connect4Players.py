import random


class HumanPlayer:
    def __init__(self, symbol, playerNum):
        self.symbol = symbol
        self.playerNum = playerNum

    def get_move(self, board):
        #takes player's move input
        #returns move as an int
        movelist= board.calc_valid_moves()
        move = int(input("Enter column number:"))
        while move not in movelist:
            print("Invalid move")
            move = int(input("Enter column number:"))
        return move

class RandomComputerPlayer:

    def __init__(self, symbol, playerNum):
        self.symbol = symbol
        self.playerNum= playerNum

    def get_move(self, board):
        return random.choice(board.calc_valid_moves())




