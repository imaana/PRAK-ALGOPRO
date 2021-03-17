from tkinter import Tk, Label, Entry, Button, StringVar
from tkinter import messagebox

my_app = Tk(className = "Menampilkan Data Diri")

L=Label(my_app, text ="Data diri", font=("Arial", 14))
L.grid(row=0, sticky='W', column=0)

L1= Label(my_app, text = "Nama")
L1.grid(row=1, sticky='W', column=0)

L1= Label(my_app, text = "Afifah Ghaisani Imana")
L1.grid(row=1, sticky='W' ,column=1)


L2= Label(my_app, text = "Nim")
L2.grid(row=2, sticky='W', column=0)

L2= Label(my_app, text = "L200190198")
L2.grid(row=2, sticky='W' ,column=1)


L3= Label(my_app, text = "Buku Favorit")
L3.grid(row=3, sticky='W', column=0)

L3= Label(my_app, text = "Misykat")
L3.grid(row=3, sticky='W', column=1)


L4= Label(my_app, text = "Idola di Kalangan Sahabat")
L4.grid(row=4, sticky='W', column=0)

L4= Label(my_app, text = "Muhammad Al-Fatih")
L4.grid(row=4, sticky='W', column=1)


L5= Label(my_app, text = "Motto")
L5.grid(row=5, sticky='W', column=0)

L5= Label(my_app, text = "Istiqomah")
L5.grid(row=5, sticky='W', column=1)

def info():
    my_app.destroy()

B1= Button(my_app, text= "Tutup", command = info)
B1.grid(row=6, column=1)


