import socket
from socket import *


UDP_IP = "127.0.0.1"
UDP_PORT = 40022
BUFFER_SIZE = 1024
Msg = '{127.0.0.1,A}'
sock = socket(AF_INET, SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(BUFFER_SIZE)
    print '[Recieved] ', data
    if not data: break
    sock.sendto(Msg,addr)
sock.close
