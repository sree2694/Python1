from tkinter import *
def PrintValue():
    print(userWrote.get())
window = Tk()
userWrote = StringVar()
userWrote.trace("w", lambda name, index, mode : PrintValue())
e = Entry(window, fg="Green", bd=5, bg="Black", textvariable=userWrote)
e.pack()

window.mainloop()