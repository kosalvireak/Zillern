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
while True:
    chunk = client.recv(maxsize)
    fragments.append(chunk)
    print(len(data_decode))
    if not chunk :
        break
        #chunk_decode = chunk.decode('utf-8')
    
#chunk_decode = chunk.decode('utf-8')
#print(chunk_decode)
print(fragments) 