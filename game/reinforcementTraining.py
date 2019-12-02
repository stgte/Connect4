from game.connect4Board import Board
from game.connect4Players import *
import numpy as np
import random
import pickle



#Taking an input board and converting it to a string, useful for hashing

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

    def changeExp(self, rate):
        self.exp_rate = rate

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

    def best_move(self, board):
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
        if boardString not in self.states:
            self.states.append(boardString)
        return moveToMake

    def feedReward(self, reward):
        for state in reversed(self.states):
            if self.state_vals.get(state) is None:
                self.state_vals[state] = 0
            self.state_vals[state] += self.lr * (self.decay_gamma * reward - self.state_vals[state])




    def get_move(self, board):
        return self.exploration_move(board)

    def savePolicy(self, title):
        fw = open('policy_' + str(title), 'wb')
        pickle.dump(self.states_value, fw)
        fw.close()

    def loadPolicy(self, file):
        fr = open(file, 'rb')
        self.states_value = pickle.load(fr)
        fr.close()





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
