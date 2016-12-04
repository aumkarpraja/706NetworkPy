import socket
from socket import *

UDP_IP = '127.0.0.1'
UDP_PORT = 40027
lDNSdata = ""
while True:
	print "[DEBUG] Awaiting localDNS to send response"
	sock = socket(AF_INET, SOCK_DGRAM) # UDP
	sock.bind((UDP_IP, UDP_PORT))
	while True:
	    lDNSdata, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
	    print "received message:", lDNSdata
	    break;
	
	print "[DEBUG] Now preparing download."
	
	TCP_IP = '127.0.0.1'
	TCP_PORT = 40025
	BUFFER_SIZE = 1024
	
	s = socket(AF_INET, SOCK_STREAM)
	s.connect((TCP_IP, TCP_PORT))
	s.send(lDNSdata)
	file = open('recv.mp4','wb')
	print "[DEBUG] Awaiting to recieve"
	data = s.recv(BUFFER_SIZE)
	
	while (data):
		print "Receiving..."
		file.write(data)
		data = s.recv(1023)
	file.close()
	print "[DEBUG] Done Receiving"
	s.close()                # Clos
#print data
