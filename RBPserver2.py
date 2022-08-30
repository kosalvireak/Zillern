import socket
from datetime import datetime
HOST = socket.gethostbyname(socket.gethostname())
PORT = 6789
SIZE = 1024
FORMAT = "utf-8"
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))  # open server
print('Starting The Server at: ', datetime.now())
print("Waiting For The Incoming Connection from client")
sock.listen(5)  # listening client
client, addr = sock.accept()  # client connect
print("""q : for close connection
on : for turn the light on
off: for turn the light off
        """)
while True:
    # data = client.recv(max_size)   #receive from client
    # if data.decode('utf-8') == 'q': #decode message
    #     break
    #print("At ", datetime.now(),addr, " said: ", data.decode('utf-8'))
    message_to_client = input("Enter message to client: ")  # input message
    message_to_client_encode = message_to_client.encode(
        'utf-8')  # encode message
    client.send(message_to_client_encode)  # send to client back
    if message_to_client == 'q':
        break

while True:

    filename = client.recv(SIZE).decode(FORMAT)
    print(f"[RECV] Receiving the filename.")

    file = open(filename, "a")
    client.send("Filename received.".encode(FORMAT))

    # Receiving the file data from the client. #
    data = client.recv(SIZE).decode(FORMAT)
    print(f"[RECV] Receiving the file data.")
    file.write(data)
    client.send("File data received".encode(FORMAT))

    # Closing the file. #
    file.close()

    # Closing the connection from the client. #
    client.close()
    print(f"[DISCONNECTED] {addr} disconnected.")
    break

sock.close()

import mysql.connector

dataBase = mysql.connector.connect(

    host="localhost",

    user="root",

    passwd="",

    database="kosalvireak"
)


cursorObject = dataBase.cursor()
f = open("Light sensor.txt","r")
for x in f:
    res = x.split()
    sql = "INSERT INTO tbl_STUDENT (NAME, EMAIL) VALUES (%s, %s)"
    val = (str(res[0]), str(res[1]))
    cursorObject.execute(sql, val)
    dataBase.commit()
