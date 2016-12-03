import socket

UDP_IP = socket.gethostbyname(socket.gethostname())
UDP_PORT = 40020
MESSAGE = "HELLO WORLD"
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # INTERNET, UDP
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))