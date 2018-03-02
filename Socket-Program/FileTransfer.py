import socket                   # Import socket module

s = socket.socket()             # Create a socket object
host = "*.*.*"     # Get local machine name
port = 8080                    # Reserve a port for your service.

s.connect((host, port))
s.sendall(bytes("file-transfer","UTF-8"))
with open('received_file', 'wb') as f:
    print('file opened')
    while True:
        print('receiving data...')
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
