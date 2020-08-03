class OthelloLogic:

    # Public
    WHITE = 'O'
    BLACK = 'X'
    EMPTY = '.'

    def __init__(self, OthelloGUI, Player1, Player2, out=True):
        # code                                                      # attributes:
        self.out = out                                              # allow console output: bool
        self.GUI = OthelloGUI                                       # GUI reference       : gui object
        self.black = Player1                                        # Player 1 reference  : player object
        self.white = Player2                                        # Player 2 reference  : player object
        self.board = [['.' for j in range(8)] for i in range(8)]    # board               : [ [ str ] ]
        for i in range(3,5):
            for j in range(3,5):
                self.board[i][j] = 'X' if i == j else 'O'
        self.moveCtr = 1                                            # Move Counter        : int
        self.turn = self.BLACK                                      # whose turn          : str
        self.valids = self.availablePositions(self.board)           # GUI move suggestion : [(int,int)]

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

    #############################################
    # Basic Operations ##########################
    #############################################

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

    #############################################
    # Othello Core Logic ########################
    #############################################

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

        while True:
            # check if there is any available move
            for (r, c) in self.allCell():
                if self.toFlip(r, c, self.turn):
                    break
            else:
                # there is no available move for this player, ask for input from the other player
                self.turn = self.opponent(self.turn)
                self.valids = self.availablePositions(self.board)  # update move suggestion
                self.GUI.update()
                continue


            # get the action from the right player (r, c)
            action = None
            if self.turn == self.BLACK:
                action = self.black.getAction(self.board)
            elif self.turn == self.WHITE:
                action = self.white.getAction(self.board)

            # check if valid
            toFlip = self.toFlip(*action, self.turn)
            if len(toFlip) == 0:  # invalid input
                continue

            if self.out:  # action console output
                print(f"MOVE #{self.moveCtr:<3}, ACTION", self.turn, "AT", action)
            self.moveCtr += 1

            for (r,c) in self.toFlip(*action, self.turn):
                self.set(r, c, self.turn)
            self.set(*action, self.turn)
            self.turn = self.opponent(self.turn)
            self.valids = self.availablePositions(self.board)  # update move suggestion
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

    def availablePositions(self, board) -> [(int, int)]:
        res = []
        for i in range(8):
            for j in range(8):
                if len(self.toFlip(i, j, self.turn)) > 0:
                    res.append((i, j))
        return res

    def run(self):
        win = self.checkWin()
        while win is False:
            self.getMove()
            win = self.checkWin()
            # if self.out: print(self) # ASCII Board out
        return win
