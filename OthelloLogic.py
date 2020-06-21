class OthelloLogic:

    # Public
    WHITE = 'O'
    BLACK = 'X'
    EMPTY = '.'

    def __init__(self, OthelloGUI, Player1, Player2, out=True):
        self.out = out
        self.GUI = OthelloGUI
        self.black = Player1
        self.white = Player2
        self.board = [['.' for j in range(8)] for i in range(8)]
        for i in range(3,5):
            for j in range(3,5):
                self.board[i][j] = 'X' if i == j else 'O'
        self.moveCtr = 0
        self.turn = self.BLACK

    def __str__(self):
        res = "== Othello Logic ==\n"
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

    def inBound(self, r, c):
        return 0 <= r < 8 and 0 <= c < 8

    def opponent(self, color):
        if color == self.BLACK:
            return self.WHITE
        elif color == self.WHITE:
            return self.BLACK
        raise Exception()

    def get(self, r, c):
        return self.board[r][c]

    def set(self, r, c, color):
        self.board[r][c] = color

    def allCell(self):
        for i in range(8):
            for j in range(8):
                yield i, j

    def checkWin(self) -> ("BLACK", "WHITE"):
        for color in [self.BLACK, self.WHITE]:
            for (r, c) in self.allCell():
                if len(self.toFlip(r, c, color)) != 0:
                    return False
        else:
            countP1 = [self.get(r, c) for r, c in self.allCell()].count(self.BLACK)
            countP2 = [self.get(r, c) for r, c in self.allCell()].count(self.WHITE)
            return countP1, countP2

    def getMove(self) -> (int, int):

        # check if there is any available move
        for (r, c) in self.allCell():
            if self.toFlip(r, c, self.turn):
                break
        else:
            # there is no available move for this player, ask for input from the other player
            self.turn = self.opponent(self.turn)
            return self.getMove()


        # get the action from the right player (r, c)
        action = None
        if self.turn == self.BLACK:
            action = self.black.getAction(self.board)
        elif self.turn == self.WHITE:
            action = self.white.getAction(self.board)

        # check if valid
        toFlip = self.toFlip(*action, self.turn)
        if len(toFlip) == 0:
            # invalid input
            return self.getMove()

        for (r,c) in self.toFlip(*action, self.turn):
            self.set(r, c, self.turn)
        self.set(*action, self.turn)
        self.turn = self.opponent(self.turn)
        self.GUI.update()
        return action

    def toFlip(self, r, c, thisColor) -> [(int,int)]:
        """ toFlip(a location to place, this color) -> [coordinates to flip] #empty means invalid move """
        res = []
        if self.get(r, c) != self.EMPTY:
            return res
        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(1,1),(-1,1),(1,-1)]:
            opponentColor = self.opponent(thisColor)
            row = r + dr
            col = c + dc
            currentDirection = []
            if not self.inBound(row, col):
                continue
            if self.get(row, col) != opponentColor:
                continue
            while self.inBound(row, col):
                if self.get(row, col) == opponentColor:
                    currentDirection.append((row, col))
                elif self.get(row, col) == self.EMPTY:
                    currentDirection.clear()
                    break
                elif self.get(row, col) == thisColor:
                    break
                row += dr
                col += dc
            else:
                currentDirection.clear()
            res.extend(currentDirection)
        return res

    def run(self):
        win = self.checkWin()
        while win is False:
            self.getMove()
            win = self.checkWin()
            if self.out:
                print(self)
        return win
