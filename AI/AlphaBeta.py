from AI.Base import OthelloBaseAI
from AI.Base import State

class AlphaBeta(OthelloBaseAI):


    def __init__(self, color):
        self.color = color

    def getAction(self, board) -> (int,int):
        value, action = self.alphaBetaSearch(State(self.color, board), 7, float('-inf'), float('+inf'), True)
        return action

    def corner(self, state):
        res = 0
        for location in [(0, 0), (0, 7), (7, 0), (7, 7)]:
            if state.get(*location) == self.color:
                res += 1
            elif state.get(*location) == self.opponentColor():
                res -= 1
        return res

    def evaluation(self, state):
        corner = self.corner(state)
        difference = 0

        if corner == 0:
            c = state.count()
            if self.color == self.BLACK:
                difference = c[0] - c[1]
            elif self.color == self.WHITE:
                difference = c[1] - c[0]

        return corner * 100 + difference

    def alphaBetaSearch(self, state, depth, alpha, beta, isMaximize) -> (int, (int, int)):

        """ classic alpha-beta pruning, returns value, action pair"""

        if depth == 0 or state.isTerminal():
            return self.evaluation(state), None
        if isMaximize:
            value = float('-inf')
            bestAction = None
            for action in state.actionSet():
                nextState = state.makeMove(*action)
                valueOfNextState, _ = self.alphaBetaSearch(nextState, depth - 1, alpha, beta, False)
                if value < valueOfNextState:
                    value = valueOfNextState
                    bestAction = action
                alpha = max(alpha, value)
                if alpha >= beta:
                    break  # Beta cutoff
            return value, bestAction
        else:
            value = float('+inf')
            for action in state.actionSet():
                nextState = state.makeMove(*action)
                valueOfNextState, _ = self.alphaBetaSearch(nextState, depth - 1, alpha, beta, True)
                if value > valueOfNextState:
                    value = valueOfNextState
                beta = min(beta, value)
                if alpha >= beta:
                    break  # Alpha cutoff
            return value, None
