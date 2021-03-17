from tkinter import Tk, Label, Entry, Button, StringVar
from tkinter import messagebox

my_app = Tk(className = "Akses terhadap properti widget")

Z=Label(my_app, text ="Bangun Geometri", font=("Arial", 14))
Z.grid(row=0, sticky='W', column=0)

Z=Label(my_app, text ="Nama Bangun")
Z.grid(row=1, sticky='W', column=0)

Z=Label(my_app, text =": Persegi.")
Z.grid(row=1, sticky='W', column=1)

Z=Label(my_app, text ="Dimensi (2D/3D)")
Z.grid(row=2, sticky='W', column=0)

Z=Label(my_app, text =": 2 Dimensi.")
Z.grid(row=2, sticky='W', column=1)

Z=Label(my_app, text ="Rumus Luas")
Z.grid(row=3, sticky='W', column=0)

Z=Label(my_app, text =": sisi x sisi")
Z.grid(row=3, sticky='W', column=1)

L1= Label(my_app, text = "Parameter 1 (sisi):")
L1.grid(row=4, column=0, sticky="W")

x= StringVar()
E1= Entry(my_app, textvariable = x)
E1.grid(row=4, column=1)

def hitung():
    a= float(x.get())
    hasil=a*a
    L.config(text=hasil)

B1= Button(my_app, text= "Hitung Luas", command = hitung)
B1.grid(row=5, column=0)


A1=Label(my_app, text="Luas =")
A1.grid(row=6, column=0)
L=Label(my_app, text="0")
L.grid(row=6, column=2)

my_app.mainloop()
