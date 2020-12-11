import threading
import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect(('localhost',10000))

data = sock.recv(1024).decode('utf-8')
print(data)


while True:
    data = input("Enter Expression: ")
    sock.send(data.encode('utf-8'))
    data = sock.recv(1024).decode('utf-8')
    print(data)


