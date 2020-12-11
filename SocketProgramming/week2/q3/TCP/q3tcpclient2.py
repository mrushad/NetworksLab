import threading
import socket

your_name=input("Enter nickname: ")
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

sock.connect(('localhost',10000))

def recieve():
    while True:
        try:
            data = sock.recv(1024).decode('utf-8')
            if data == "name":
                sock.send(your_name.encode('utf-8'))
            else:
                print(data)
        except:
            print("Error has occured")
            sock.close()
            break

def send():
    while True:
        data=input("")
        message = f'{your_name}: {data}'
        sock.send(message.encode('utf-8'))

receive_thread=threading.Thread(target=recieve)
receive_thread.start()
send_thread=threading.Thread(target=send)
send_thread.start()


