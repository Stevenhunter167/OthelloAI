from math import log, sqrt
import random

class MCTreeNode:

    """ a base class for MCTS node """

    def __init__(self, parent=None, children=None, state=None):
        self.state = state
        self.parent = parent
        self.children = children
        self.vi = 0
        self.ni = 0

    def __str__(self):
        return f"{{n={self.ni},v={self.vi}}}"

    def __eq__(self, other):
        """ TODO: implement this method in your derived class """
        return False

    def evaluate(self):
        """ TODO: implement this method in your derived class """
        return 0.0

    def getChildren(self) -> list:
        """ TODO: implement this method in your derived class """
        return list()

    def isTerminal(self):
        """ TODO: implement this method in your derived class """
        return True

    def expand(self) -> list:
        self.children = self.getChildren()


class MonteCarloSearchTree:

    """ the search tree data structure and methods for MCTS """

    def __init__(self, balanceFactor=2):
        self.root = None
        self.balanceFactor = balanceFactor  # value of c
        self.debug = {}

    def setRoot(self, treenode):
        self.root = treenode
        self.debug['node_explored'] = 0

        # if self.root is None:
        #     self.root = treenode
        #     return  # no root before
        # frontier = [self.root]
        # while len(frontier) > 0:
        #     node = frontier.pop(0)
        #     if self.isLeaf(node):
        #         continue
        #     if node == treenode:
        #         self.root = node
        #         return True  # found node in subtree, setting it as root
        #     frontier.extend(node.children)
        # self.root = treenode
        # return False  # not found

    def UCB1(self, treenode):
        """ classic UCB1 formula, optional to reimplement your own formula for calculating UCB1 """
        if treenode.ni == 0:
            return float('+inf')
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
        self.debug['node_explored'] += 1

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
        if target.isTerminal():
            self.update(target, target.evaluate())  # already at bottom of tree
            return
        if target.ni != 0:
            self.expand(target)
            target = next(iter(target.children))
        result = self.simulate(target)
        self.update(target, result.evaluate())

    def getResult(self) -> "State":
        maxUCB1 = float('-inf')
        nextNode = None
        for child in self.root.children:
            childUCB1 = self.UCB1(child)
            if childUCB1 > maxUCB1:
                maxUCB1 = childUCB1
                nextNode = child
        return nextNode.state

    ######################################################
    # Output #############################################
    ######################################################

    def DFS(self, treenode, f=(lambda s: print([str(n) for n in s])), stack=[]):
        if self.isLeaf(treenode):
            stack.append(treenode)
            f(stack)
            stack.pop(-1)
            return
        for subtree in treenode.children:
            stack.append(subtree)
            self.DFS(subtree)
            stack.pop(-1)

    def consoleOut(self):
        self.DFS(self.root)

    def serialize(self):
        pass