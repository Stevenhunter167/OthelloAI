from AI.Base import OthelloBaseAI
from AI.Base import State
from .MonteCarloSearchTree import MCTreeNode, MonteCarloSearchTree

import time

class MCTS(OthelloBaseAI):

    class TreeNode(MCTreeNode):

        def __init__(self, state, color, parent=None, children=None):
            super().__init__(parent, children, state)
            self.color = color

        def evaluate(self):
            """ evaluation function """
            blackcnt, whitecnt = self.state.count()
            result = blackcnt - whitecnt if self.color == 'X' else whitecnt - blackcnt

            if result > 0:    return 1
            elif result == 0: return 0
            else:             return -1

        def __str__(self):
            return super().__str__()

        def __eq__(self, other):
            return self.state.board == other.state.board \
                   and self.state.color == other.state.color

        def getChildren(self):
            result = []
            for action in self.state.actionSet():
                child = self.state.makeMove(*action)
                node = MCTS.TreeNode(child, self.color, parent=self, children=None)
                result.append(node)
            return result

        def expand(self) -> list:
            self.children = self.getChildren()

        def isTerminal(self):
            return self.state.isTerminal()

    def __init__(self, color, thinkTime=2.5):
        self.color = color
        self.searchTree = MonteCarloSearchTree()
        self.thinkTime = thinkTime

    def getAction(self, board) -> (int, int):
        startTime = time.time()
        currentState = State(self.color, board)

        # initialize serach tree
        self.searchTree.setRoot(self.TreeNode(currentState, self.color))

        # search until there is no time left
        while time.time() - startTime < self.thinkTime:
            self.searchTree.iterate()

        # return the best move found
        bestNextState = self.searchTree.getResult()
        for action in currentState.actionSet():
            childState = currentState.makeMove(*action)
            if childState.board == bestNextState.board:
                return action

        raise Exception("No action is found")