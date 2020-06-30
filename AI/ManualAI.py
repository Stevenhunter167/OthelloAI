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
