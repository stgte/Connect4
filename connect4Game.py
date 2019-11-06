from connect4Board import Connect4Board
import datetime
import copy


class Connect4Game:

    def __init__(self, player1, player2, show_status=True):
        self.player1 = player1
        self.player2 = player2
        self.show_status = show_status
        self.board = Connect4Board()
        self.decision_times = {self.player1.symbol: 0, self.player2.symbol: 0}
        self.play_game()
        self.playerToNum = {player1: 0, player2: 1}

    def play_game(self):
        if self.show_status:
            self.board.print_board()
        while not self.board.check_win():
            self.play_round()
        if self.show_status:
            print("Game over, Final Winner:")
            print(self.board.calc_winner())

    def play_round(self):
        start = datetime.now()
        self.play_move(self.player1)
        self.decision_times[self.player1.symbol] += (datetime.now()-start).total_seconds()
        start = datetime.now()
        self.play_move(self.player2)
        self.decision_times[self.player2.symbol] += (datetime.now()-start).total_seconds()

    def play_move(self, player):
        if self.board.calc_valid_moves():
            chosen_move = player.get_move(copy.deepcopy(self.board))
            if not self.board.add_disc(chosen_move, self.playerToNum[player]):
                print("Error: invalid move made")
            elif self.show_status:
                self.board.print_board()
                print_scores(self.board.calc_scores())
        elif self.show_status:
            print(player.symbol, "can't move.")

    def calc_winner(self):
        # scores = self.board.calc_scores()
        # if scores[self.player1.symbol] > scores[self.player2.symbol]:
        #     return self.player1.symbol
        # if scores[self.player1.symbol] < scores[self.player2.symbol]:
        #     return self.player2.symbol
        # else:
        #     return "TIE"
        winner = self.board.check_win()
        if winner == 1:
            return "X"
        elif winner == 0:
            return "O"
        else:
            return "TIE"


    def get_decision_times(self):
        return self.decision_times

def print_scores(score_map):
    for symbol in score_map:
        print(symbol, ":", score_map[symbol], end="\t")
    print()


def compare_players(player1, player2):
    game_count_map = {player1.symbol: 0, player2.symbol: 0, "TIE": 0}
    time_elapsed_map = {player1.symbol: 0, player2.symbol: 0}
    for i in range(1, 11):
        if i % 100 == 0:
            print(i, "games finished")

        # swap who goes first
        if i % 2 == 0:
            game = Connect4Game(player1, player2, show_status=False)
        else:
            game = Connect4Game(player2, player1, show_status=False)

        game_count_map[game.calc_winner()] += 1
        decision_times = game.get_decision_times()
        for symbol in decision_times:
            time_elapsed_map[symbol] += decision_times[symbol]
    print(game_count_map)
    print(time_elapsed_map)