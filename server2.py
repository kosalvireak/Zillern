#Client ard server send and receive forever until both of them type 'q'
# The time also being record everytime they send/receive

import socket
from datetime import datetime
HOST= "172.20.10.4"
PORT = 6789
max_size=1024
sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST,PORT))
print('Starting The Server at: ', datetime.now())
print("Waiting For The Incoming Connection from client")
sock.listen(5)
client, addr = sock.accept()
while True:
    data = client.recv(max_size)
    if data.decode('utf-8') == 'q':
        break
    print("At ", datetime.now(),addr, " said", data.decode('utf-8'))
    message_to_client = input("Enter message to client: ")
    message_to_client_encode = message_to_client.encode('utf-8')
    client.send(message_to_client_encode)
    if message_to_client == 'q':
        break

client.close()
sock.close()