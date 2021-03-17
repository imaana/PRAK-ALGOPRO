#SERVER
#impor modul socket
import socket
 
hostname= 'localhost'
pesan=''

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("",50001))
s.listen(5)
print 'TCP Server sudah siap\n Sedang menerima berkas ...'
print 'Berkas telah disimpan dengan nama : L200190198.txt'

while True:
    conn, addr = s.accept()     # Establish connection with client.
    print 'Got connection from', addr
    data = conn.recv(1024)
    print('Server received', repr(data))

    filename='TCPSERVER.py' #In the same folder or path is this file running must the file you want to tranfser to be
    f = open(filename,'rb')
    l = f.read(1024)
    while (l):
       conn.send(l)
       print('Sent ',repr(l))
       l = f.read(1024)
    f.close()

    print('Done sending')
    conn.send('Thank you for connecting')
    conn.close()
