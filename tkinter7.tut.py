from tkinter import *
root = Tk()

def getvals():
    print(f"{name_value.get(),phone_value.get(),payment_value.get(),standard_value.get(),gender_value.get(),roll_value.get(),check_box.get()}")
    with open("record.txt","a") as f:
        f.write(f"{name_value.get(),phone_value.get(),payment_value.get(),standard_value.get(),gender_value.get(),roll_value.get(),check_box.get()}")




root.geometry('644x344')
Label(root,text="CANDIDA PUBLIC SCHOOL",font="comicsansms 13 bold").grid(row=0,column=3)
name = Label(root,text="Name").grid(row=1,column=1)
phone = Label(root,text="phone").grid(row=2,column=1)
payment = Label(root,text="payment").grid(row=3,column=1)
standard = Label(root,text="class").grid(row=4,column=1)
gender = Label(root,text="gender").grid(row=5,column=1)
roll_no = Label(root,text="roll no").grid(row=6,column=1)

name_value = StringVar()
phone_value = StringVar()
payment_value = StringVar()
standard_value = StringVar()
gender_value = StringVar()
roll_value = StringVar()
check_box = IntVar()


main_name = Entry(root,textvariable=name_value).grid(row=1,column=3)
main_phone = Entry(root,textvariable=phone_value).grid(row=2,column=3)
main_payment = Entry(root,textvariable=payment_value).grid(row=3,column=3)
main_standard = Entry(root,textvariable=standard_value).grid(row=4,column=3)
main_gender = Entry(root,textvariable=gender_value).grid(row=5,column=3)
main_roll = Entry(root,textvariable=roll_value).grid(row=6,column=3)

Button(text="Submit",command=getvals).grid(row=7,column=3)
Checkbutton(variable=check_box,text="have you meet the principal").grid(row=8,column=3)

root.mainloop()