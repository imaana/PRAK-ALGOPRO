from tkinter import Tk, Label, Entry
from tkinter import LEFT, RIGHT

my_app = Tk(className = "Applikasi dengan label") #title apps

L1 = Label(my_app, text = "Nama Mahasiswa")
L1.pack(side=LEFT)

E1 = Entry(my_app)
E1.pack(side = RIGHT)

my_app.mainloop()
