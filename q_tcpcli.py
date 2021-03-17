#nama berkas: p_tcpcli.py
#client tcp umtuk server

import socket

hostname= 'localhost'
pesan=''

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((hostname, 50002))
print "Mesin penjawab otomatis sudah siap"
while pesan.lower() != 'q':
    pesan = raw_input("Pertanyaan: ")
    s.send(pesan)
    if pesan.lower() != 'q':
        response= s.recv(1024)
        print 'Jawaban: ', response
    s.close()
