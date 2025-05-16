import tkinter as tk
from tkinter import Listbox, Button
from tkinter.constants import ANCHOR

top=tk.Tk()
lb=Listbox(top)
lb.insert(1,"USA")
lb.insert(2," india")
lb.insert(3,"mercury")
lb.pack()
btn=tk.Button(top,text="show",command=lambda lb.delete(ANCHOR))
btn.pack()
top.mainloop()











