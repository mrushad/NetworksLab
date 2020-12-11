import socket
localIP = "127.0.0.1"
localPort = 20001
bufferSize = 1024
msgFromServer = "Hello UDP Client!"
bytesToSend = str.encode(msgFromServer)

# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and ip
UDPServerSocket.bind((localIP, localPort))

print("UDP server listening")

# Listen for incoming datagrams
while(True):
	(message, address) = UDPServerSocket.recvfrom(bufferSize)
	clientIP  = format(address)
	print("Sending Greeting to CLient" + clientIP + "...")
	# Sending a Greeting to client
	UDPServerSocket.sendto(bytesToSend, address)
	print("Sent.")
	break

UDPServerSocket.close()

