from tkinter import *
window = Tk()

def handleClick():
    print("Button Clicked")

btn = Button(window, bd = 20, bg="Green", fg="White", text="Click Me",
padx=50, pady=80, command=handleClick)
btn.place(x=50, y=50)

window.mainloop()