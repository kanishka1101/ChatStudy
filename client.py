import socket
import threading

HOST = '127.0.0.1'
PORT = 12345

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

name = input("Enter your name: ")

def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == "NAME":
                client.send(name.encode('utf-8'))
            else:
                print(message)
        except:
            print("Disconnected from server")
            client.close()
            break

def write():
    while True:
        try:
            msg = f"{name}: {input()}"
            client.send(msg.encode('utf-8'))
        except:
            break

thread1 = threading.Thread(target=receive)
thread1.start()

thread2 = threading.Thread(target=write)
thread2.start()
