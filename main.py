# GUI
from OthelloGUI import OthelloGUI

# import your AI
from AI.ManualAI import ManualAI
from AI.RandomAI import RandomAI
from AI.OthelloAI import OthelloAI

# Color
BLACK = 'X'
WHITE = 'O'

# Specify what kind of game to play (Black First)
# player1 = ManualAI(BLACK, "steven")
player1 = RandomAI(BLACK)
player2 = RandomAI(WHITE)
game = OthelloGUI(player1, player2, delay=0.1, destroyWhenOver=False)
print("Game Result", game.result())