
from tkinter import  *
import tkinter.messagebox as tmsg
root = Tk()
root.geometry('600x400')
root.title("sliders")
def get_hours():
    tmsg.showinfo("submitted",f"so you sleep {mysliders.get()} hours a day")

Label(root,text="how much  hours do you sleep in a week",font="lucida 19 bold").pack(side=TOP)
mysliders = Scale(root,from_=0,to=100,orient=HORIZONTAL)
mysliders.pack()

Button(root,text="submit",command=get_hours).pack()

root.mainloop()