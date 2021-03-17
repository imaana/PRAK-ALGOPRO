from tkinter import Tk, Label, Entry, Button, StringVar
from tkinter import messagebox

my_app = Tk(className = "Akses terhadap properti widget")

L1= Label(my_app, text = "Angka 1")
L1.grid(row=0, column=0)

x= StringVar()
E1= Entry(my_app, textvariable = x)
E1.grid(row=0, column=1, columnspan=3)

L2= Label(my_app, text = "Angka 2")
L2.grid(row=1, column=0)

y= StringVar()
E1= Entry(my_app, textvariable=y)
E1.grid(row=1, column=1, columnspan=3)

def tambah():
    a= float(x.get())
    b= float(y.get())
    hasil=a+b
    L.config(text=hasil)

B1= Button(my_app, text= "+", command = tambah)
B1.grid(row=2, column=0)

def kurang():
    a= float(x.get())
    b= float(y.get())
    hasil=a-b
    L.config(text=hasil)

B1= Button(my_app, text= "-", command = kurang)
B1.grid(row=2, column=1)

def kali():
    a= float(x.get())
    b= float(y.get())
    hasil=a*b
    L.config(text=hasil)

B1= Button(my_app, text= "x", command = kali)
B1.grid(row=2, column=2)

def bagi():
    a= float(x.get())
    b= float(y.get())
    hasil=a/b
    L.config(text=hasil)

B1= Button(my_app, text= "/", command = bagi)
B1.grid(row=2, column=3)

A1=Label(my_app, text="Hasil")
A1.grid(row=3, column=0)
L=Label(my_app, text="0")
L.grid(row=3, column=3)

my_app.mainloop()
