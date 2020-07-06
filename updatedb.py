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
conn = sqlite3.connect(current_directory + '/Databases/storefile.db')
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
        self.heading = Label(master, text="Update the database", font='Basetica 40 bold', fg='Black')
        self.heading.place(x=0, y=0)

        # Title

        # Label and entry for id and button

        self.id_le = Label(master, text="Enter ID", font='arial 18 bold')
        self.id_le.place(x=0, y=80)

        self.id_leb = Entry(master, font='arial 18 bold', width=15)
        self.id_leb.place(x=270, y=80)

        self.btn_search = Button(master, text="Search", width=10, height=1, command=self.search)
        self.btn_search.place(x=480, y=82)

        # labels for the system

        self.name_1 = Label(master, text="Enter Product Name", font='arial 18 bold')
        self.name_1.place(x=0, y=120)

        self.stock_1 = Label(master, text="Enter Product Stock", font='arial 18 bold')
        self.stock_1.place(x=0, y=160)

        self.Type_1 = Label(master, text="Enter Product Type", font='arial 18 bold')
        self.Type_1.place(x=0, y=200)

        self.vendor_1 = Label(master, text="Enter Product Vendor", font='arial 18 bold')
        self.vendor_1.place(x=0, y=240)

        self.date_1 = Label(master, text="Enter Date of Entry", font='arial 18 bold')
        self.date_1.place(x=0, y=280)

        self.datep_1 = Label(master, text="Enter Production Date", font='arial 18 bold')
        self.datep_1.place(x=0, y=320)

        # Entries for all of the labels

        self.name_e = Entry(master, width=25, font='arial 18 bold')
        self.name_e.place(x=270, y=120)

        self.stock_e = Entry(master, width=25, font='arial 18 bold')
        self.stock_e.place(x=270, y=160)

        self.type_e = Entry(master, width=25, font='arial 18 bold')
        self.type_e.place(x=270, y=200)

        self.vendor_e = Entry(master, width=25, font='arial 18 bold')
        self.vendor_e.place(x=270, y=240)

        self.date_e = Entry(master, width=25, font='arial 18 bold')
        self.date_e.place(x=270, y=280)

        self.datep_e = Entry(master, width=25, font='arial 18 bold')
        self.datep_e.place(x=270, y=320)
        # Buttons

        self.btn_add = Button(master, text="Update Database", font='arial 10', width=25, height=2, command=self.update)
        self.btn_add.place(x=390, y=360)

        self.btn_del = Button(master, text="Delete Record", font='arial 10', width=25, height=2, command=self.delete)
        self.btn_del.place(x=390, y=410)
        # text box for logs

        self.tBox = Text(master, width=65, height=20)
        self.tBox.place(x=650, y=70)
        self.tBox.insert(END, "ID is " + str(id))

        # insert into the entries to update

    def search(self, *args, **kwargs):

        # Removing text

        self.name_e.delete(0, END)
        self.type_e.delete(0, END)
        self.vendor_e.delete(0, END)
        self.stock_e.delete(0, END)
        self.date_e.delete(0, END)
        self.datep_e.delete(0, END)

        sql = "SELECT * FROM inventory WHERE id=?"
        result = c.execute(sql, (self.id_leb.get(), ))
        for r in result:
            self.n1 = r[1]  # Name
            self.n2 = r[2]  # Type
            self.n3 = r[3]  # Vendor
            self.n4 = r[4]  # Stock
            self.n5 = r[5]  # Date of addition to db
            self.n6 = r[6]  # Date of Production
        conn.commit()

        # Inserting into my text field

        self.name_e.insert(0, str(self.n1))
        self.type_e.insert(0, str(self.n2))
        self.vendor_e.insert(0, str(self.n3))
        self.stock_e.insert(0, str(self.n4))
        self.date_e.insert(0, str(self.n4))
        self.datep_e.insert(0, str(self.n5))

    def update(self, *args, **kwargs):

        # Retrieving data
        self.u1 = self.name_e.get()
        self.u2 = self.type_e.get()
        self.u3 = self.vendor_e.get()
        self.u4 = self.stock_e.get()
        self.u5 = self.date_e.get()
        self.u6 = self.datep_e.get()

        query = "UPDATE inventory SET name=?, type=?, vendor=?, stock=?, date=?, dateofproduction=? WHERE id=?"
        c.execute(query, (self.u1, self.u2, self.u3, self.u4, self.u5, self.u6, self.id_leb.get()))
        conn.commit()
        # Get the updated fields and update

        tkinter.messagebox.showinfo("Success", "Updated")

    def delete(self, *args, **kwargs):
        get_id = self.id_leb.get()

        sql = 'DELETE FROM inventory WHERE id=?'
        c.execute(sql, (get_id,))
        conn.commit()
        self.name_e.delete(0, END)
        self.stock_e.delete(0, END)
        self.type_e.delete(0, END)
        self.vendor_e.delete(0, END)
        self.date_e.delete(0, END)
        self.datep_e.delete(0, END)

root = Tk()
b = Database(root)

root.geometry("1200x470+0+0")
root.title("Update the database")
root.mainloop()

