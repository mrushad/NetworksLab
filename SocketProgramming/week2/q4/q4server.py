import threading
import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(('localhost',10000))
sock.listen()

print("Waiting for clients to join...")


def recieve(client):
    while True:
            msg=client.recv(1024).decode('utf-8')
            answer = eval(msg)
            client.send(f"Server: {answer}".encode('utf-8'))


while True:
    client,address = sock.accept()
    print(f"Client {address} has joined")
    client.send('Connected.'.encode('utf-8'))
    thread = threading.Thread(target=recieve,args=(client,))
    thread.start()

    
