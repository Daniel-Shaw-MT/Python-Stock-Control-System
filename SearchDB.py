# Imports...
import tkinter
from tkinter import *
from tkinter import messagebox
import sqlite3
import datetime
import cv2
import pyzbar.pyzbar as pyzbar
import re
from subprocess import call
import os
# Notes
# I am using open cv to access the camera and use it to capture images for pyzbar to interpret
# You require all of the imported packages for the program to run as its essential.
# Re is used to replace the -b'' of pyzbar. It is also essential for the function of the program

# This file allows a front end user to check items. It can be used to look up information.

# Connects the database to my program

current_directory = os.getcwd()

# This get the current working directory and uses it to locate the database.

conn = sqlite3.connect(current_directory+'/Databases/storefile.db')

c = conn.cursor()


class Application:
    def __init__(self, master, *args, **kwargs):

        self.master = master
        # frame
        self.left = Frame(master, width=800, height=768, bg='white')
        self.left.pack(side=LEFT)

        # components
        self.heading = Label(self.left, text="Search The Database", font="basetica 40 bold", bg="white")
        self.heading.place(x=0, y=5)

        self.buttonscnqr = Button(self.left, text="Search Database With QR", width=22, height=2, bg='orange',
                                  command=self.checkdbqr)
        self.buttonscnqr.place(x=550, y=130)

        self.buttonscn = Button(self.left, text="Search Database", width=22, height=2, bg='orange',
                                command=self.checkdbenterid)
        self.buttonscn.place(x=550, y=85)

        self.enterid = Label(self.left, text='Enter product ID:', font='arial 18 bold', bg='white')
        self.enterid.place(x=0, y=90)

        self.enteride = Entry(self.left, width=25, font='arial 18 bold', bg='light gray')
        self.enteride.place(x=200, y=90)

        self.productname = Label(self.left, text="", font='arial 18 bold', bg='white')
        self.productname.place(x=0, y=145)

        self.producttype = Label(self.left, text="", font='arial 18 bold', bg='white')
        self.producttype.place(x=0, y=205)

        self.productvendor = Label(self.left, text="", font='arial 18 bold', bg='white')
        self.productvendor.place(x=0, y=175)

        self.productstock = Label(self.left, text="", font='arial 18 bold', bg='white')
        self.productstock.place(x=0, y=235)

        self.productdate = Label(self.left, text="", font='arial 18 bold', bg='white')
        self.productdate.place(x=0, y=285)

        self.productdateofp = Label(self.left, text="", font='arial 18 bold', bg='white')
        self.productdateofp.place(x=0, y=315)

        self.buttoncheckforqr = Button(self.left, text="Check for QR...", width=22, height=2, bg='orange',
        command=self.check_for_qr)
        self.buttoncheckforqr.place(x=550, y=175)

    # Checking by the ID

    def checkdbenterid(self, *args, **kwargs):
        try:
            self.get_id = self.enteride.get()
            # Get the products info and id and fill the labels
            query = "SELECT name, type, vendor, stock, date, dateofproduction FROM inventory WHERE id=?"
            result = c.execute(query, (self.get_id,))

            for self.r in result:
                self.get_name = self.r[0]
                self.get_type = self.r[1]
                self.get_vendor = self.r[2]
                self.get_stock = self.r[3]
                self.get_date = self.r[4]
                self.get_proddate = self.r[5]

            self.productname.configure(text="Product name: " + str(self.get_name))
            self.producttype.configure(text="Type: " + str(self.get_type))
            self.productvendor.configure(text="Vendor: " + str(self.get_vendor))
            self.productdate.configure(text="Date of Addition to DB: " + str(self.get_date))
            self.productdateofp.configure(text="Date of Manufacture: " + str(self.get_proddate))
            self.productstock.configure(text="Amount in stock: " + str(self.get_stock))
            self.enteride.delete(0, END)
        except(Exception):
            tkinter.messagebox.showinfo("Does not exist", "This record does not exist")

    # This definition is used to search the database using the ID obtained from a QR code.

    def checkdbqr(self, *args, **kwargs):

        # Get the products info and id and fill the labels

        query = "SELECT name, type, vendor, stock, date, dateofproduction FROM inventory WHERE id=?"
        result = c.execute(query, (self.get_id,))

        for self.r in result:
            self.get_name = self.r[0]
            self.get_type = self.r[1]
            self.get_vendor = self.r[2]
            self.get_stock = self.r[3]
            self.get_date = self.r[4]
            self.get_proddate = self.r[5]

        self.productname.configure(text="Product name: " + str(self.get_name))
        self.producttype.configure(text="Type: " + str(self.get_type))
        self.productvendor.configure(text="Vendor: " + str(self.get_vendor))
        self.productdate.configure(text="Date of Manufacture: " + str(self.get_date))
        self.productdateofp.configure(text="Date of Manufacture: " + str(self.get_proddate))
        self.productstock.configure(text="Amount in stock: " + str(self.get_stock))

    # This is used to open the camera and search for IDS in the current frame.

    def check_for_qr(self, *args, **kwargs):

        # Very Important! ⬇

        # This variable is used to capture video. when cv2.VideoCapture() has a '0' it is representing using a external
        # camera set this to '1' to use a laptop camera or some kind of internal camera. It can be unwieldy at times so
        # try 0 and 1.

        cap = cv2.VideoCapture(1)

        # Very Important! ⬆

        font = cv2.FONT_HERSHEY_PLAIN
        idqr = 0
        while True:
            _, frame = cap.read()

            decodedObjects = pyzbar.decode(frame)
            for obj in decodedObjects:
                dataString = obj.data.decode("utf-8")
                dataString = re.sub('[''b]', '', dataString)
                cv2.putText(frame, str(dataString), (50, 50), font, 3, (255, 0, 0), 3)
                self.get_id = dataString

            cv2.imshow("Scanning for QR Codes in frame", frame)
            key = cv2.waitKey(1)
            if key == 27:
                self.checkdbqr
                break
                cv2.destroyAllWindows()
                cv2.VideoCapture.release()

root = Tk()
b = Application(root)

root.geometry("800x400+0+0")
root.title("Search The Database")
root.mainloop()
