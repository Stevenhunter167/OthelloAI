from tkinter import *
import threading

def createWindow():
    root = [None]
    def newthread():
        root[0] = Tk()
        root[0].mainloop()
    threading.Thread(target=newthread).start()
    return root[0]

root = createWindow()

while True:
    print(root)
    input()
    Button(root, text="hello").pack()