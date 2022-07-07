# If The data that client send is bigger then the maxsize(1024)

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('172.20.10.4',55055))
s.listen(5)
client, addr = s.accept()
data = client.recv(1024)
data_decode = data.decode('utf-8')
print(data_decode)
maxsize = 1024
fragments = []
while not done:
    chunk = client.recv(maxsize)
    if not chunk:
        break
    fragments.append(chunk)