from AI.Base import OthelloBaseAI

class mcts(OthelloBaseAI):

    def __init__(self, color):
        self.color = color

    def getAction(self, board) -> (int, int):
        pass