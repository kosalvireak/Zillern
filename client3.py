import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('172.20.10.4',55055))
data = "Hello world\n"
sock.send(data.encode('utf-8'))
large_data = "He " * 2000
sock.send(large_data.encode('utf-8'))
