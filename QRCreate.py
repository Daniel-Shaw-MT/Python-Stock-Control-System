
# imports
import os
import sqlite3
import qrcode

# imports


# This program generates QR codes for the SearchDB.py class to read.
# These are to be printed and stuck to the object with the corresponding id
# --------Settings--------
current_directory = os.getcwd()
conn = sqlite3.connect(current_directory+'/Databases/storefile.db')
c = conn.cursor()
# What id to use when generating
# This depends on what current ID the database is on
print("What ID do you need to generate: ")
id = input()


def gen():
    query = "SELECT name FROM inventory WHERE id=?"
    result = c.execute(query,  (id))

    for r in result:
        get_name = r[0]



# This is the name of file

    nameoffile = str(get_name)

# What directory to use.

    directory = current_directory + "/QRCodes/"

# Generating the QR Code. Done by qrcode package
    qr = qrcode.make(id)
    qr.save(directory+nameoffile+'.png')

# --------- Settings --------
gen()