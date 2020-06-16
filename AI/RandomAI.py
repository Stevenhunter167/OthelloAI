import random

class RandomAI:

    def __init__(self, color):
        self.color = color

    def inBound(self, r, c):
        return 0 <= r < 8 and 0 <= c < 8

    def toFlip(self, board, r, c):
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

    def allValid(self, board):
        res = []
        for i in range(8):
            for j in range(8):
                if len(self.toFlip(board, i, j)) > 0:
                    res.append((i, j))
        return res

    def getAction(self, board) -> (int, int):
        return random.choice(self.allValid(board))