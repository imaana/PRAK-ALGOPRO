#Program Akun
#Dibuat oleh Afifah Ghaisani Imana L200190198

import random
angka = random.randint(0,1000)

Nama = "Afifah Ghaisani Imana"
TanggalLahir = "08 Februari 2000"
NamaSingkat = Nama[0]+". "+Nama[7]+". "+Nama[16:21]
Username = Nama[0]+TanggalLahir[0:2]+TanggalLahir[12:17]
Password = Nama[:6]+str(angka)

print(Nama)
print(TanggalLahir)
print(NamaSingkat)
print(Username)
print(Password)
