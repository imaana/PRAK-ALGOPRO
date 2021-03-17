def segitiga(a, t):
    luas = a*t*0.5
    return luas

def lingkaran(r):
    phi = 3.14
    luas = phi*r*r
    return luas

print("Selamat datang di program untuk menghitung luas")
print("-----------------------------------------------")
print("Menu Pilihan\n 1. Segitiga\n 2. Lingkaran\n 3. Keluar\n")
x=0
while x != "0":
    x=input("Masukkan Pilihan : ")
    if x =="1":
        print("Menghitung Luas Segitiga")
        a=int(input("Masukkan Alas : "))
        t=int(input("Masukkan Tinggi : "))
        print("Luas Segitiga adalah ", segitiga(a,t))
    elif x =="2":
        print("Menghitung Luas Lingkaran")
        r=int(input("Masukkan Jari-jari : "))
        print("Luas Lingkaran adalah ", lingkaran(r))
    elif x =="3":
        print("Keluar")
        break
