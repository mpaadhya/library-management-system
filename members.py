from tkinter import *
import mysql.connector

con = mysql.connector.connect(
host="localhost",
user="root",
password="yourpassword",
database="LMS"
)

cur = con.cursor()

class StoreMember:

    def __init__(self):

        self.window = Tk()

        self.window.title("Add Member")

        Label(self.window,text="Member Name").grid(row=0)

        Label(self.window,text="Phone").grid(row=1)

        self.name = Entry(self.window)

        self.phone = Entry(self.window)

        self.name.grid(row=0,column=1)

        self.phone.grid(row=1,column=1)

        Button(self.window,text="Add Member",command=self.addmember).grid(row=2,column=1)

        self.window.mainloop()

    def addmember(self):

        cur.execute(
        "INSERT INTO member(member_name,phone) VALUES(%s,%s)",
        (self.name.get(),self.phone.get())
        )

        con.commit()