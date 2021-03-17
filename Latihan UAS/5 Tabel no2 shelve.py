import shelve

F= open("coba.txt", "w")
nama= F.write("Nama     Nilai\n")
susi= F.write("Susi      : 69\n")
bambang= F.write("Bambang : 80")
F= shelve.open("oke.txt")
F.close()
