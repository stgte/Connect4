import numpy as np


class Node:
    def __init__(self, move=None, parent=None, state=None):
        self.state = state.Clone()
        self.parent = parent
        self.move = move
        self.untriedMoves = state.getValidMoves()
        self.childNodes = []
        self.wins = 0
        self.visits = 0
        self.player = state.player

    def selection(self):
        # return child with largest UCT value
        foo = lambda x: x.wins /x.visits + np.sqrt( 2 *np.log(self.visits ) /x.visits)
        return sorted(self.childNodes, key=foo)[-1]

    def expand(self, move, state):
        # return child when move is taken
        # remove move from current node
        child = Node(move=move, parent=self, state=state)
        self.untriedMoves.remove(move)
        self.childNodes.append(child)
        return child

    def update(self, result):
        self.wins += result
        self.visits += 1