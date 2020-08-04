from math import log, sqrt
import random

class MCTreeNode:

    """ a base class for MCTS node """

    def __init__(self, parent=None, children=None, data=None):
        self.data = data
        self.parent = parent
        self.children = children
        self.vi = 0
        self.ni = 0

    def getChildren(self) -> list:
        """ TODO: implement this method in your derived class """
        return list()

    def expand(self) -> list:
        self.children = self.getChildren()

    def isTerminal(self):
        """ TODO: implement this method in your derived class """
        return True

class MonteCarloSearchTree:

    """ the search tree data structure and methods for MCTS """

    def __init__(self, root, balanceFactor=2):
        self.root = root                    # root node
        self.balanceFactor = balanceFactor  # value of c

    def UCB1(self, treenode):

        """ classic UCB1 formula, optional to reimplement your own formula for calculating UCB1 """

        exploitation = treenode.vi / treenode.ni                    # exploitation term
        exploration = sqrt(log(treenode.parent.ni) / treenode.ni)   # exploration term
        return exploitation + self.balanceFactor * exploration      # calculate UCB1 value

    def select(self) -> MCTreeNode:
        current = self.root
        while not self.isLeaf(current):
            maxUCB1 = float('-inf')
            nextNode = None
            for child in current.children:
                childUCB1 = self.UCB1(child)
                if childUCB1 > maxUCB1:
                    maxUCB1 = childUCB1
                    nextNode = child
            current = nextNode
        return current

    def expand(self, treenode: MCTreeNode):
        """ expand the selected node """
        treenode.expand()

    def simulate(self, treenode: MCTreeNode) -> MCTreeNode:
        """ returns the result of simulation """
        while not treenode.isTerminal():
            children = treenode.getChildren()
            treenode = random.choice(children)
        return treenode

    def update(self, treenode: MCTreeNode, simulationResult: float):
        current = treenode
        while current is not None:
            current.ni += 1
            current.vi += simulationResult
            current = current.parent

    def isLeaf(self, treenode):
        return treenode.children is None

    def isTerminal(self, treenode):
        """ implement this method in your derived class """
        return treenode.isTerminal()

    def iterate(self):
        """ execute 1 iteration of monte carlo tree search """
        target = self.select()
        if target.ni != 0:
            self.expand(target)
            target = next(iter(target.children))
        result = self.simulate(target)
        self.update(target, result.vi)

    def getResult(self):
        maxUCB1 = float('-inf')
        nextNode = None
        for child in self.root.children:
            childUCB1 = self.UCB1(child)
            if childUCB1 > maxUCB1:
                maxUCB1 = childUCB1
                nextNode = child
        return nextNode

    ######################################################
    # Output #############################################
    ######################################################

    # TODO
