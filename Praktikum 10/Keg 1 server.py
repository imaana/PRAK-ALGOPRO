
import socket

hostname= 'localhost'
pesan=''

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("",50003))
s.listen(5)
print "Server penjawab otomatis sudah siap"
data=''
kamus={'nama': 'Afifah Ghaisani Imana', 'NIM' : 'L200190198', 'angkatan':'2019',
       'keluar' : 'siap!!'}
while data.lower() != 'keluar':
    komm, addr = s.accept()
    while data.lower() != 'keluar':
        data = komm.recv(1024)

        print 'Perintah: ', data
        if kamus.has_key(data):
            komm.send(kamus[data])
        else:
            komm.send('Maaf, perintah tidak dimengerti')
