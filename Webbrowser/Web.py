#Web Browser using Python(tkinter) 
#Motto behind this show the power of python
#before run this, need to ensure to install all package
from tkinter import *  #* means all
from win10toast import ToastNotifier
import urllib.request,os,time,socket,random,webbrowser,datetime,winsound,re,pyautogui #multiple module import
from tkinter import messagebox
##from urllib.parse import quote
from tkinter.filedialog import askopenfilename #multiple module at once reduce delay in runtime
from datetime import date   #date and time module
from sys import getsizeof    #sys access module and size of data module
##def fn():                             '''calling function for event '''
##print("Testing")
'''This is where all function are written for event handling'''
def donothing():
    print("Ok")
def messag():    #New window for help option
    win = Toplevel(root)
    win.title("Hello, We are here helping for you")
##    Label(root,text = "Symbol Identity").place(x = 2, y = 5)
    msg = Message(win,text = "Hi,Welcome to EXDEVELOPERS COMPANY,\n\n This is all done in Python with Tkinter Framework\n\n Python is very verstatile language and it is widely used language.\n\n I know some have symbol language problem , it may new for someone or it may be confusing. \n\n Don't worry we will settle down your nerve that is holding some disaster question related to this")
    msg.pack()
#This is menubar command without function
##menubar = Menu(root)
##filemenu = Menu(menubar,tearoff = 0)
##filemenu.add_command(label="Open",command = donothing)
##filemenu.add_command(label="Save",command = donothing)
##filemenu.add_command(label="Print",command = donothing)
##filemenu.add_command(label="Exit",command = ck)
##filemenu.add_cascade(label="File",menu=filemenu)
##helpmenu=Menu(menubar,tearoff=0)
##helpmenu.add_command(label="Help index",command = donothing)
##helpmenu.add_command(label="About",command = donothing)
##menubar.add_cascade(label="Help",menu=helpmenu)
def cl():
    winsound.MessageBeep()
    root.destroy()
def seac():
    print("",a.get())
def uio():
    exec(open("surfingweb.py").read())  #execute new file 
##def open():
##    url = input()
##    return webbrowser.open(url,new =0,autoraise = True)
def newtab():  #new tab function
    try:
        webbrowser.open(a.get())
    except:
        print("Failed to load")
##def sety():
##    try:
##        url = input()
##        webbrowser.open(url)
##    except:
##        print("Error due to multi-threading")
def dia():
    fname = askopenfilename(filetypes=(("Template files", "*.tplate")
                                                         ,("HTML files", "*.html;*.htm")
                                                         ,("All files", "*.*")))

def ck():
    if messagebox.askokcancel(title = "Do you want to quit",message = "Are you sure?",icon = "warning"):
        root.destroy()
time1 = ' '        
def clos():
    global time1
    time2 = time.strftime('%I:%M:%S:%p')
    if time2 != time1:
        time1 = time2
        clock.config(text = time2)
    clock.after(200,clos)
s = datetime.datetime.now().strftime("%a-%d-%b-%y")    #use date module without function,if we use
                                                    #we need to update time with date that
                                                    #quite difficult task, that why we use var alone

def se():
    print("hu")
def hel():
    print("help")
def do_popup(event):
    # display the popup menu
    try:
        popup.tk_popup(event.x_root, event.y_root, 0)
    finally:
        # make sure to releasethe grab (Tk 8.0a1 only)
        popup.grab_release()    
def ty():
    root.withdraw
    p = pyautogui.prompt('Save file as','Screenshot')
    try:
        s = pyautogui.screenshot(p+'.jpg')
        pyautogui.confirm('Done','Confirmation message')
    except:
        print('Failed to load')
##def     
##time1 = ''
##def ut():
##    global time1
##    time2 = time.strftime('%H:%M:%S')
##    if time2 != time1:
##        time1 = time2
##        clock.config(text = time2)
##        clock.after(1000,tick)   
            
##def toa():
##    toast = ToastNotifier()
##    toast.show_toast("HI,this is test")


##def callback(*args):
##    print ("variable changed!")

##def motion(event): #motion tracking
##print("Mouse position: (%s %s)" % (event.x, event.y))
##  return    #binding event with mouse
root = Tk()                        #starting tkinter
root.title("Power Of Python")
root.geometry("900x900+150+50")   #dimension of window 
root.configure(background="#2e76ea")    #background colour for window
root.state('zoomed')    
left = Frame(root,bg = "#9900FF",highlightbackground="green", highlightcolor="green", highlightthickness=1,width = 700,height =1000)   #creating frame with {left} var
left.place(x = 700,y = 0)
#right frame for top menu
right = Frame(root,bg = "#25A1C0",width = 1500,height = 30)
right.place(x = 1,y = 1)
#side frame for shortcut keys
side = Frame(root,bg = '#6C3483',highlightbackground="#B3B6B7", highlightcolor="#B3B6B7", highlightthickness=1,width = 50,height = 703)
side.place(x = 1,y = 35)
##right = Frame(root,bg = "yellow",width = 450,height = 800)
##right.grid(row = 1)
a = Entry(root, font="Monochrome 15 ", width=40,bg = "#FF5733")   #entry labal is created
a.place(x = 150,y = 90)
a.delete(0,END)
a.insert(0," ")    #putting string
##imag = PhotoImage(file='C:/Users/Kumar Builders/Downloads/if_icon-129-cloud-download_314243.gif')
##toast = Entry(root)
##toast.place(x = 25,y = 180)
##messagebox.showinfo(title = "Read carefully",message = "This is python based browser , aim of this browser to highlight the power of python")
##messagebox.askquestion(title = "Read carefully",message = "Do you love python",icon = "question")
##messagebox.showwarning(title = "Read carefully",message = "Be safe from hackers,don't try to be hero on internet",icon = 'warning')

##var = StringVar()
##menubar = Menu(left)
####Motion = "-------------------------------------------------------------------------------------"  #putting str for motion tracking
##filemenu = Menu(menubar,tearoff = 3)
##filemenu.add_command(label = "New",command = ck)
##filemenu.add_command(label = "Open",command = ck)
##filemenu.add_command(label = "Print",command = ck)
##filemenu.add_command(label = "Save",command = ck)
##filemenu.add_command(label = "Close",command = cl)
##menubar.add_cascade(label = "File",menu = filemenu)
##filemenu.add_command(label = "Undo",command = ck)
##filemenu.add_command(label = "Open",command = cl)
##filemenu.add_command(label = "Print",command = ck)
##filemenu.add_command(label = "Save",command = cl)
##filemenu.add_command(label = "Close",command = cl)
##menubar.add_cascade(label = "Edit",menu = filemenu)
####popup = Menu(root, tearoff=0)
####popup.add_command(label="Next",command=ty) # , command=next) etc...
####popup.add_command(label="Previous")
####popup.add_separator()
####popup.add_command(label="Home")
####w = Label(root)
####w.place()
####w.bind("<Button-3>", do_popup)
Button(root,text = "Leave",command = ck,relief= RAISED,font=12,bg = "#ECF0F1").grid(row = 1)  #b1 button
##b2 = Button(root,text = "Quit",command = cl,relief=RIDGE).pack(side="top", anchor = SE)
####b2 = Button(root,text = "Quit",command = cl).grid(row = 2,column = 100)
Button(root,text = '+Tab',command = uio,relief= RAISED,font=12,bg = "#ECF0F1").grid(row = 1,column = 1)
Button(root,text = 'Open file',command = dia,relief= RAISED,font=12,bg = "#ECF0F1").grid(row = 1,column = 2)
Button(root,text = "Search",command = newtab,relief=GROOVE,font=12,bg = "#3498DB").place(x = 60,y = 88) # button
##Button.bind('<Enter>',open)
Button(root,text = "Home",command = cl,relief = RAISED,font = 12,bg = "#ECF0F1").place(x = 183,y = 0)
Button(right,text = "≡",command = cl,font = ('Times',15,'bold'),bg = "#ECF0F1").place(x = 1335,y = 0,relx = 0,rely = 0)
c = Button(side,text = '~',command = cl,relief = GROOVE,font = ('times',15,'bold'),width = 3)
c.bind('<Control-q>',cl)
c.place(x = 1,y = 1)
Button(root,text = 'Help',command = messag,font = ('times',12,'bold')).place(x = 239,y = 0)
Button(side,text = '↓',relief = GROOVE,font = ('times',12,'bold'),width = 4).place(x = 1,y = 40)
Button(side,text="«",relief = GROOVE,font = ('times',15,'bold'),width = 3).place(x = 1,y = 72)
Button(side,text="*",command = ty,relief = GROOVE,font = ('times',15,'bold'),width = 3).place(x = 1,y = 112)
Button(side,text="*",relief = GROOVE,font = ('times',15,'bold'),width = 3).place(x = 1,y = 152)
Button(side,text="?",command = messag,relief = GROOVE,font = ('times',15,'bold'),width = 3).place(x = 1,y = 192)
Button(side,text="",command = root.bell,relief = GROOVE,font = ('times',15,'bold'),width = 3).place(x = 1,y = 232)
##Label(root,text = "check").grid(row = 3,column = 4,padx=2)
##Label(root,text = "Want to show something?").place(x = 20,y = 150)
##Button(root,text = "Check",command = home).place(x = 23,y = 140)
##clock = Label(right,font=("Helvetica", 15),width = 50,height = 1).place(x = 30,y = 5)
Label(left,text = "Data usage",font = 12,bg = "#19C70E",relief = FLAT,padx = 2,justify = CENTER,width = 73).place(x = 3,y = 30) #create label in frame
Label(left,text = "Internet Speed",font = 12,bg = "#19C70E",relief = RIDGE,padx = 2,justify = CENTER,width = 73).place(x = 3,y = 350)  #create another label for new label
clock = Label(root,font=('times',15,'bold'),bg = '#25A1C0',width = 70,height = 0)
clock.place(x = 300, y = 1)
Label(root,text = s,font = ('times',15,'bold'),bg = "#25A1C0",width = 20,height = 1).place(x = 400,y = 1)  #create another label for new label
##msg = Message(root,text = Motion)   #create an event with motion string and closing them
##msg.bind("<Motion>",motion)
##msg.grid(row = 170,column = 20)
##root.config(menu = menubar)
##toast = Tk()
##toast = ToastNotifier()
##toast.show_toast("HI,WELCOME TO EXDEVELOPER PRODUCT")
clos()      #clock module 
root.mainloop()   #end of tkinter
