from game.connect4Board import Board
from game.connect4Players import *
import numpy as np
import random
#Should take the connect 4 board and convert it to a list that can be input to the ML algorithm
#List should be 4q elements long, one element for each of the 42 spaces on the board
#Sets an empty space to 0, your space to 1, and enemy space to -1, will not be using a bias unit



def board_to_string(board, symbol):
    grid = board.board
    list = ''
    for i in range(board.cols):
        for j in range(board.rows):
            spot = grid[i][j]
            if spot == symbol:#You control space
                list = list + '1'
            elif spot == '.':#Space is neutral
                list = list + '0'
            else:#Enemy controls space
                list = list + '2'
    return list



class ReinforcementAgent:

    def __init__(self, symbol, exp_rate = 0.3, lr = 0.2, decay_gamma = 0.9):
        self.states = []
        self.state_vals = {}
        self.exp_rate = exp_rate
        self.lr = lr
        self.decay_gamma = decay_gamma
        self.symbol = symbol


    def exploration_move(self, board):
        if np.random.uniform(0, 1) <= self.exp_rate: #exploratory move (random)
            return random.choice(board.getValidMoves())
        else:
            max = -inf
            moves = board.getValidMoves()
            random.shuffle(moves)
            for move in moves:
                nextBoard = copy.deepcopy(board)
                nextBoard.insert(move, self.symbol)
                boardString = board_to_string(nextBoard, self.symbol)
                if self.state_vals.get(boardString) is None:
                    value = 0
                else:
                    value = self.state_vals[boardString]
                if value >= max:
                    max = value
                    moveToMake = move
            return moveToMake

    def get_move(self, board):
        return self.exploration_move(board)

        #     value_max = -999
        #     for p in positions:
        #         next_board = current_board.copy()
        #         next_board[p] = symbol
        #         next_boardHash = self.getHash(next_board)
        #         value = 0 if self.states_value.get(next_boardHash) is None else self.states_value.get(next_boardHash)
        #         # print("value", value)
        #         if value >= value_max:
        #             value_max = value
        #             action = p
        #     # print("{} takes action {}".format(self.name, action))
        # return action





def test():
    base = Board()
    player = HumanPlayer("R")
    base.insert(1, "R")
    base.insert(0, "Y")
    base.insert(1, "Y'")
    base.insert(1, "R")
    list = board_to_string(base, player)
    print(len(list))
    print(list)


def main():
    test()
