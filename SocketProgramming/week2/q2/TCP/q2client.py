import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print("Connecting to Chat Room: " , server_address, "...")
sock.connect(server_address)

print("Welcome to Client-Server Chat Room\n")

while True:
	data = sock.recv(4096)
	print('Server: ' , data.decode())
	if data.decode() == "quit":
		break
	data = input("You: ")
	sock.sendall(data.encode())
	if data == "quit":
		break

print('You are no longer in the Chat Room')
sock.close()
