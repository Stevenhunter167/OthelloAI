import tkinter as tk
import threading
import time
from OthelloLogic import OthelloLogic
from AI.ManualAI import ManualAI
from AI.OthelloAI import OthelloAI
from AI.RandomAI import RandomAI

BLACK = 'X'
WHITE = 'O'

class OthelloGUI:

    # Public
    def __init__(self, player1, player2):
        self.root = tk.Tk()
        self.root.title("Main View")
        self.canvas = tk.Canvas(self.root, bg="green", height=400, width=400)
        self.logic = OthelloLogic(self, player1, player2)
        self.update()
        # tk.Button(self.root, text="start", command=self.start).pack()
        self.start()
        self.root.mainloop()

    def start(self):
        threading.Thread(target=self.logic.run).start()

    def update(self):
        winstatus = self.logic.checkWin()
        if winstatus:
            print(winstatus)
            # self.root.destroy()

        """ updates gui """
        self.canvas.delete("all")
        for r in range(8):
            for c in range(8):
                self.canvas.create_rectangle(c * 50, r * 50, c * 50 + 50, r * 50 + 50)
                if self.logic.get(r, c) != '.':
                    fill = {
                        "fill" : "black"
                    } if self.logic.get(r, c) == "X" else {
                        "fill" : "white"
                    }
                    self.canvas.create_oval(c * 50, r * 50, c * 50 + 50, r * 50 + 50, **fill)
        self.canvas.pack()
        time.sleep(0.3)
        # self.root.after(10000, self.update)

if __name__ == "__main__":
    # ManualAI(BLACK, name="manual ai")
    player1 = ManualAI(BLACK, "steven")
    player2 = RandomAI(WHITE)
    OthelloGUI(player1, player2)
