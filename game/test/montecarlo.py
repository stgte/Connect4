import copy
import time
import random
from game.test.Node import Node


class MCTPlayer:
    def __init__(self, symbol):
        self.symbol = symbol

    def get_move(self, state, currentNode):
        node, col = MCTS(state, 10000, currentNode, timeout=2)
        return node, col


def MCTS(currentState, itermax, currentNode=None, timeout=100):
    rootnode = Node(state=currentState)
    if currentNode is not None: rootnode = currentNode

    #    print(rootnode.wins, rootnode.visits)
    #    for child in rootnode.childNodes:
    #        print(child.move, child.wins, child.visits)

    start = time.clock()
    for i in range(itermax):
        node = rootnode
        state = currentState.Clone()

        # selection
        # keep going down the tree based on best UCT values until terminal or unexpanded node
        while node.untriedMoves == [] and node.childNodes != []:
            node = node.selection()
            state.insert(node.move)

        # expand
        if node.untriedMoves != []:
            m = random.choice(node.untriedMoves)
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

    foo = lambda x: x.wins / x.visits
    sortedChildNodes = sorted(rootnode.childNodes, key=foo)[::-1]
    # print("AI\'s computed winning percentages")
    # for node in sortedChildNodes:
    #     print('Move: %s    Win Rate: %.2f%%' % (node.move , 100 * node.wins / node.visits))
    # print('Simulations performed: %s\n' % i)
    return rootnode, sortedChildNodes[0].move