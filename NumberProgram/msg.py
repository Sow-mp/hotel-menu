import tkinter as tk
from tkinter import messagebox, LabelFrame

top=tk.Tk()
top.geometry()
messagebox.showinfo("infp ","fffjf")
lf1=LabelFrame(top,text="fhjb ")
lf1.pack(fill="both",expand="yes")
lf2=LabelFrame(top,text="fhjb ")
toplabel=tk.Label(lf1,text="ffb")
toplabel.pack()
lf2.pack(fill="both",expand="yes")
bottomlabel=tk.Label(lf2,text="ffb")
bottomlabel.pack()
spin = tk.Spinbox(top, from_= 0, to = 25)
top.mainloop()

