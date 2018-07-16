from tkinter import *
import time
root = Tk()
def cl():
    l.config(text = "hi")
l = Label(root,text = "Red",activebackground = 'red')
l.pack()
Button(root,text = "change",command = cl).pack()
root.mainloop()
