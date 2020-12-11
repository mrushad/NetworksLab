import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
print("Starting up on " , server_address)
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
	# Wait for a connection
	connection, client_address = sock.accept()
	data = 'Hello TCP Client'
	print("Sending Greeting to Client ", client_address, "...")
	connection.sendall(data.encode())
	print("Sent.")
	break

connection.close()
