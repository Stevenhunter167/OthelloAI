import pygame
import threading

from .OthelloLogic import OthelloLogic

GREEN = (  0, 150,   0)
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)

class OthelloGUI:
    # os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0, 460)
    pygame.init()
    window = pygame.display.set_mode((400, 400))


    def __init__(self, player1, player2, delay=0.3, destroyWhenOver=True, logicout=True):
        # os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0, 460)

        pygame.display.set_caption('Board')
        self.clock = pygame.time.Clock()
        self.logic = OthelloLogic(self, player1, player2, logicout)
        self.logicThread = threading.Thread(target=self.logic.run)
        self.reset()
        self.update()

    def update(self):
        self.reset()
        for r in range(8):
            for c in range(8):
                if self.logic.get(r, c) == 'X':
                    pygame.draw.circle(self.window, BLACK, (c * 50 + 25, r * 50 + 25), 25, 0)
                elif self.logic.get(r, c) == 'O':
                    pygame.draw.circle(self.window, WHITE, (c * 50 + 25, r * 50 + 25), 25, 0)
        for (r, c) in self.logic.valids:
            pygame.draw.circle(self.window,
                               BLACK if self.logic.turn == 'X'
                                     else WHITE,
                               (c * 50 + 25, r * 50 + 25), 2, 0
                               )
        pygame.display.update()

    def reset(self):
        self.window.fill(GREEN)
        for r in range(8):
            for c in range(8):
                pygame.draw.rect(self.window, BLACK, (c * 50, r * 50, 50, 50), 1)
        # pygame.display.update()

    def result(self):
        return self.logic.checkWin()

    def start(self):
        self.logicThread.start()
        while not self.result():
            pygame.event.get()
            pygame.display.update()
            self.clock.tick(100)
            # print(time.time())
        self.destroy()

    def startSingleThread(self):
        self.logic.run()

    def destroy(self):
        self.logicThread.join()