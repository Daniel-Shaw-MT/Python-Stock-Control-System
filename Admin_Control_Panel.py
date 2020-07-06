# imports
from tkinter import *
import tkinter.messagebox
import datetime
from subprocess import call
# This is the Main Menu of my program it allows a user to choose what he or she wants.


def openmain():
    call(["python", "SearchDB.py"])


def openupdate():
    call(["python", "updatedb.py"])


def openaddtobd():
    call(["python", "add_to_db.py"])


class MainMenu:

    def __init__(self, master, *args, **kwargs):
        # Title

        self.master = master
        self.heading = Label(master)
        self.heading = Label(master, text="Main Menu", font='Basetica 40 bold', fg='Black')
        self.heading.place(x=0, y=0)

        self.buttonupd = Button(master, text="Press to update the Database", width=25, command=openupdate)
        self.buttonupd.place(x=0, y=70)

        self.buttonaddtodb = Button(master, text="Press to add to the Database", width=25,  command=openaddtobd)
        self.buttonaddtodb.place(x=0, y=100)

        self.buttonopenmain = Button(master, text="Press to open main screen", width=25, command=openmain)
        self.buttonopenmain.place(x=0, y=130)


root = Tk()
b = MainMenu(root)

root.geometry("300x200+0+0")
root.title("Main Menu")
root.mainloop()
