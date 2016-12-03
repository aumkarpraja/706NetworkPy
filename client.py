import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 40022
DATA = 'hello world'
BUFFER_SIZE = 80
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((TCP_IP,TCP_PORT))
sock.send(DATA)
data = sock.recv(BUFFER_SIZE)
sock.close()

print 'Recieved data: ', data
