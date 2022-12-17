from tkinter import *

window = Tk()

fTop = Frame(window)
fTop.pack()
fBot = Frame(window)
fBot.pack(side=BOTTOM)

lbl1 = Label(fTop, text="Hello")
lbl2 = Label(fTop, text="Top")
lbl3 = Label(fBot, text="Bottom")
lbl1.pack(side=LEFT)
lbl2.pack(side=LEFT)
lbl3.pack()
window.mainloop()