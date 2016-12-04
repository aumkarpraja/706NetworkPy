from socket import *

UDP_IP = "127.0.0.1"
UDP_PORT = 40020

sock = socket(AF_INET, SOCK_DGRAM) 
sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
sock.bind((UDP_IP, UDP_PORT))

videoNum = ""

# Wait for response from DNS
while True:
    videoNum, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print "Selected: ", videoNum
    break;

	
print "[DEBUG] Socket closed."
sock.close()

UDP_PORT = 40021
sock = socket(AF_INET, SOCK_DGRAM) # UDP
sock.sendto("V: " + videoNum, (UDP_IP, UDP_PORT))
print "[DEBUG] V flag sent to hisCinemaDNS"
sock.close()
print "[DEBUG] Socket closed. again."

UDP_PORT = 40020
sock = socket(AF_INET, SOCK_DGRAM) # UDP
sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
sock.bind((UDP_IP, UDP_PORT))
print "[DEBUG] Waiting for IP of herCDNDNS"
while True:
    IPadd, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print "received IP:", IPadd
    break;
sock.close()
print "[DEBUG] Socket closed. again. Recived message from hisCinemaDNS"