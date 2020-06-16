# packages
import tkinter as tk
import threading
import time

# Othello Logic
from OthelloLogic import OthelloLogic


class OthelloGUI:

    def __init__(self, player1, player2, delay=0.3, destroyWhenOver=True):
        # GUI Params
        self.delay = delay
        self.destroyWhenOver = destroyWhenOver

        # GUI Main Window
        self.root = tk.Tk()
        self.root.title("Main View")
        self.canvas = tk.Canvas(self.root, bg="green", height=400, width=400)
        self.logic = OthelloLogic(self, player1, player2)
        self.update()
        self.start()
        self.root.mainloop()

    def start(self):
        # start logic in a separate thread
        threading.Thread(target=self.logic.run).start()

    def update(self):
        """ updates gui """
        winStatus = self.logic.checkWin()
        if winStatus:
            if self.destroyWhenOver:
                self.root.destroy()

        # refresh gui: update all cells
        self.canvas.delete("all")
        for r in range(8):
            for c in range(8):
                self.canvas.create_rectangle(c * 50, r * 50, c * 50 + 50, r * 50 + 50)
                if self.logic.get(r, c) != '.':
                    self.canvas.create_oval(c * 50, r * 50, c * 50 + 50, r * 50 + 50,
                                            fill='black' if self.logic.get(r, c) == "X" else 'white')
        self.canvas.pack()
        time.sleep(self.delay)

    def result(self):
        return self.logic.checkWin()

    def destroy(self):
        self.root.destroy()
