import socket
import sys
from socket import *

def query():
    sock = socket.socket()
    TCP_IP = '127.0.0.1'
    TCP_PORT = 40024
    BUFFER_SIZE = 1024
    socket.bind((TCP_IP,TCP_PORT))
    sock.listen(10)
    while True:
        sc, addr = sock.accept()
        file = open('FrontSquat.mp4','wb')
        while True:
            file.write(sf)
            sf = sc.recv(BUFFER_SIZE)
        file.close()
        sc.close()

    sock.close()
