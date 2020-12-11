import socket
import sys

localIP = "127.0.0.1"
localPort = 20001
bufferSize = 1024

# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and ip
UDPServerSocket.bind((localIP, localPort))

print("Welcome to Client-Server Chat Room")
print("UDP server listening")
print("Waiting for Client...")

# Listen for incoming datagrams

while True:
	(message, address) = UDPServerSocket.recvfrom(bufferSize)
	clientIP  = format(address)

	print("Client: " + message.decode())
	if message.decode() == "quit":	
		break

	message = input("You: ")

	UDPServerSocket.sendto(message.encode(), address)

	if message == "quit":	
		break



UDPServerSocket.close()
print("Chat Room Closed.")


