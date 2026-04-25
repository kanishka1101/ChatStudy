import socket
import threading

HOST = '127.0.0.1'   # Localhost
PORT = 12345

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []
names = []

print("Server started... Waiting for connections...")

def broadcast(message):
    for client in clients:
        try:
            client.send(message)
        except:
            pass

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            if not message:
                break
            broadcast(message)
        except:
            break

    # Remove client if disconnected
    if client in clients:
        index = clients.index(client)
        name = names[index]

        clients.remove(client)
        names.remove(name)
        client.close()

        print(f"{name} disconnected")
        broadcast(f"{name} left the chat!".encode('utf-8'))

def receive():
    while True:
        client, address = server.accept()
        print(f"Connected with {address}")

        client.send("NAME".encode('utf-8'))
        name = client.recv(1024).decode('utf-8')

        names.append(name)
        clients.append(client)

        print(f"Username: {name}")
        broadcast(f"{name} joined the chat!".encode('utf-8'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

receive()
