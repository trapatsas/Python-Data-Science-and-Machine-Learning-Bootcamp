import tkinter # note that module name has changed from Tkinter in Python 2 to tkinter in Python 3
from tkinter import Button,Label,Entry
top = tkinter.Tk()

L1 = Label(top, text="User Name")
#L1.pack( side = LEFT)
E1 = Entry(top, bd =5)

#E1.pack(side = RIGHT)
# Code to add widgets will go here...
w = Button (top)
top.mainloop()