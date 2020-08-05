from AI.Base import OthelloBaseAI
from AI.Base import State
from .MonteCarloSearchTree import MCTreeNode, MonteCarloSearchTree

import time

class MCTS(OthelloBaseAI):

    class TreeNode(MCTreeNode):

        def __init__(self, state, parent=None, children=None):
            super().__init__(parent, children, state)

        def evaluate(self):
            """ evaluation function """
            return 0.0

        def __eq__(self, other):
            return self.state.board == other.state.board \
                   and self.state.color == other.state.color

        def getChildren(self):
            result = []
            for action in self.state.actionSet():
                child = self.state.makeMove(*action)
                node = MCTS.TreeNode(child, parent=self, children=None)
                result.append(node)
            return result

        def isTerminal(self):
            return self.state.isTerminal()

    def __init__(self, color, thinkTime=10):
        self.color = color
        self.searchTree = MonteCarloSearchTree()
        self.thinkTime = thinkTime

    def getAction(self, board) -> (int, int):
        startTime = time.time()
        currentState = State(self.color, board)

        # initialize serach tree
        self.searchTree.setRoot(MCTS.TreeNode(currentState))

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