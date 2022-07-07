import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('172.20.10.4',55055))
data = "Hello world"
sock.send(data.encode('utf-8'))