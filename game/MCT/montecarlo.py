import copy
import time
import random
from game.MCT.Node import Node


class MCTPlayer:
    def __init__(self, symbol):
        self.symbol = symbol

    def get_move(self, state, currentNode):
        node, col = MCTS(state, 10000, currentNode, timeout=2)
        return node, col


def MCTS(currentState, itermax, currentNode=None, timeout=100):
    root = Node(state=currentState)
    
    if currentNode is not None: root = currentNode

    start = time.clock()
    for i in range(itermax):
        node = root
        state = currentState.Clone()

        # selection
        # keep going down the tree based on best UCT values until terminal or unexpanded node
        while node.untried == [] and node.children != []:
            node = node.selection()
            state.insert(node.move)

        # expand
        if node.untried != []:
            m = random.choice(node.untried)
            state.insert(m)
            node = node.expand(m, state)

        # rollout
        while state.getValidMoves():
            state.insert(random.choice(state.getValidMoves()))

        # backpropagate
        while node is not None:
            node.update(state.result(node.player))
            node = node.parent

        duration = time.clock() - start
        if duration > timeout: break

    score = lambda x: x.wins / x.visits
    sortedChildNodes = sorted(root.children, key=score)[::-1]
    # print("AI\'s computed winning percentages")
    # for node in sortedChildNodes:
    #     print('Move: %s    Win Rate: %.2f%%' % (node.move , 100 * node.wins / node.visits))
    # print('Simulations performed: %s\n' % i)
    return root, sortedChildNodes[0].move