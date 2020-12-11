import socket
import sys


serverAddressPort   = ("127.0.0.1", 20001)
bufferSize          = 1024

# Create a UDP socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

print("Welcome to Client-Server Chat Room\n")

while True:
	data = input("You: ")
	UDPClientSocket.sendto(data.encode(), serverAddressPort)
	if data == "quit":
		break
	
	data = UDPClientSocket.recvfrom(bufferSize)
	print('Server: ' , data[0].decode())
	if data[0].decode() == "quit":
		break


print('You are no longer in the Chat Room')
UDPClientSocket.close()


