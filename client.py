import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 40024
BUFFER_SIZE = 1024

# Step 1, send a request that you want the web page from hiscinema.com
MESSAGE = "GET"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(MESSAGE)

print "Sending..."

# Step 2 - Wait for data
while 1:
    c, addr = s.accept()     # Establish connection with client.
    print 'Got connection from', addr
    print "Receiving..."
    l = c.recv(1024)
    while (l):
        print "Receiving..."
        f.write(l)
        l = c.recv(1024)
f.close()
    print "Done Receiving"
    c.send('Thank you for connecting')
    c.close()                # Clos
    print l

print "Test"
