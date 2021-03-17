
import socket                   # Import socket module

hostname= 'localhost'
pesan=''

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((hostname, 50001))
with open('received_file', 'wb') as f:
    print 'Mengirim berkas melalui protocol TCP\nNama berkas : L200190198.txt'
    while True:
        print('mengirim...')
        data = s.recv(1024)
        print('data=%s', (data))
        if not data:
            break
        # write data to a file
        f.write(data)

f.close()
print('Successfully get the file')
s.close()
print('connection closed')
