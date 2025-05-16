from tkinter import *
import sqlite3

# Database connection and table creation
conn = sqlite3.connect("users.db")
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    email TEXT,
                    password TEXT)''')
conn.commit()

conn=sqlite3.connect("users.db")
cursor=conn.cursor()
cursor.execute('''(id integer )''')
conn.commit()
# Function to store data in the database
def save_data():
    name = e1.get()
    email = e2.get()
    password = e3.get()
if name and email and password:

    cursor.execute("insert into users() values()",(name,email,password))
    cursor.comm
    if name and email and password:
        cursor.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)", (name, email, password))
        conn.commit()
        status_label.config(text="Data Saved Successfully!", fg="green")
    else:
        status_label.config(text="All fields are required!", fg="red")

# Tkinter UI
top = Tk()
top.geometry("400x250")
top.title("User Registration")

Label(top, text="Name").place(x=30, y=50)
Label(top, text="Email").place(x=30, y=90)
Label(top, text="Password").place(x=30, y=130)

e1 = Entry(top)
e1.place(x=80, y=50)

e2 = Entry(top)
e2.place(x=80, y=90)

e3 = Entry(top, show="*") # Hides password input
e3.place(x=95, y=130)

Button(top, text="Submit", activebackground="pink", activeforeground="blue", command=save_data).place(x=30, y=170)

status_label = Label(top, text="", fg="red")
status_label.place(x=30, y=200)

top.mainloop()

# Close the database connection when the window is closed
conn.close()
