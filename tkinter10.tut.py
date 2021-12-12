from tkinter import *
root = Tk()
root.geometry('500x400')
root.title("Menu's and submenus")
def my_func():
    print("hello world")


mymenu = Menu(root)
m2 = Menu(mymenu,tearoff=0)
m2.add_command(label="FILE",command=my_func)
m2.add_command(label="Save",command=my_func)
root.config(menu=mymenu)
mymenu.add_cascade(label="file",menu=m2)


m3 = Menu(mymenu,tearoff=0)
m3.add_command(label="save as",command=my_func)
m3.add_command(label="exit",command=my_func)
root.config(menu=mymenu)
mymenu.add_cascade(label="all you want",menu=mymenu)

root.mainloop()