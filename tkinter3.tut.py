from tkinter import *
root = Tk()

root.geometry('444x244')
root.title("sparsh's GUI")
sparsh = Label(text="MY name is sparsh saxena and this is what you can know from my website if you are interested in any"
               ,bg="red",fg="white",padx="44",pady="55",font="comicsansms 9 bold",borderwidth=8,relief=SUNKEN)
sparsh.pack(side=LEFT,fill=Y,padx=34,pady=4)
root.mainloop()