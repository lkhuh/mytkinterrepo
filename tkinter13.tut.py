from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root.geometry('555x400')
root.title("radio buttons")
def get_order():
    tmsg.showinfo("your order",f"we have recieved your order of {var.get()}")
var = StringVar()
var.set("radio")
Label(root,text="what do you like to have sir?",font="comisansms 19 bold").pack()
radio = Radiobutton(root,text="dosa",var=var,value="dosa").pack(anchor="w")
radio = Radiobutton(root,text="Idly",var=var,value="Idly").pack(anchor="w")
radio = Radiobutton(root,text="vada pav",var=var,value="vada pav").pack(anchor="w")
radio = Radiobutton(root,text="samosa",var=var,value="samosa").pack(anchor="w")
Button(root,text="order",command=get_order,padx=54).pack()
root.mainloop()