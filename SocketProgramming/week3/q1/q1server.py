import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
print("Starting up on " , server_address)
sock.bind(server_address)

print("Welcome!")
print("Waiting for Client...")
# Listen for incoming connections
sock.listen(1)


# Wait for a connection
connection, client_address = sock.accept()

print("Connected.\n")

while True:
	data = connection.recv(4096)
	print("Client: " + data.decode())
	if data.decode() == "Bye":
		data = "Bye"
	else:
		data = data.decode().upper()

	connection.sendall(data.encode())
	print("You: " + data)
	if data == "Bye":
		break


sock.close()
print("Connection Closed.")
