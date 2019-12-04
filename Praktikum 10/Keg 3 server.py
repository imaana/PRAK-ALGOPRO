
import socket

hostname= 'localhost'
pesan=''

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("",50002))
s.listen(5)
print "Server penjawab otomatis sudah siap"
perintah=''
sisi=0
while perintah != 'keluar':
    komm, addr = s.accept()
    while perintah != 'keluar':
        item = komm.recv(1024).lower().split("=")
        perintah = item [0]
        if perintah == 'keluar':
            komm.send('done')
            s.close()
            break

        print 'Pesan: ', perintah
        if len(item)==2:
            if perintah == 'sisi':
                sisi=int(item[1])
                komm.send('Sisi disimpan')
            else:
                komm.send('Pesan tidak diketahui')
        elif perintah == 'hitung':
            L=float(sisi*sisi)
            response = 'Luas Persegi dengan sisi {} adalah {}'.format(sisi,L)
            komm.send(response)
        else:
            komm.send('Pesan tidak diketahui')
            
