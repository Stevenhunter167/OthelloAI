from AI.Base import OthelloBaseAI
from AI.Base import State
from .MonteCarloSearchTree import MCTreeNode, MonteCarloSearchTree

class MCTS(OthelloBaseAI):

    class TreeNode(MCTreeNode):

        def __init__(self, state, parent=None, children=None):
            super().__init__(parent, children, state)

        def evaluate(self):
            """ evaluation function """
            return 0.0

        def getChildren(self):
            result = []
            for action in self.state.actionSet():
                child = self.state.makeMove(action)
                node = MCTS.TreeNode(child, parent=self, children=None)
                result.append(node)
            return result

        def isTerminal(self):
            return self.state.isTerminal()

    def __init__(self, color):
        self.color = color

    def getAction(self, board) -> (int, int):
        pass