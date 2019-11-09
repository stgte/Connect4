from game.board import Board
from game.connect4Players import *
from datetime import datetime
import copy
#Done by Josh

class Game:

    def __init__(self, player1, player2, cols = 7, rows = 6, toWin = 4, show_status = False):
        self.board = Board(cols, rows, toWin)
        self.player1 = player1
        self.player2 = player2
        self.decision_times = {self.player1.symbol: 0, self.player2.symbol: 0}
        self.play_game(self)

    def playGame(self):
        if self.show_status:
            self.board.printBoard()
        while self.board.stillGoing():
            self.playRound()
        if self.show_status:
            print("Game over, winner:")
            print(self.check_winner())


    def playRound(self):
        start = datetime.now()
        self.playTurn(self.player1)
        self.decision_times[self.player1.symbol] += (datetime.now() - start).total_seconds()
        start = datetime.now()
        self.playTurn(self.player2)
        self.decision_times[self.player2.symbol] += (datetime.now() - start).total_seconds()


    def playTurn(self, player):
        moves = self.board.calc_valid_moves()
        if moves:
            chosen_move = player.get_move(copy.deepcopy(self.board))
            if not chosen_move in moves:
                print("Error: invalid move made")
            else:
                self.board.insert(chosen_move, player.symbol)


    def check_winner(self):
        winner = self.board.getWinner()
        if winner:
            return winner
        else:
            return "TIE"

def main():
    game = Game(HumanPlayer("R"), HumanPlayer("Y"))