import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 40024
BUFFER_SIZE = 1024
Message = '1'
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(Message)
file = open('recv.mp4','wb')

# Step 2 - Wait for data
while True:
    data = s.recv(BUFFER_SIZE)
    while (data):
        print "Receiving..."
        file.write(data)
file.close()
print "Done Receiving"
s.close()                # Clos
#print data
