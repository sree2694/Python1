from tkinter import *

window = Tk()

labelUser = Label(window, text="Username:")
labelPass = Label(window, text="Psw:")
eUser = Entry(window)
ePass = Entry(window)

labelUser.grid(row=0, sticky=E)
labelPass.grid(row=1, sticky=E)
eUser.grid(row=0, column=1)
ePass.grid(row=1, column=1)
window.mainloop()