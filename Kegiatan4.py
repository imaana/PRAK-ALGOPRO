Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> Nama="Afifah Ghaisani Imana"
>>> NIM=198
>>> Tinggi=1.59
>>> Berat=55
>>> TahunLahir=2000
>>> Aku=(TahunLahir, Berat, Tinggi, NIM, Nama)
>>> Data=[TahunLahir, Berat, Tinggi, NIM, Nama]
>>> type(Aku)
<class 'tuple'>
>>> #karena data didalam var Aku diapit oleh kurung buka dan kurung tutup yang menandakan data tersebut adalah tuple
>>> Aku[0]
2000
>>> #karena objek pertama yang disebut didalam var Aku adalah TahunLahir yang menyimpan data 2000
>>> a = NIM%4; Aku[a]
1.59
>>> #karena sisa bagi 198 oleh 4 adalah 2. kemudian yang tersimpan dalam var Aku urutan ke-2 adalah Tinggi yang menyimpan data 1.59
>>> type (Aku[a])
<class 'float'>
>>> #karena nilai dari 'Tinggi' adalah 1.59 yaitu bilangan desimal yang bertipe float
>>> Aku[a:4]
(1.59, 198)
>>> #karena Aku[a] adalah urutan dalam var Aku ke-2 hingga sebelum ke-4, yaitu Tinggi dan NIM yang mempunyai nilai 1.59 untuk Tinggi dan 198 untuk NIM
>>> type (Aku[4])
<class 'str'>
>>> #karena yang tersimpan pada var Aku urutan ke=4 adalah Nama yang bertipe string
>>> Aku[0]="ok"
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    Aku[0]="ok"
TypeError: 'tuple' object does not support item assignment
>>> #error karena data tuple tidak dapat dirubah isinya
>>> type(Data)
<class 'list'>
>>> #karena data dalam var Data diapit oleh kurung siku [] yang menandatang data tersebut adalah list
>>> type(Data[4])
<class 'str'>
>>> #karena yang tersimpan pada vae Data urutan ke-4 adalah var Nama yang bertipe string
>>> Data[4][5]
'h'
>>> #karena data pada var Data urutan ke-4 yaitu Nama, dan dalam var Nama urutan ke-5 yaitu huruf 'h'
>>> Data[4][a:6]
'ifah'
>>> #karena data pada var Data urutan ke-4 yaitu Nama, dan dalam var Nama urutan ke-a sampai sebelum urutan ke-6 yaitu 'ifah'
>>> Data[0]="ok"; Data
['ok', 55, 1.59, 198, 'Afifah Ghaisani Imana']
>>> #karena data bertipe list dapat dirubah isinya, Data urutan ke-0 diganti dengan string "ok", dan karena var Data disebut kembali di akhir, maka muncl semua data var yang sudah tersimpan di var Data
>>> Data [-a]
198
>>> #karena urutan list jika minus maka dibaca dari belakang, a bernilai 2 jadi urutan -2 atau kedua dari kanan yaitu NIM yang bernilai 198
>>> range(a)
range(0, 2)
>>> #karena a tadi bernilai 2, jadi range 0,2
