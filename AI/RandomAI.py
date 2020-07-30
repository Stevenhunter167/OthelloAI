import random
from .Base.OthelloBaseAI import OthelloBaseAI

class RandomAI(OthelloBaseAI):

    def __init__(self, color):
        self.color = color

    def getAction(self, board) -> (int, int):
        return random.choice(self.availablePositions(board))
