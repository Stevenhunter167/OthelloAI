# GUI
from History.OthelloGUI import OthelloGUI

# import your AI
from AI.ManualAI import ManualAI
from AI.RandomAI import RandomAI

# Color
BLACK = 'X'
WHITE = 'O'

# Specify what kind of game to play (Black First)
print("===== main.py =====")
for i in range(5):
    player1 = ManualAI(BLACK, "steven")
    # player1 = RandomAI(BLACK)
    # player1 = StevenAI(BLACK)
    player2 = RandomAI(WHITE)
    game = OthelloGUI(player1, player2, delay=0, destroyWhenOver=True, logicout=False)

    # print match result
    result = game.result()
    resstr = None
    if result[0] == result[1]:resstr = "DRAW"
    elif result[0] <= result[1]:resstr = "WHITE"
    else:resstr = "BLACK"
    print("Game Result", result, resstr, "WIN")
print("=== main.py DONE ==")
