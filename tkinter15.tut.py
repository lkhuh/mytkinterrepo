from tkinter import *
root = Tk()
root.geometry('600x400')
root.title("scrollbar tut")

scrollbar = Scrollbar(root)
scrollbar.pack(fill=Y,side=RIGHT)





listbox = Listbox(root,yscrollcommand=scrollbar.set)

for i in range(34444):
     listbox.insert(END,f"item {i}")
listbox.pack(fill=BOTH,padx=22,pady=60)

scrollbar.config(command=listbox.yview())




root.mainloop()