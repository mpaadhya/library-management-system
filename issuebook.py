from tkinter import *
import mysql.connector
import datetime

con = mysql.connector.connect(
host="localhost",
user="root",
password="yourpassword",
database="LMS"
)

cur = con.cursor()

class IssueBook:

    def __init__(self):

        self.window = Tk()

        self.window.title("Issue Book")

        Label(self.window,text="Book ID").grid(row=0)

        Label(self.window,text="Member ID").grid(row=1)

        self.bookid = Entry(self.window)

        self.memberid = Entry(self.window)

        self.bookid.grid(row=0,column=1)

        self.memberid.grid(row=1,column=1)

        Button(self.window,text="Issue",command=self.issue).grid(row=2,column=1)

        self.window.mainloop()

    def issue(self):

        book_id = self.bookid.get()

        member_id = self.memberid.get()

        today = datetime.date.today()

        cur.execute(
        "INSERT INTO issue(book_id,member_id,issue_date) VALUES(%s,%s,%s)",
        (book_id,member_id,today)
        )

        cur.execute(
        "UPDATE books SET book_status=1 WHERE book_id=%s",
        (book_id,)
        )

        con.commit()