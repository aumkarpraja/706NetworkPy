import socket




def response(num):
# Set up route to Client -> LocalDNS
	UDP_IP = "127.0.0.1"
	UDP_PORT = 40020
	MESSAGE = num
	print "[DEBUG] Sending message to localDNS of video selected."
	# Create socket and send through socket, close after
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP	
	sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
	sock.close()
	print "[DEBUG] hisCinemaDNS idle. Closing."

def response2():
	UDP_IP = "127.0.0.1"
	UDP_PORT = 40020
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
	sock.bind((UDP_IP, UDP_PORT))
	while True:
	    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
	    print "received message:", data