from tkinter import  *
root = Tk()
root.geometry('600x400')
root.title("LISTBOX tut")
listbox = Listbox(root)
listbox.pack()
listbox.insert(END,"hello")
root.mainloop()