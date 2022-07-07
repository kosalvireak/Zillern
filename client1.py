#The server and client just connect and send & reply 1 message

import socket
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
port = 55055
sock.connect(('172.20.10.4',port))
msg = sock.recv(1024)
msg_decode = msg.decode('utf-8')
print('Message from server'+msg_decode)
msg_back = input('Do you want to respone to the serve ? ')
msg_back_encoded = msg_back.encode('utf-8')
sock.send(msg_back_encoded)
sock.close()