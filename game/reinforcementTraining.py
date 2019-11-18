from game.connect4Board import Board
from game.connect4Players import *
import numpy as np
import random
#Should take the connect 4 board and convert it to a list that can be input to the ML algorithm
#List should be 43 elements long, 1 bias unit and one element for each of the 42 spaces on the board
#Sets an empty space to 0, your space to 1, and enemy space to -1



def board_to_column(board, player):
    grid = board.board
    list = [1] #starts with bias unit
    symbol = player.symbol
    for i in range(board.cols):
        for j in range(board.rows):
            spot = grid[i][j]
            if spot == symbol:
                list.append(1)
            elif spot == '.':
                list.append(0)
            else:
                list.append(-1)
    return list

class ReinforcementAgent:

    def __init__(self, symbol, exp_rate = 0.3, lr = 0.2, decay_gamma = 0.9):
        self.states = []
        self.state_vals = {}
        self.exp_rate = exp_rate
        self.lr = lr
        self.decay_gamma = decay_gamma


    def exploration_move(self, board):
        if np.random.uniform(0, 1) <= self.exp_rate: #exploratory move (random)
            return random.choice(board.getValidMoves())




def test():
    base = Board()
    player = HumanPlayer("R")
    base.insert(1, "R")
    base.insert(0, "Y")
    base.insert(1, "Y'")
    base.insert(1, "R")
    list = board_to_column(base, player)
    print(len(list))
    print(list)


def main():
    test()
