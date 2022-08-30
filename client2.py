import socket
#from gpiozero import LED
from datetime import datetime
HOST = "172.16.0.188"
PORT = 6789
max_size = 1024
#led_server = LED(27)
FORMAT = "utf-8"
print("Starting the client at: ", datetime.now())
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # start socket
client.connect((HOST, PORT))
print("""q : for close connection
on : for turn a light on
off: for turn a light off
        """)  
while True:                        
    data = client.recv(max_size) 
    if data.decode('utf-8') == 'on':
        # led_server.on()
        print("light is on")
    elif data.decode('utf-8') == 'off':
        # led_server.off()
        print("light is off")
    print("At ", datetime.now(), "server replied with: ",
          data.decode('utf-8'))  
    if data.decode('utf-8') == 'q':
        break

f = open("Light sensor.txt", "r")
# f = open("/home/pi/Desktop/Light sensor.txt", "r")
data = f.read()
client.send("Light sensor.txt".encode(FORMAT))
msg = client.recv(max_size).decode(FORMAT)
print(f"server: {msg}")
client.send(data.encode(FORMAT))
msg = client.recv(max_size).decode(FORMAT)
print(f"server: {msg}")
f.close()
client.close()

