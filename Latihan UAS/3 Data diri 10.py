from tkinter import Tk, Label, Entry, Button, StringVar
from tkinter import messagebox

my_app = Tk(className = "Data diri")

L1= Label(my_app, text="Nama Lengkap")
L1.grid(row=0, column=0, sticky="w")

S1= StringVar()
E1= Entry(my_app, textvariable = S1)
E1.grid(row=0, column=1)

L2= Label(my_app, text="Nim")
L2.grid(row=1, column=0, sticky="w")

S2= StringVar()
E2= Entry(my_app, textvariable = S2)
E2.grid(row=1, column=1)

L3= Label(my_app, text="Kota Asal")
L3.grid(row=2, column=0, sticky="w")

S3= StringVar()
E3= Entry(my_app, textvariable = S3)
E3.grid(row=2, column=1)

L4= Label(my_app, text="Status")
L4.grid(row=3, column=0, sticky="w")

S4= StringVar()
E4= Entry(my_app, textvariable = S4)
E4.grid(row=3, column=1)

L5= Label(my_app, text="Jenis Kelamin")
L5.grid(row=4, column=0, sticky="w")

S5= StringVar()
E5= Entry(my_app, textvariable = S5)
E5.grid(row=4, column=1)

def simpan():
    """Menyimpan semua data yang sudah tersimpan"""
    klik="Nama Lengkap = "+S1.get()+"\n"+"Nim = "+ S2.get()+"\n"+"Kota Asal = "+ S3.get()+"\n"+"Status = "+ S4.get()+"\n"+"Jenis Kelamin = "+ S5.get()
    messagebox.showinfo("Data diri", klik)

def reset():
    """Menghapus semua data yang sudah dimasukkan"""
    S1.set("")
    S2.set("")
    S3.set("")
    S4.set("")
    S5.set("")

B1= Button(my_app, text="Simpan", command = simpan)
B1.grid(row=5, column=1)

B2= Button(my_app, text="Reset", command = reset)
B2.grid(row=5, column=0)

my_app.mainloop()
