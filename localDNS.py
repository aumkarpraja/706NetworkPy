import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 40020

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
sock.bind((UDP_IP, UDP_PORT))

videoNum = ""

# Wait for response from DNS
while True:
    videoNum, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print "Selected: ", videoNum
    break;

	
print "[DEBUG] Socket closed."
sock.close()
	
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
sock.sendto("V: " + videoNum, (UDP_IP, UDP_PORT))
print "[DEBUG] V flag sent to hisCinemaDNS"


