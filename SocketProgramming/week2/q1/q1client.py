import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 10000)
print('Connecting to server ' , server_address, '...')
sock.connect(server_address)
print('Connected.')

try:
	message = 'Please send current date'
	print('Sending request message: ' , message)
	sock.sendall(message.encode())
	print('Sent')
	data = sock.recv(4096)
	print('Message Received.')
	print('Current Date: ' , data.decode())

finally:
	print('Closing socket')
	sock.close()
