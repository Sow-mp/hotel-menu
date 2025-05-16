import sqlite3
import tkinter as tk

from reverse import status_label

conn=sqlite3.connect("users.db")
cursor=conn.cursor()
cursor.execute(''' create table if not exists users(
id integers primary key auto increment,
)''')
cursor.commit()
 def save_data():
     name=e1.get()
     email=e2.get()
     password=e3.get()

   if name and email and password:
      cursor.execute(" user(a)values(),(name,email,password)")
      conn.commit()
      status_label.config(text=" ",fg="red")
   else:
       status_label.config(text=" ",fg=" ")

 top=tk.Tk()

 top.mainloop()
 conn.close()

