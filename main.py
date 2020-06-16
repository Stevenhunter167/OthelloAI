from OthelloGUI import OthelloGUI
from AI.ManualAI import ManualAI
from AI.RandomAI import RandomAI
from AI.OthelloAI import OthelloAI

BLACK = 'X'
WHITE = 'O'

# Specify what kind of game to play

player1 = ManualAI(BLACK, "steven")
player2 = RandomAI(WHITE)
OthelloGUI(player1, player2)