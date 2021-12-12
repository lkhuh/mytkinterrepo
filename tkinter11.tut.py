from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.geometry('600x450')
root.title("messagebox")
def func():
    print("hello")
def help():
    tmsg.showinfo(title="help for this GUI",message="Do you think this gui will succedd or not")
def rate():
    tmsg.askquestion("rate us","was you experience good")
mymenu = Menu(root)
m1 = Menu(mymenu,tearoff=0)
m1.add_command(label="file",command=func)
mymenu.add_cascade(label="file",menu=m1)
root.config(menu=mymenu)

m2 = Menu(mymenu,tearoff=0)
m2.add_command(label="save",command=func)
mymenu.add_cascade(label="save",menu=m2)
root.config(menu=mymenu)

m3 = Menu(mymenu,tearoff=0)
m3.add_command(label="help",command=help)
m3.add_command(label="rate",command=rate)
root.config(menu=mymenu)
mymenu.add_cascade(label="help",menu=m3)
root.mainloop()