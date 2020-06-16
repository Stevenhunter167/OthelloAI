from tkinter import *

class ManualAI:

    def __init__(self, color, name):
        self.name = name
        self.color = color

    def getAction(self, board) -> (int, int):

        root = Tk()
        root.geometry("400x400+0+0")
        root.title(self.name + " " + self.color)
        canvas = Canvas(root, bg="white", height=400, width=400)
        for r in range(8):
            for c in range(8):

                canvas.create_rectangle(c * 50, r * 50, c * 50 + 50, r * 50 + 50)

                if board[r][c] != '.':
                    fill = {
                        "fill" : "black"
                    } if board[r][c] == "X" else {}
                    canvas.create_oval(c * 50, r * 50, c * 50 + 50, r * 50 + 50, **fill)

        res = [0, 0]
        def callback(event):
            r = event.y // 50
            c = event.x // 50
            res[0], res[1] = r, c
            print("clicked at", r, c)
            root.destroy()

        canvas.bind("<Button-1>", callback)
        canvas.pack()
        root.mainloop()

        return tuple(res)