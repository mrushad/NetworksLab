import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print('Connecting to server ' , server_address)
sock.connect(server_address)
    
while True:
	data = sock.recv(4096)
	print('Server Message: ' , data.decode())
	break

print('closing socket')
sock.close()
