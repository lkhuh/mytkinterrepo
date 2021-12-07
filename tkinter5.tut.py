from tkinter import *
root = Tk()
def hello():
    print("hello world")
root.geometry('888x444')
f1 = Frame(root,borderwidth=6,bg="grey",relief=SUNKEN)
f1.pack(side=LEFT, anchor="nw")
b1 = Button(f1,fg="red",text="print now",command=hello)
b1.pack()
root.mainloop()