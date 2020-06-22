from tkinter import *
import pygame
from AI.Base.OthelloBaseAI import OthelloBaseAI

class ManualAI(OthelloBaseAI):

    window = pygame.display.set_mode((400, 400))

    def __init__(self, color, name):
        self.name = name
        self.color = color

    def getAction(self, board) -> (int, int):
        while True:
            if pygame.mouse.get_pressed() == (1, 0, 0):
                (x, y) = pygame.mouse.get_pos()
                pygame.event.clear()
                # print(x, y)
                return (y // 50, x // 50)

        # root = Tk()
        # root.geometry("400x400+0+0")
        # root.title(self.name + " " + self.color)
        # canvas = Canvas(root, bg="white", height=400, width=400)
        # for r in range(8):
        #     for c in range(8):
        #         canvas.create_rectangle(c * 50, r * 50, c * 50 + 50, r * 50 + 50)
        #         if board[r][c] != '.':
        #             fill = {
        #                 "fill" : "black"
        #             } if board[r][c] == "X" else {}
        #             canvas.create_oval(c * 50, r * 50, c * 50 + 50, r * 50 + 50, **fill)
        # for r, c in self.availablePositions(board):
        #     canvas.create_oval(c * 50 + 22, r * 50 + 22, c * 50 + 28, r * 50 + 28, fill="black")
        #
        # res = [0, 0]
        # def callback(event):
        #     r = event.y // 50
        #     c = event.x // 50
        #     res[0], res[1] = r, c
        #     print(self.name + " clicked at", r, c)
        #     root.destroy()
        #
        # canvas.bind("<Button-1>", callback)
        # canvas.pack()
        # root.mainloop()

        return
