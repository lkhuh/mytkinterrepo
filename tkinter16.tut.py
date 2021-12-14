from tkinter import *
root = Tk()
root.geometry('800x400')
root.title("status bar tut")
def upload():
    status.set("BUSY")
    sbar.update()
    import time
    time.sleep(5)
    status.set("READY NOW")
status = StringVar()
status.set("Ready")
sbar = Label(root,textvariable=status,relief=SUNKEN,anchor="w")
sbar.pack(fill=X,side=BOTTOM)
Button(root,text="UPLOAD",command=upload).pack()
root.mainloop()