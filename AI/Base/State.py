from AI.Base.OthelloBaseAI import OthelloBaseAI

class State(OthelloBaseAI):

    """ Represents the current state of board """

    def __init__(self, color, board):
        """
        initialize State
        """
        self.color = color  # whose turn is this
        self.board = board
        self.validMoves = self.availablePositions(board)

    def __str__(self):
        res = "====== State ======\n"
        res += "# "
        for i in range(8):
            res += str(i) + " "
        res += "#\n"
        for i in range(8):
            res += str(i) + " "
            for j in range(8):
                res += self.board[i][j] + " "
            res += str(i) + "\n"
        res += "# "
        for i in range(8):
            res += str(i) + " "
        res += "#\n==================="
        return res

    def get(self, r, c):
        return self.board[r][c]

    def set(self, r, c, color):
        self.board[r][c] = color

    @staticmethod
    def copy(board) -> "board":
        """ helper: make a deep copy of the board """
        res = list()
        for row in board:
            res.append(row.copy())
        return res

    def actionSet(self) -> [(int,int)]:
        """ returns a list of performable actions """
        return self.availablePositions(self.board)

    def isTerminal(self):
        """ this state is a terminal state, end of game """
        for state in [State(self.opponentColor(), self.copy(self.board)), self]:
            for (r, c) in self.allCell():
                if len(self.toFlip(self.board, r, c)) != 0:
                    return False
        else:
            countP1 = [self.get(r, c) for r, c in self.allCell()].count(self.BLACK)
            countP2 = [self.get(r, c) for r, c in self.allCell()].count(self.WHITE)
            return countP1, countP2

    def count(self) -> ("black", "white"):
        """ count the stones, returns (black:int, white:int) """
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
        resultBoard[r][c] = self.color
        return State(self.opponentColor(), resultBoard)
