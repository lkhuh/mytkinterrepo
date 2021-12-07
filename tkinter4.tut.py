from tkinter import *
root = Tk()
root.geometry("855x455")
f1 = Frame(root,bg="grey",relief=SUNKEN,borderwidth="6")
f1.pack(side=LEFT,fill="y")

f2 = Frame(root,bg="grey",relief=SUNKEN,borderwidth="8")
f2.pack(side=TOP,fill="x")
l = Label(f1,text="project tkinter" )
l.pack(pady=142)

l1 = Label(f2,text="welcome to sublime text",font="comicsansms 19 bold",fg="red")
l1.pack()
root.mainloop()