import random
import copy
from math import inf

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

class MinimaxPlayer:

    def __init__(self, symbol):
        self.symbol = symbol

    def get_move(self, board):
        if len(board.getValidMoves()) == 1:
            return board.getValidMoves()[0]
        answer = minimax(board, 2, self.symbol, True)
        return answer[0]


def minimax(board, depth, symbol, max):
    if max:
        best = [-1, -inf]
    else:
        best = [-1, inf]

    if (not board.stillGoing()):
        return [-1, heuristic(board)]

    elif depth == 0 or len(board.getValidMoves()) == 0:
        return [-1, heuristic(board)]

    for move in board.getValidMoves():
        baseBoard = copy.deepcopy(board)
        baseBoard.insert(move, symbol)
        score = minimax(baseBoard, depth - 1, flipSymbol(symbol), not max)
        score[0] = move

        if max:
            if score[1] > best[1]:
                best = score

        else:
            if score[1] < best[1]:
                best = score

    return best

def heuristic(board):
    heur = 0
    state = board.board
    print(state)
    for i in range(0, board.rows):
        for j in range(0, board.cols):
            # check horizontal streaks
            try:
                # add player one streak scores to heur
                if state[i][j] == state[i + 1][j] == 0:
                    heur += 10
                if state[i][j] == state[i + 1][j] == state[i + 2][j] == 0:
                    heur += 100
                if state[i][j] == state[i + 1][j] == state[i + 2][j] == state[i + 3][j] == 0:
                    heur += 10000

                # subtract player two streak score to heur
                if state[i][j] == state[i + 1][j] == 1:
                    heur -= 10
                if state[i][j] == state[i + 1][j] == state[i + 2][j] == 1:
                    heur -= 100
                if state[i][j] == state[i + 1][j] == state[i + 2][j] == state[i + 3][j] == 1:
                    heur -= 10000
            except IndexError:
                pass

            # check vertical streaks
            try:
                # add player one vertical streaks to heur
                if state[i][j] == state[i][j + 1] == 0:
                    heur += 10
                if state[i][j] == state[i][j + 1] == state[i][j + 2] == 0:
                    heur += 100
                if state[i][j] == state[i][j + 1] == state[i][j + 2] == state[i][j + 3] == 0:
                    heur += 10000

                # subtract player two streaks from heur
                if state[i][j] == state[i][j + 1] == 1:
                    heur -= 10
                if state[i][j] == state[i][j + 1] == state[i][j + 2] == 1:
                    heur -= 100
                if state[i][j] == state[i][j + 1] == state[i][j + 2] == state[i][j + 3] == 1:
                    heur -= 10000
            except IndexError:
                pass

            # check positive diagonal streaks
            try:
                # add player one streaks to heur
                if not j + 3 > board.cols and state[i][j] == state[i + 1][j + 1] == 0:
                    heur += 100
                if not j + 3 > board.cols and state[i][j] == state[i + 1][j + 1] == state[i + 2][j + 2] == 0:
                    heur += 100
                if not j + 3 > board.cols and state[i][j] == state[i + 1][j + 1] == state[i + 2][j + 2] \
                        == state[i + 3][j + 3] == 0:
                    heur += 10000

                # add player two streaks to heur
                if not j + 3 > board.cols and state[i][j] == state[i + 1][j + 1] == 1:
                    heur -= 100
                if not j + 3 > board.cols and state[i][j] == state[i + 1][j + 1] == state[i + 2][j + 2] == 1:
                    heur -= 100
                if not j + 3 > board.cols and state[i][j] == state[i + 1][j + 1] == state[i + 2][j + 2] \
                        == state[i + 3][j + 3] == 1:
                    heur -= 10000
            except IndexError:
                pass

            # check negative diagonal streaks
            try:
                # add  player one streaks
                if not j - 3 < 0 and state[i][j] == state[i + 1][j - 1] == 0:
                    heur += 10
                if not j - 3 < 0 and state[i][j] == state[i + 1][j - 1] == state[i + 2][j - 2] == 0:
                    heur += 100
                if not j - 3 < 0 and state[i][j] == state[i + 1][j - 1] == state[i + 2][j - 2] \
                        == state[i + 3][j - 3] == 0:
                    heur += 10000

                # subtract player two streaks
                if not j - 3 < 0 and state[i][j] == state[i + 1][j - 1] == 1:
                    heur -= 10
                if not j - 3 < 0 and state[i][j] == state[i + 1][j - 1] == state[i + 2][j - 2] == 1:
                    heur -= 100
                if not j - 3 < 0 and state[i][j] == state[i + 1][j - 1] == state[i + 2][j - 2] \
                        == state[i + 3][j - 3] == 1:
                    heur -= 10000
            except IndexError:
                pass
    return heur


class AlphaBetaPlayer:
    def __init__(self, symbol):
        self.symbol = symbol

    def get_move(self, board):
        if len(board.getValidMoves()) == 1:
            return board.getValidMoves()[0]
        answer = AlphaBeta(board, 4, self.symbol)
        # print(answer)
        return answer[0]


def AlphaBeta(board, depth, symbol):
    def max_value(board, alpha, beta, symbol, depth):
        if not board.stillGoing():
            return [-1, heuristic(board)]

        elif depth == 0 or len(board.getValidMoves()) == 0:
            return [-1, -1, heuristic(board)]
        best = [-1, -inf]


        for move in board.getValidMoves():
            copied_board = copy.deepcopy(board)
            copied_board.insert( move, symbol)
            score = min_value(copied_board, alpha, beta, flipSymbol(symbol), depth - 1)
            if best[1] < score[1]:
                best[1] = score[1]
                best[0] = move
            if best[1] >= beta:
                return best
            alpha = max(alpha, best[1])
        return best

    def min_value(board, alpha, beta, symbol, depth):
        if not board.stillGoing():
            return [-1, -1,heuristic(board)]
        elif depth == 0 or len(board.getValidMoves()) == 0:
            return [-1, -1, heuristic(board)]

        best = [-1, -1, inf]

        for move in board.getValidMoves():
            copied_board = copy.deepcopy(board)
            copied_board.insert(move, symbol)
            score = max_value(copied_board, alpha, beta, flipSymbol(symbol), depth - 1)
            if best[1] > score[1]:
                best[1] = score[1]
                best[0] = move
            if best[1] <= alpha:
                return best
            beta = min(beta, best[1])
        return best

    return max_value(board, -inf, inf, symbol, depth)



def flipSymbol(symbol):
    if symbol == 'R':
        return 'Y'
    else:
        return 'R'