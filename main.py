# GUI
from GameComponents import OthelloGUI

# Color
BLACK = 'X'
WHITE = 'O'

# import your AI
from AI.RandomAI import RandomAI            # Random Move
from AI.AlphaBeta import AlphaBeta

# print("===== main.py =====")
for i in range(10):
    player1 = RandomAI(BLACK)
    player2 = AlphaBeta(WHITE)

    # play game
    game = OthelloGUI(player1, player2, delay=0, destroyWhenOver=True, logicout=False)
    game.start()

    # print match result
    result = game.result()

    # print result in a nicer way
    resstr = None
    if result[0] == result[1]:resstr = "DRAW"
    elif result[0] <= result[1]:resstr = "WHITE"
    else:resstr = "BLACK"
    print("Game Result", result, resstr)
print("=== main.py DONE ==")
