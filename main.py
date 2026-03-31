import importlib
from tkinter import *
from tkinter import ttk
import mysql.connector

bookwindow = importlib.import_module('books')
memberwindow = importlib.import_module('members')
issuebookwindow = importlib.import_module('issuebook')

con = mysql.connector.connect(
host="localhost",
user="root",
password="yourpassword",
database="LMS"
)

cur = con.cursor()

class System:

    def __init__(self,master):

        self.master = master

        main_frame = Frame(master)
        main_frame.pack()

        top_frame = Frame(main_frame)
        top_frame.pack(fill=X)

        Button(top_frame,text="Add Member",command=self.new_member).pack(side=LEFT)
        Button(top_frame,text="Add Book",command=self.new_book).pack(side=LEFT)
        Button(top_frame,text="Issue Book",command=self.issue_book).pack(side=LEFT)

        centre_frame = Frame(main_frame)
        centre_frame.pack()

        left_frame = Frame(centre_frame)
        left_frame.pack(side=LEFT)

        self.management_box = Listbox(left_frame,width=40,height=25)
        self.management_box.pack()

        self.list_details = Listbox(left_frame,width=60,height=25)
        self.list_details.pack()

        self.management_box.bind('<<ListboxSelect>>',self.bookinfo)

        right_frame = Frame(centre_frame)
        right_frame.pack()

        Label(right_frame,text="Search Book").pack()

        self.ent_search = Entry(right_frame)
        self.ent_search.pack()

        Button(right_frame,text="Search",command=self.search).pack()

        self.showbooks()

    def showbooks(self):

        self.management_box.delete(0,END)

        cur.execute("SELECT * FROM books")

        books = cur.fetchall()

        for book in books:

            self.management_box.insert(END,str(book[0])+"-"+book[1])

    def bookinfo(self,evt):

        value = self.management_box.get(self.management_box.curselection())

        book_id = value.split('-')[0]

        cur.execute("SELECT * FROM books WHERE book_id=%s",(book_id,))

        book = cur.fetchone()

        self.list_details.delete(0,END)

        self.list_details.insert(END,"Book Name: "+book[1])
        self.list_details.insert(END,"Author: "+book[2])
        self.list_details.insert(END,"Pages: "+str(book[3]))

        if book[4]==0:
            self.list_details.insert(END,"Status: Available")
        else:
            self.list_details.insert(END,"Status: Issued")

    def search(self):

        value = self.ent_search.get()

        cur.execute("SELECT * FROM books WHERE book_name LIKE %s",('%'+value+'%',))

        books = cur.fetchall()

        self.management_box.delete(0,END)

        for book in books:

            self.management_box.insert(END,str(book[0])+"-"+book[1])

    def issue_book(self):

        issuebookwindow.IssueBook()

    def new_book(self):

        bookwindow.StoreBook()

    def new_member(self):

        memberwindow.StoreMember()

def base():

    root = Tk()

    root.title("Library Management System")

    root.geometry("1000x600")

    app = System(root)

    root.mainloop()

if __name__ == "__main__":

    base()