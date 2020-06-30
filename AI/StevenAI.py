from AI.Base.OthelloBaseAI import OthelloBaseAI
from AI.Base.State import State


class StevenAI(OthelloBaseAI):

    def __init__(self, color):
        self.color = color

    def evaluate(self, state: State) -> float:
        c = state.count()
        difference = 0
        if self.color == self.BLACK:
            difference = c[0] - c[1]
        elif self.color == self.WHITE:
            difference = c[1] - c[0]

        return difference \
               + self.corner(state) * 64 \
               + 2 * (len(state.validMoves) * 1 if state.color == self.color else -1) # + 2 * self.side(state)

    def corner(self, state):
        res = 0
        for location in [(0, 0), (0, 7), (7, 0), (7, 7)]:
            if state.get(*location) == self.color:
                res += 1
            elif state.get(*location) == self.opponentColor():
                res -= 1
        return res

    def side(self, state):
        res = 0
        for r, c in self.allCell():
            if (r == 0 or c == 0) or (r == 7 or c == 7):
                if state.get(r, c) == self.color:
                    res += 1
                elif state.get(r, c) == self.opponentColor():
                    res -= 1
        return res


    def heuristicMinimax(self, currentState: State, depth, isMyTurn, policy: int):
        if depth == 0 or currentState.isTerminal():
            return self.evaluate(currentState), None

        # find every valid child node, evaluate its value
        allChildren = []
        for r, c in currentState.validMoves:
            thisChild = currentState.makeMove(r, c)
            allChildren.append((thisChild, self.evaluate(thisChild), (r, c)))

        if isMyTurn:
            allChildren.sort(key=lambda t: t[1], reverse=True)  # decreasing order

            i = 0
            maxEvaluation = float("-inf")  # initialize max to -infinity
            bestAction = None
            for child, value, action in allChildren:
                if i >= policy:
                    break
                evaluation, _ = self.heuristicMinimax(child, depth - 1, False, policy)
                if evaluation > maxEvaluation:
                    maxEvaluation = evaluation
                    bestAction = action

            return maxEvaluation, bestAction

        else:
            allChildren.sort(key=lambda t: t[1], reverse=False)  # increasing order

            i = 0
            minEvaluation = float("+inf")
            bestAction = None
            for child, value, action in allChildren:
                if i >= policy:
                    break
                evaluation, _ = self.heuristicMinimax(child, depth - 1, True, policy)
                if evaluation < minEvaluation:
                    minEvaluation = evaluation
                    bestAction = action

            return minEvaluation, bestAction

    def getAction(self, board):
        currentState = State(self.color, board)
        # evaluate the best value, action pair given the current state
        value, action = self.heuristicMinimax(currentState, depth=3, isMyTurn=True, policy=20)
        # print(State(self.color, board))
        # print("value:", value)
        return action
