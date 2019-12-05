from game.test.connect4Board import Board
from datetime import datetime
import copy
from game.test.montecarlo import MCTPlayer
from game.test.connect4Players import AlphaBetaPlayer
from game.test.Node import Node
#Done by Josh


class Game:

    def __init__(self, player1, player2, cols = 7, rows = 6, toWin = 4, show_status=False):
        self.board = Board(player2.symbol)
        self.player1 = player1
        self.player2 = player2
        self.show_status = show_status
        # self.node = Node(state=self.board)
        # print(self.show_status)
        self.decision_times = {self.player1.symbol: 0, self.player2.symbol: 0}
        self.playGame()

    def playGame(self):
        if self.show_status:
            self.board.printBoard()
        node = Node(state=self.board)
        while self.board.stillGoing():
            node = self.playRound(node)
        if self.show_status:
            print("Game over, winner:")
            print(self.check_winner())


    def playRound(self, node):
        start = datetime.now()
        node=self.playTurn(self.player1, node)
        self.decision_times[self.player1.symbol] += (datetime.now() - start).total_seconds()
        if self.board.stillGoing():
            start = datetime.now()
            node=self.playTurn(self.player2, node)
            self.decision_times[self.player2.symbol] += (datetime.now() - start).total_seconds()
        return node


    def playTurn(self, player, node):
        moves = self.board.getValidMoves()
        if moves:
            # currentNode = copy.deepcopy(self.node)
            node, chosen_move = player.get_move(self.board.Clone(), node)
            if not chosen_move in moves:
                print("Error: invalid move made")
            else:
                self.board.insert(chosen_move)
                node = self.goto_childNode(node,chosen_move)
        if self.show_status:
            self.board.printBoard()
        return node

    def goto_childNode(self, node, move):
        for childnode in node.childNodes:
            if childnode.move == move:
                return childnode
        return Node(state=self.board.Clone())


    def check_winner(self):
        return self.board.gotWinner(self.board.player)
        # if winner:
        #     return winner
        # else:
        #     return "TIE"
    def compare_winner(self):
        return self.board.find_winner(self.board.player)


    def get_decision_times(self):
        return self.decision_times



def compare_players(player1, player2, numGames):
    game_count_map = {player1.symbol: 0, player2.symbol: 0, "TIE": 0}
    time_elapsed_map = {player1.symbol: 0, player2.symbol: 0}
    for i in range(1, numGames + 1):
        if i % 1 == 0:
            # pass
            print(i, "games finished")

        # swap who goes first
        if i % 2 == 0:
            game = Game(player1, player2, show_status=True)
        else:
            game = Game(player2, player1, show_status=True)
        # game = Game(player1, player2, show_status=True)
        game_count_map[game.compare_winner()] += 1
        decision_times = game.get_decision_times()
        for symbol in decision_times:
            time_elapsed_map[symbol] += decision_times[symbol]
    print(game_count_map)
    print(time_elapsed_map)

def main():
    # game = Game(MCTPlayer(0), AlphaBetaPlayer(1,2), show_status=True)
    # compare_players(MCTPlayer(0),MCTPlayer(1), 5)
    compare_players(MCTPlayer(0), AlphaBetaPlayer(1, 2), 5)
    compare_players(AlphaBetaPlayer(0, 2), MCTPlayer(1), 5)
    # game = Game(AlphaBetaPlayer(0, 2), AlphaBetaPlayer(1, 2), show_status=True)
    print("Finished")

if __name__ == "__main__":
    main()