from OthelloGUI import OthelloGUI
from AI.ManualAI import ManualAI
from AI.RandomAI import RandomAI
from AI.OthelloAI import OthelloAI

BLACK = 'X'
WHITE = 'O'

# Specify what kind of game to play

# player1 = ManualAI(BLACK, "steven")
player1 = RandomAI(BLACK)
player2 = RandomAI(WHITE)
game = OthelloGUI(player1, player2, delay=0, destroyWhenOver=False)
print(game.result())