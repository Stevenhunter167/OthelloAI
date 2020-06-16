import tkinter as tk
import threading
from OthelloLogic import OthelloLogic
from AI.OthelloAI import OthelloAI

# def createWindow(geo="400x400"):
#     root = [None]
#     def newthread():
#         root[0] = tk.Tk()
#         root[0].geometry(geo)
#         root[0].mainloop()
#     threading.Thread(target=newthread).start()
#     return root[0]

class OthelloGUI:

    # Public
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Main View")
        self.canvas = tk.Canvas(self.root, bg="white", height=400, width=400)

        player1 = OthelloAI()
        player2 = OthelloAI()
        self.logic = OthelloLogic(self, player1, player2)
        self.update()
        tk.Button(self.root, text="start", command=self.start).pack()
        self.root.mainloop()

    def start(self):
        threading.Thread(target=self.logic.run).start()

    def update(self):
        """ updates gui """
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
        self.root.after(5000, self.update)

if __name__ == "__main__":
    OthelloGUI()