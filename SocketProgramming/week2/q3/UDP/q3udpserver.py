import threading
import socket

sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind(('localhost',10000))
clients=[]

def start():
    while 1:
        data,address = sock.recvfrom(1024)
        if address not in clients:
            clients.append(address)
            print(f"Client {address} has connected")
        for x in clients:
            sock.sendto(data,x)


print("Waiting for clients to join...")

start()

    
