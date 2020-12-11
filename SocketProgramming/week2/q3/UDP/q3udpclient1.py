import threading
import socket

client_name=input("Enter nickname: ")
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)


def recieve():
    while True:
        try:
            data = sock.recv(1024).decode('utf-8')    
            print(data)
        except:
            print("Error has occured")
            break

def send():
    while 1:
        data = input("")
        message = f'{client_name}: {data}'
        sock.sendto(message.encode('utf-8'),('localhost',10000))

print("\nYou are connected")
recieve_thread=threading.Thread(target=recieve)
recieve_thread.start()
send_thread=threading.Thread(target=send)
send_thread.start()
