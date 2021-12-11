from tkinter import *

def SPARSH(event):
    print(f"you clicked on the buttton at")
root = Tk()

root.geometry('900x500')
root.title("tut 9")
widget = Button(root,text="Click me")
widget.pack(side="top")
widget.bind('<Button-1>',SPARSH)

root.mainloop()