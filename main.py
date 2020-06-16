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
for i in range(10):
    player1 = RandomAI(BLACK)
    player2 = RandomAI(WHITE)
    game = OthelloGUI(player1, player2, delay=0, destroyWhenOver=True, logicout=False)

    result = game.result()
    resstr = None
    if result[0] == result[1]:resstr = "DRAW"
    elif result[0] <= result[1]:resstr = "WHITE"
    else:resstr = "BLACK"
    print("Game Result", result, resstr, "WIN")