# Client ard server send and receive forever until both of them type 'q'
# The time also being record everytime they send/receive

import socket
from datetime import datetime
HOST = "172.20.10.4"
PORT = 20000
max_size = 1024
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))  # open server
print('Starting The Server at: ', datetime.now())
print("Waiting For The Incoming Connection from client")
sock.listen(5)  # listening client
client, addr = sock.accept()  # client connect
filename = client.recv(max_size)  # receive file name
file = open(filename, "w")  # open file name
                                                
client.send("Filename received.".encode('utf-8'))   # tell client that you receive
while True:

    data = client.recv(max_size)  # receive from client
    data_decode = data.decode('utf-8')
    file.write(data_decode)
        # message_to_client = input("Enter message to client: ")  # input message
        # message_to_client_encode = message_to_client.encode(
        #     'utf-8')  # encode message
        # client.send(message_to_client_encode)  # send to client back
        # if message_to_client == 'q':
        #     break

client.close()
sock.close()
