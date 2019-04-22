from tkinter import *
from tkinter import messagebox
b = 0 
def newt():
    global b
    b = b + 1
    Button(root,text=b,command = newt,font=12,bg = "#ECF0F1").grid()
    if b > 10:
        messagebox.showerror('stop')
root = Tk()                        #starting tkinter
root.title("Power Of Python")
root.geometry("900x900+150+50")   #dimension of window 
root.configure(background="#057596")    #background colour for window
root.state('zoomed')
right = Frame(root,bg = "pink",width = 1500,height = 30)
right.place(x = 1,y = 1)
Button(root,text = "New Tab",command=newt,relief= RAISED,font=12,bg = "#ECF0F1").grid(row = 1)  #b1 button
Button(root,text = "Close here",command = root.destroy,relief = RAISED,font=12,bg = "#ECF0F1").place(x = 1276,y = 1)
root.mainloop()
