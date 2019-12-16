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

#Takes a board string and returns the same board state flipped over the vertical axis
def flip_string(boardString):
    columns = []
    for i in range(7):
        firstPlace = i * 6
        secondPlace = (i + 1) * 6
        column = boardString[firstPlace:secondPlace]
        columns.append(column)
    flippedString = ''
    for j in range(7):
        flippedString = flippedString + columns[6 - j]
    return flippedString

#Returns the flipped column, for example turns the first column (index 0) into the last column (index 6)
def flip_column(column):
    return 6 - column



class ReinforcementAgent:

    def __init__(self, symbol, exp_rate = 0.3, lr = 0.2, decay_gamma = 0.9):
        self.states = []
        self.state_vals = {}
        self.exp_rate = exp_rate
        self.lr = lr
        self.decay_gamma = decay_gamma
        self.symbol = symbol

    def change_exp(self, rate):
        self.exp_rate = rate

    def exploration_move(self, board):
        if np.random.uniform(0, 1) <= self.exp_rate: #exploratory move (random)
            move = random.choice(board.getValidMoves())
            nextBoard = copy.deepcopy(board)
            nextBoard.insert(move, self.symbol)
            boardString = board_to_string(nextBoard, self.symbol)

            self.states.append(boardString)
            return move
        else:
            max = -inf
            moves = board.getValidMoves()
            random.shuffle(moves)
            for move in moves:
                nextBoard = copy.deepcopy(board)
                nextBoard.insert(move, self.symbol)
                boardString = board_to_string(nextBoard, self.symbol)
                flipped = False
                if self.state_vals.get(boardString) is not None:
                    value = self.state_vals[boardString]
                elif self.state_vals.get(flip_string(boardString)) is not None: #checks if you've seen the flipped board state
                    value = self.state_vals[flip_string(boardString)]
                    flipped = True
                else:
                    value = 0
                if value >= max:
                    max = value
                    moveToMake = move
                    stateToAdd = boardString
                    if flipped:
                        moveToMake = flip_column(moveToMake) #If you are basing your choice off the flipped board adds the correct board state and returns the correct move
                        stateToAdd = flip_string(stateToAdd)
            self.states.append(stateToAdd)
            return moveToMake

    #Backpropogates to reward/punish good/bad moves
    def feed_reward(self, reward):
        for state in reversed(self.states):
            if self.state_vals.get(state) is None:
                self.state_vals[state] = 0
            self.state_vals[state] += self.lr * (self.decay_gamma * reward - self.state_vals[state])
            reward = self.state_vals[state]
    #Need to empty states after each game
    def reset(self):
        self.states = []

    def get_move(self, board):

        return self.exploration_move(board)

    def save_policy(self, title):
        fw = open('policy_' + str(title), 'wb')
        pickle.dump(self.state_vals, fw)
        fw.close()

    def load_policy(self, file):
        fr = open(file, 'rb')
        self.state_vals = pickle.load(fr)
        fr.close()





def test():
    board1 = Board()
    board2 = Board()
    board1.insert(0, 'R')
    board2.insert(6, 'R')
    firstString = board_to_string(board1, 'R')
    secondString = board_to_string(board2, 'R')
    secondString = flip_string(secondString)
    print("Should be True: " + str(firstString == secondString))
    board1 = Board()
    board2 = Board()
    board1.insert(1, 'Y')
    board2.insert(5, 'Y')
    board1.insert(3, 'R')
    board2.insert(3, 'R')
    firstString = board_to_string(board1, 'R')
    secondString = board_to_string(board2, 'R')
    secondString = flip_string(secondString)
    print("Should be True: " + str(firstString == secondString))
    board1 = Board()
    board2 = Board()
    board1.insert(1, 'Y')
    firstString = board_to_string(board1, 'R')
    secondString = board_to_string(board2, 'R')
    secondString = flip_string(secondString)
    print("Should be False: " + str(firstString == secondString))





def main():
    test()
