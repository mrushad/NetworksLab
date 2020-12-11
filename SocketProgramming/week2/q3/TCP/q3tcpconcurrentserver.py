import threading
import socket

sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(('localhost',10000))
sock.listen()

clients = []
client_names = []

def recieve(client):
    while True:
        try:
            data=client.recv(1024)
            for x in clients:
                x.send(data)
        except:
            i = clients.index(client)
            clients.remove(client)
            client.close()
            data = f'{client_names[i]} has quit'.encode("utf-8")
            for x in clients:
                x.send(data)
            client_names.remove(client_names[i])
            break

def start():
    while True:
        client,address=sock.accept()
        print(f"Client {address} has joined")
        client.send("name".encode('utf-8'))
        cname=client.recv(1024).decode('utf-8')
        client_names.append(cname)
        clients.append(client)
        data = f"{cname} has joined".encode('utf-8')
        for x in clients:
            x.send(data)
        client.send('\nYou are connected'.encode('utf-8'))

        thread=threading.Thread(target=recieve,args=(client,))
        thread.start()

print("\nWaiting for clients to join...")

start()
