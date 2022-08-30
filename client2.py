
import socket
from datetime import datetime
HOST = "172.20.10.4"
PORT = 6789
max_size = 1024

FORMAT = "utf-8"
print("Starting the client at: ", datetime.now())
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # start socket
client.connect((HOST, PORT))
print("""q : for close connection
on : for turn a light on
off: for turn a light off
        """)  # connect to server
while True:
    # message_to_server = input("Enter message to server: ")              #input message
    # message_to_server_encode = message_to_server.encode('utf-8')        #encode input message
    # s.send(message_to_server_encode)                                    #send to server
    data = client.recv(max_size)  # receive from server
    if data.decode('utf-8') == 'on':
        # led_server.on()
        print("light is on")
    elif data.decode('utf-8') == 'off':
        # led_server.off()
        print("light is off")
    print("At ", datetime.now(), "server replied with: ",
          data.decode('utf-8'))  # print it out
    if data.decode('utf-8') == 'q':
        break

f = open("/home/pi/Desktop/Light sensor.txt", "r")
data = f.read()
client.send("Light sensor.txt".encode(FORMAT))
msg = client.recv(max_size).decode(FORMAT)
print(f"server: {msg}")
client.send(data.encode(FORMAT))
msg = client.recv(max_size).decode(FORMAT)
print(f"server: {msg}")
f.close()
client.close()
