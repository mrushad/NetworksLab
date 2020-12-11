import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print("Connecting to Server: " , server_address, "...")
sock.connect(server_address)

print("Welcome!\n")

while True:
	data = input("You: ")
	sock.sendall(data.encode())
	if data == "quit":
		break

print('Connection Closed.')
sock.close()
