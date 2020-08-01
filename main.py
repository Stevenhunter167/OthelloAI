# GUI
from OthelloGUI import OthelloGUIv2

# import your AI
from AI.ManualAI import ManualAI
from AI.RandomAI import RandomAI
from AI.OthelloAI import OthelloAI
from AI.StevenAI import StevenAI
from AI.AlphaBeta import AlphaBeta

# Color
BLACK = 'X'
WHITE = 'O'

# Specify what kind of game to play (Black First)
print("===== main.py =====")
for i in range(10):

    # player1 = RandomAI(BLACK)
    # player1 = ManualAI(BLACK, "steven")
    player1 = AlphaBeta(BLACK)
    player2 = RandomAI(WHITE)

    game = OthelloGUIv2(player1, player2, delay=0, destroyWhenOver=True, logicout=False)
    game.start()
    # print match result
    result = game.result()
    resstr = None
    if result[0] == result[1]:resstr = "DRAW"
    elif result[0] <= result[1]:resstr = "WHITE"
    else:resstr = "BLACK"
    print("Game Result", result, resstr)
input()
print("=== main.py DONE ==")
