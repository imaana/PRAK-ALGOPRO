from tkinter import Tk, Label, Entry, Button, StringVar
from tkinter import messagebox

my_app = Tk(className = "Akses terhadap properti widget")

L1= Label(my_app, text = "Nama Mahasiswa")
L1.grid(row=0, column=0)

str1= StringVar()
E1= Entry(my_app, textvariable = str1)
E1.grid(row=0, column=1)

L2= Label(my_app, text = "Umur")
L2.grid(row=1, column=0)

str2= StringVar(value=0)
E1= Entry(my_app, textvariable=str2)
E1.grid(row=1, column=1)

def info():
    """Mengambil data pada entry E1 dan E2, dan menampilakannya dengan messagebox"""
    info= str1.get() +" berumur " + str2.get() + " tahun"
    messagebox.showinfo("Pesan", info)

def hapus():
    """Menghapus text di entry E1 dan E2"""
    str1.set("") #menulis ke entry1 dengan string kosong
    str2.set(0)#menulis ke entry2 dengan 0

B1= Button(my_app, text= "Informasi", command = info)
B1.grid(row=2, column=1)

B2= Button(my_app, text= "Clear", command = hapus)
B2.grid(row=2, column=0)

my_app.mainloop()
