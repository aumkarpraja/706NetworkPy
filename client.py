import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 40024
BUFFER_SIZE = 1024

# Step 1, send a request that you want the web page from hiscinema.com
MESSAGE = "GET"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(MESSAGE)

# Step 2 - Wait for data
while 1:
    data = s.recv(BUFFER_SIZE)
    while (data):
        print "Receiving..."
        f.write(data)
f.close()
print "Done Receiving"
s.close()                # Clos
print data

