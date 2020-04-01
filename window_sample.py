from tkinter import *

def clicked():
    lbl.configure(text="Button was clicked !!")


window = Tk()

window.title("Welcome to tkinter app")

lbl = Label(window, text="Hello")

lbl.grid(column=0, row=0)

btn = Button(window, text="Click Me", command=clicked)

btn.grid(column=1, row=0)

window.mainloop()