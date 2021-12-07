from tkinter import *
from PIL import Image, ImageTk
root = Tk()
# sparsh = PhotoImage(file="enemy.png")
photo = Image.open("photo1.jpg")
sparsh = ImageTk.PhotoImage(photo)
me = Label(image=sparsh)
me.pack()
root.mainloop()