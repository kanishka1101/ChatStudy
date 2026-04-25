# Ex. No:1b 			Study of Client Server Chat Applications

## Aim: 
To perform a study on Client Server Chat Applications
## Introduction:
Client-server chat applications are a category of networked software that enables real-time communication between users over a network. This study explores the key components, architecture, and considerations in the development of client-server chat applications, highlighting their significance and common implementation practices.
Client-server chat applications are software systems that enable real-time communication between users over a network. These applications follow a client-server model, where one component (the server) manages connections and facilitates communication, while the other component (the client) interacts with the server to send and receive messages. Below are the fundamental aspects and components involved in the basics of client-server chat applications:
## 1. Client-Server Model:
•	Server:
•	The server is a central component that listens for incoming connections from clients.
•	It manages the communication channels and facilitates the exchange of messages between clients.
•	It may handle user authentication, message routing, and other core functionalities.
•	Client:
•	Clients are users or devices that connect to the server to participate in the chat.
•	Each client has a unique identity, often represented by a username.
•	Clients interact with the server to send and receive messages.
## 2. Communication Protocols:
•	Communication between clients and servers often relies on established protocols. The choice of protocol influences the behavior of the chat application.
•	TCP (Transmission Control Protocol):
•	Provides reliable, connection-oriented communication.
•	Ensures the ordered and error-free exchange of messages.

•	UDP (User Datagram Protocol):
•	Connectionless and operates in a best-effort mode.
•	Faster but may result in message loss or disorder.
## 3. Socket Programming:
•	Sockets:

•	Sockets serve as communication endpoints.
•	Each client and the server has a socket for sending and receiving data.

•	Functions:
•	Socket programming involves functions for creating, binding, listening, accepting connections, and sending/receiving data through sockets.
## 4. User Authentication:
•	For security and privacy, chat applications often implement user authentication mechanisms.
•	Users are required to provide credentials (e.g., username and password) to access the chat system.
•	More advanced methods like tokens or secure protocols can enhance authentication.
5. Message Routing:
•	The server is responsible for routing messages from one client to another.
•	It ensures that messages are delivered to the intended recipients.
•	Message routing may involve maintaining a list of connected users and their associated sockets.

## Architecture:
## Client-Server Model:
Client-server chat applications typically follow the client-server model, where one entity acts as the server, managing connections and facilitating communication, and one or more entities act as clients, initiating communication with the server.

## Communication Protocols:
The choice of communication protocol is crucial. Many chat applications use TCP (Transmission Control Protocol) for reliable, connection-oriented communication to ensure the ordered and error-free exchange of messages.
User Authentication:
User authentication mechanisms are essential to ensure secure and authorized access to the chat system. This can involve username-password authentication or more advanced methods like tokens.
## Components of Client-Server Chat Applications:
## Server-Side Components:

•	Socket Handling: The server manages incoming client connections using sockets, creating a separate thread or process for each connected client.
•	User Management: Maintaining information about connected users, their status, and handling login/logout functionality.
•	Message Routing: Implementing logic to route messages from one client to another, ensuring proper delivery.

## Considerations in Development:
1.	Concurrency and Multithreading:
•	Chat applications often require handling multiple connections simultaneously. The server must be designed to support concurrency, commonly achieved through multithreading or asynchronous programming.
2.	Security:
•	Ensuring the security of user data and messages is paramount. Encryption techniques, such as SSL/TLS, can be implemented to secure data in transit. Proper user authentication mechanisms help prevent unauthorized access.
3.	Scalability:
•	As the number of users grows, the chat application must be scalable. This involves optimizing server-side architecture to handle increasing loads efficiently.
4.	Persistence:
•	Some chat applications implement message persistence, allowing users to retrieve past messages. This may involve using databases to store and retrieve chat history.

5.	Notification Systems:
•	Implementing real-time notifications to inform users of new messages, user presence changes, or other relevant events.


Client-server chat applications are versatile tools that facilitate real-time communication between users over a network. They incorporate various components, including server-side and client-side elements, and must consider factors such as security, scalability, and concurrency. As technology continues to advance, client-server chat applications remain integral for collaborative communication in various domains.

Client-server chat applications are foundational to real-time communication over networks. They incorporate principles of socket programming, communication protocols, and security mechanisms to provide a seamless user experience. Understanding the basics of client-server chat applications is essential for developers involved in networked application development, as they form the backbone of various collaborative communication systems. As technology evolves, chat applications continue to adapt, incorporating new features and technologies to enhance user interaction and connectivity.

## Program

## Server.py
```
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
```

## Client.py
```
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
```

## Output

![alt text](<Screenshot 2026-04-25 105412.png>)
![alt text](<Screenshot 2026-04-25 105340.png>)

## Result:

Thus the study on Client Server Chat Applications has been performed

