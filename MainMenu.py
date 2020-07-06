# imports
from tkinter import *
from subprocess import call
# This is the Main Menu of my program it allows a user to choose what he or she wants.


def openmain():
    call(["python", "SearchDB.py"])


class MainMenu:

    def __init__(self, master, *args, **kwargs):
        # Title

        self.master = master
        self.heading = Label(master)
        self.heading = Label(master, text="Main Menu.", font='Basetica 40 bold', fg='Black')
        self.heading.place(x=0, y=0)

        self.buttonopenmain = Button(master, text="Press to open main screen...", width=25, command=openmain)
        self.buttonopenmain.place(x=0, y=65)


root = Tk()
b = MainMenu(root)

root.geometry("300x100+0+0")
root.title("Main Menu")
root.mainloop()
