import socket

TCP_IP = '127.0.0.1' #change to socket.gethostname()
TCP_PORT = 5005 #change to 40022

BUFFER_SIZE = 1024
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((TCP_IP,TCP_PORT))
sock.listen(1)

conn, addr = sock.accept()
print 'Connection addresses: ', addr

while 1:
    data = conn.recv(BUFFER_SIZE)
    if not data: break
    print 'Recieved data: ', data
    conn.send(data)
conn.close()
