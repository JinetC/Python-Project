from tkinter import *

root = Tk()

def myClick():
    #myLebal = Label(root, text="My name is Jineth").pack()
    top = Toplevel()
    top.title("My second window")
    btn2 = Button(top, text="close", command=top.destroy).pack()

frame = LabelFrame(root, padx=50, pady=50)
frame.pack(padx=10, pady=10)


myButton = Button(frame, text="Vehicle Registration", padx=50, command=myClick)
myButton2 = Button(frame, text="Customer Use", padx=65, command=myClick)
mylabel2 = Label(frame, text="   ")
myButton.grid(row=0, column=0)
myButton2.grid(row=3, column=0)
mylabel2.grid(row=2, column=0)

root.mainloop()