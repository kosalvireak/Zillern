import socket
from datetime import datetime
HOST= "192.168.56.1"
PORT = 6789
max_size=1024
sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
sock.bind((HOST,PORT)) #open server
print('Starting The Server at: ', datetime.now())
print("Waiting For The Incoming Connection from client")
sock.listen(5) #listening client
client, addr = sock.accept()  #client connect
print("""q : for close connection
on : for turn the light on
off: for turn the light off
        """)
while True:
    data = client.recv(max_size)   #receive from client
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