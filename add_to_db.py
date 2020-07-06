# Imports...
import os
from tkinter import *
import sqlite3
import tkinter.messagebox
import datetime
# This part of my program will be used to add new objects to my database. This is to be accessed by a network
# administrator or database architect.

# This command creates a connection between my program and my database. You will want to change the directory depending
# on where this project file is located.

# -------- Settings --------
current_directory = os.getcwd()

# You want to change this file path depending on the location of the file.
conn = sqlite3.connect(current_directory + '/DB/storefile.db')
c = conn.cursor()
# -------- Settings --------

# Selecting the ID from the table inventory.

result = c.execute("SELECT Max(id) from inventory")
for r in result:
    id = r[0]
current_date = datetime.date.today()


class Database:

    def __init__(self, master, *args, **kwargs):
        # Title
        self.master = master
        self.heading = Label(master)
        self.heading = Label(master, text="Add to the database", font='Basetica 40 bold', fg='Black')
        self.heading.place(x=0, y=0)

        # Title

        # labels for the system

        self.name_1 = Label(master, text="Enter Product Name", font='arial 18 bold')
        self.name_1.place(x=0, y=80)

        self.stock_1 = Label(master, text="Enter Product Stock", font='arial 18 bold')
        self.stock_1.place(x=0, y=120)

        self.Type_1 = Label(master, text="Enter Product Type", font='arial 18 bold')
        self.Type_1.place(x=0, y=160)

        self.vendor_1 = Label(master, text="Enter Product Vendor", font='arial 18 bold')
        self.vendor_1.place(x=0, y=200)

        self.date_l = Label(master, text="Enter Production Date", font='arial 18 bold')
        self.date_l.place(x=0, y=240)

        # Entries for all of the labels

        self.name_e = Entry(master, width=25, font='arial 18 bold')
        self.name_e.place(x=270, y=80)

        self.stock_e = Entry(master, width=25, font='arial 18 bold')
        self.stock_e.place(x=270, y=120)

        self.type_e = Entry(master, width=25, font='arial 18 bold')
        self.type_e.place(x=270, y=160)

        self.vendor_e = Entry(master, width=25, font='arial 18 bold')
        self.vendor_e.place(x=270, y=200)

        self.date_e = Entry(master, width=25, font='arial 18 bold')
        self.date_e.place(x=270, y=240)

        self.btn_add = Button(master, text="Add to Database", font='arial 10', width=25, height=2, command=self.get_items)
        self.btn_add.place(x=415, y=320)

        # text box for logs

        self.tBox = Text(master, width=65, height=20)
        self.tBox.place(x=650, y=70)
        self.tBox.insert(END, "ID is "+ str(id))

    def get_items(self, *args, **kwargs):

        # Get from the entry boxes

        self.name = self.name_e.get()
        self.stock = self.stock_e.get()
        self.type = self.type_e.get()
        self.vendor = self.vendor_e.get()
        self.dateofa = current_date
        self.dateop = self.date_e.get()

        if self.name == '' or self.stock == '' or self.type == '':
            tkinter.messagebox.showinfo("Error Please fill in the specified fields", " Please Try again")
        else:
            sql = "INSERT INTO inventory (Name, Type, Vendor, Stock, date, dateofproduction) VALUES(?,?,?,?,?,?)"
            (c.execute(sql, (self.name, self.type, self.vendor, self.stock, self.dateofa, self.dateop)))
            conn.commit()
            tkinter.messagebox.showinfo("Success", "Added to the Database")

            # Adding messages to the provided text box for user
            self.tBox.insert(END, "\n\nInserted "+str(self.name) + " into the database.")

        # This Function will clear the entry fields

    def clear_all(self):
        self.name_e.delete(0, END)
        self.stock_e.delete(0, END)
        self.type_e.delete(0, END)
        self.vendor_e.delete(0, END)
        self.date_e.delete(0, END)


root = Tk()
b = Database(root)

root.geometry("1200x400+0+0")
root.title("Add to the database")
root.mainloop()

