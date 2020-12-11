import socket
import sys
from datetime import datetime

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 10000)
print('Starting up on ' , server_address)
sock.bind(server_address)

sock.listen(1)

while True:
	print('Waiting for client...')
	connection, client_address = sock.accept()

	try:
		print('Connected to client ' , client_address)

		while True:
			data = connection.recv(4096)
			print('Request received: ' , data.decode())
			now = datetime.now()
			date = now.strftime("%m/%d/%Y")
			print('Sending current date to client...')
			connection.sendall(str.encode(date))
			print('Sent.');
			break

		break

	finally:
		connection.close()
