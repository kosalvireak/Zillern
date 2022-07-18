# Client ard server send and receive forever until both of them type 'q'
# The time also being record everytime they send/receive

import socket
from datetime import datetime
HOST= "172.16.2.87"
PORT = 6789
max_size=1024
print("Starting the client at: ", datetime.now())
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)                    #start socket
s.connect((HOST,PORT))                                                  #connect to server
while True:
    message_to_server = input("Enter message to server: ")              #input message
    message_to_server_encode = message_to_server.encode('utf-8')        #encode input message
    s.send(message_to_server_encode)                                    #send to server
    data = s.recv(max_size)                                             #receive from server
    print("At ", datetime.now(), "server replied with: ", data.decode('utf-8')) #print it out
s.close()