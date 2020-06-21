from AI.Base.OthelloBaseAI import OthelloBaseAI


class State(OthelloBaseAI):

    """ Represents the current state of board """

    def __init__(self, color, board):
        """
        initialize State
        :param
        evaluateFunc: evaluateFunc(board) -> float
        """
        self.color = color
        self.board = board
        self.validMoves = self.availablePositions(board)

    @staticmethod
    def copy(board) -> "board":
        """ helper: make a deep copy of the board """
        res = list()
        for row in board:
            res.append(row.copy())
        return res

    def isTerminal(self):
        # oppoState = State(self.opponentColor(), self.board, self.evaluateFunction)
        # if len(self.validMoves) == 0 and len(oppoState.validMoves) == 0:
        for color in [self.BLACK, self.WHITE]:
            for (r, c) in self.allCell():
                if len(self.toFlip(self.board, r, c)) != 0:
                    return False
        else:
            countP1 = [self.get(r, c) for r, c in self.allCell()].count(self.BLACK)
            countP2 = [self.get(r, c) for r, c in self.allCell()].count(self.WHITE)
            return countP1, countP2

    def count(self) -> ("black", "white"):
        res = [0, 0]
        for r, c in self.allCell():
            if self.get(r, c) == 'X':
                res[0] += 1
            elif self.get(r, c) == 'O':
                res[1] += 1
        return tuple(res)

    def makeMove(self, r, c) -> "State":
        """ returns the state after this move """
        if (r, c) not in self.validMoves:
            raise Exception(f"invalid move {(r, c)}")
        resultBoard = self.copy(self.board)
        for tr, tc in self.toFlip(resultBoard, r, c):
            resultBoard[tr][tc] = self.color
        return State(self.opponentColor(), resultBoard)
