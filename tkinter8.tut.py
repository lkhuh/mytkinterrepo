from tkinter import *
root = Tk()
root.title("Sparsh's GUI")
canvas_width = 800
canvas_height = 400
root.geometry(f"{canvas_width}x{canvas_height}")
can_widget = Canvas(root, width=canvas_width, height=canvas_height)
can_widget.pack()
can_widget.create_line(0,400,800,0,fill="blue")
can_widget.create_text(250,300,text="PYTHON")
can_widget.create_rectangle(3,7,200,500,fill="red")
can_widget.create_oval(3,7,200,500)
root.mainloop()