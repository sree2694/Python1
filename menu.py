from tkinter import *

window = Tk()

mainMenu = Menu(window)
window.config(menu=mainMenu)

def test():
    print("hhhh")

fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="Open", command=test)
fileMenu.add_command(label="Save", command=test)
fileMenu.add_separator()
fileMenu.add_command(label="Close", command=test)

editMenu = Menu(mainMenu)
mainMenu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Undo")
editMenu.add_command(label="Redo")

mainMenu.add_command(label="Help")

window.mainloop()