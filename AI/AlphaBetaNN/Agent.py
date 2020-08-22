from AI.Base import OthelloBaseAI
from AI.Base import State

class AlphaBetaNN(OthelloBaseAI):

    def __init__(self, color):
        self.color = color

    def getAction(self, board) -> (int,int):
        value, action = self.alphaBetaSearch(State(self.color, board), 5, float('-inf'), float('+inf'), True)
        return action

    def evaluation(self, state: State):
        return 0.0

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
