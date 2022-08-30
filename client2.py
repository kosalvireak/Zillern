
import socket
from datetime import datetime
HOST= "192.168.56.1"
PORT = 6789
max_size=1024
print("Starting the client at: ", datetime.now())
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)                    #start socket
s.connect((HOST,PORT))
print("""q : for close connection
on : for turn a light on
off: for turn a light off
        """)                                                  #connect to server
while True:
    message_to_server = input("Enter message to server: ")              #input message
    message_to_server_encode = message_to_server.encode('utf-8')        #encode input message
    s.send(message_to_server_encode)                                    #send to server
    data = s.recv(max_size)                                             #receive from server
    if data.decode('utf-8') == 'on': 
        #led.on()
        print("light is on")
    elif data.decode('utf-8') == 'off':
        #led.off()
        print("light is off")
    print("At ", datetime.now(), "server replied with: ", data.decode('utf-8')) #print it out
s.close()