from tkinter import Tk, Label, Entry, Button, StringVar
from tkinter import messagebox

my_app = Tk(className = "Coba")

L1=Label(my_app, text ="Nama ")
L1.grid(row=0, column=0, sticky="w")

L1=Label(my_app, text ="Nilai ")
L1.grid(row=0, column=1)

L1=Label(my_app, text ="Susi : ")
L1.grid(row=1, column=0, sticky="w")

x=StringVar()
E1=Entry(my_app, textvariable = x)
E1.grid(row=1, column=1, columnspan=3)

L2=Label(my_app, text ="Bambang : ")
L2.grid(row=2, column=0, sticky="w")

y=StringVar()
E2=Entry(my_app, textvariable = y)
E2.grid(row=2, column=1, columnspan=3)

def klik():
    buka=x.get()
    buka2=y.get()
    berkas=open("baru.txt", "w")
    berkas.write("Nama   "+"   Nilai\n")
    berkas.write("Susi    : "+buka+"\n")
    berkas.write("Bambang : "+buka2)
    berkas.close()
    
B1=Button(my_app, text="Simpan",command = klik)
B1.grid(row=3, column=1)

my_app.mainloop()


