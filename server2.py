import socket
from datetime import datetime
HOST= "172.16.0.188"
PORT = 6789
max_size=1024
sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
sock.bind((HOST,PORT)) #open server
print('Starting The Server at: ', datetime.now())
print("Waiting For The Incoming Connection from client")
sock.listen(5) #listening client
client, addr = sock.accept()  #client connect
while True:
    data = client.recv(max_size)   #recieve from client
    if data.decode('utf-8') == 'q': #decode message
        break
    print("At ", datetime.now(),addr, " said: ", data.decode('utf-8'))
    message_to_client = input("Enter message to client: ")   #input message
    message_to_client_encode = message_to_client.encode('utf-8') #encode message
    client.send(message_to_client_encode)    #send to client back
    if message_to_client == 'q':
        break

client.close()
sock.close() 