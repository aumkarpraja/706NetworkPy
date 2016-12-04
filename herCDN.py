import socket
import sys
from socket import *



TCP_IP = '127.0.0.1'
TCP_PORT = 40024
BUFFER_SIZE = 1024
sock = socket(AF_INET, SOCK_STREAM)
sock.bind((TCP_IP,TCP_PORT))
sock.listen(10)
while True:
    conn, addr = sock.accept()
    data = conn.recv(BUFFER_SIZE)
    if data == '1':
        file = open('FrontSquat.mp4','wb')
    if data == '2':
        file = open('FrontSquat.mp4','wb')

    while True:
        file.write(data)

    file.close()
    conn.close()

sock.close()
