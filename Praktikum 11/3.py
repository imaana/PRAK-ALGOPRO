from tkinter import Tk, Label, Entry, Button
from tkinter import messagebox

my_app = Tk(className = "Aplikasi dengan beberapa widget")

L1= Label(my_app, text = "Nama Mahasiswa")
L1.grid(row=0, column=0)

E1= Entry(my_app)
E1.grid(row=0, column=1)

L2= Label(my_app, text = "NIM")
L2.grid(row=1, column=0)

E1= Entry(my_app)
E1.grid(row=1, column=1)

def tampil_pesan():
    messagebox.showinfo("Pesan", "Hello World")

B= Button(my_app, text= "Hello", command = tampil_pesan)
B.grid(row=2, column=1)

my_app.mainloop()
