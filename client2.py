import socket
from datetime import datetime
HOST= "172.20.10.4"
PORT = 6789
max_size=1024
print("Starting the client at: ", datetime.now())
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))
while True:
    message_to_server = input("Enter message to server: ")
    message_to_server_encode = message_to_server.encode('utf-8')
    s.send(message_to_server_encode)
    data = s.recv(max_size)
    print("At ", datetime.now(), "server replied with", data.decode('utf-8'))
s.close()