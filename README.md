# 📚 Library Management System

A desktop GUI application to manage books, members, and book issue records
for a library. Built with Python Tkinter and MySQL.

---

## 📌 About The Project

This project provides a complete library management solution with a clean
graphical interface. Librarians can add books, register members, issue and
track books, and search the collection — all from a simple desktop application.

---

## ✨ Features

- 📖 Add and manage books with author and page details
- 👤 Register and manage library members
- 📋 Issue books to members with date tracking
- 🔍 Search books by name
- 📊 View all books and their availability status
- 🔐 Login system for secure access

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Core programming language |
| Tkinter | Desktop GUI framework |
| MySQL | Database for storing records |
| mysql-connector-python | Python-MySQL connection |

---

## ⚙️ How To Run

**Step 1 — Install required library:**
```bash
pip install -r requirements.txt
```

**Step 2 — Set up MySQL database:**

Open MySQL and run the `database.sql` file:
```bash
mysql -u root -p < database.sql
```
Or open MySQL Workbench and run the SQL commands manually.

**Step 3 — Update your MySQL password:**

Open `main.py`, `books.py`, `members.py`, and `issuebook.py`
Find this line in each file and replace `yourpassword` with your actual MySQL password:
```python
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="yourpassword",   # ← change this
    database="LMS"
)
```

**Step 4 — Run the application:**
```bash
python main.py
```

---

## 📁 Project Structure

```
library-management-system/
├── main.py           # Main application window
├── books.py          # Add book window
├── members.py        # Add member window
├── issuebook.py      # Issue book window
├── database.sql      # MySQL database setup
└── requirements.txt  # Required Python libraries
```

---

## 🖥️ How It Works

1. Login with username and password to access the system
2. Main window shows all books and a search bar
3. Click **Add Book** to add a new book to the library
4. Click **Add Member** to register a new library member
5. Click **Issue Book** to issue a book to a member
6. Click any book to see its details and availability status

---

## 🎓 About

Developed as part of M.Tech in Computer Science & Engineering
@ Anurag University, Hyderabad

**Author:** Aadhya MP
**GitHub:** [github.com/mpaadhya](https://github.com/mpaadhya)
