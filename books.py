from tkinter import *
import mysql.connector

con = mysql.connector.connect(
host="localhost",
user="root",
password="yourpassword",
database="LMS"
)

cur = con.cursor()

class StoreBook:

    def __init__(self):

        self.window = Tk()

        self.window.title("Add Book")

        Label(self.window,text="Book Name").grid(row=0)

        Label(self.window,text="Author").grid(row=1)

        Label(self.window,text="Pages").grid(row=2)

        self.name = Entry(self.window)

        self.author = Entry(self.window)

        self.pages = Entry(self.window)

        self.name.grid(row=0,column=1)

        self.author.grid(row=1,column=1)

        self.pages.grid(row=2,column=1)

        Button(self.window,text="Add Book",command=self.addbook).grid(row=3,column=1)

        self.window.mainloop()

    def addbook(self):

        cur.execute(
        "INSERT INTO books(book_name,author,pages) VALUES(%s,%s,%s)",
        (self.name.get(),self.author.get(),self.pages.get())
        )

        con.commit()