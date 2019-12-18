import numpy as np


class Node:
    def __init__(self, move=None, parent=None, state=None):
        self.state = state.Clone()
        self.parent = parent
        self.move = move
        self.untried = state.getValidMoves()
        self.children = []
        self.wins = 0
        self.visits = 0
        self.player = state.player

    def selection(self):
        # select largest score value
        score = lambda x: x.wins /x.visits + np.sqrt( 2 *np.log(self.visits ) /x.visits)
        return sorted(self.children, key=score)[-1]

    def expand(self, move, state):
        # return child when move is taken
        # remove move from current node
        child = Node(move=move, parent=self, state=state)
        self.untried.remove(move)
        self.children.append(child)
        return child

    def update(self, result):
        self.wins += result
        self.visits += 1