class OthelloBaseAI:

    """ contains some util functions for AIs """

    BLACK = 'X'
    WHITE = 'O'

    def allCell(self):
        """ a generator of all cell in (row,col) coordinates """
        for i in range(8):
            for j in range(8):
                yield i, j

    def opponentColor(self):
        """ returns the color of opponent stone """
        if self.color == self.BLACK:
            return self.WHITE
        elif self.color == self.WHITE:
            return self.BLACK
        raise Exception()

    def inBound(self, r, c) -> bool:
        """ checking if a cell is valid """
        return 0 <= r < 8 and 0 <= c < 8

    def toFlip(self, board, r, c) -> [(int, int)]:
        """ the stones that will be reversed if (r,c) is pushed to the board """
        res = []
        if board[r][c] != '.':
            return res
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]:
            opponentColor = 'X' if self.color == 'O' else 'O'
            row = r + dr
            col = c + dc
            currentDirection = []
            if not self.inBound(row, col):
                continue
            if board[row][col] != opponentColor:
                continue
            while self.inBound(row, col):
                if board[row][col] == opponentColor:
                    currentDirection.append((row, col))
                elif board[row][col] == '.':
                    currentDirection.clear()
                    break
                elif board[row][col] == self.color:
                    break
                row += dr
                col += dc
            else:
                currentDirection.clear()
            res.extend(currentDirection)
        return res

    def availablePositions(self, board) -> [(int, int)]:
        """ all legal actions that the agent can perform """
        res = []
        for i in range(8):
            for j in range(8):
                if len(self.toFlip(board, i, j)) > 0:
                    res.append((i, j))
        return res






