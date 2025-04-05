"""
Theme: Broadcast - Chat Room Connection - Client-To-Client

Description:
This script sets up a chat room server that allows multiple clients to connect,
send messages, and communicate with each other in real-time. Clients use aliases
to identify themselves. The server broadcasts messages to all clients and handles
disconnections properly.

Author: Your Name
Date: 06 April 2025
"""

import threading
import socket

# Define host and port for the server
host = '127.0.0.1'  # Localhost
port = 59000        # Port number for communication

# Create a socket instance
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))

# Start listening for incoming connections
server.listen()

# Lists to store connected clients and their aliases
clients = []
aliases = []

def broadcast(message):
    """
    Function to send a message to all connected clients.
    """
    for client in clients:
        client.send(message)

def handle_client(client):
    """
    Function to handle communication with a connected client.
    """
    while True:
        try:
            # Receive message from the client and broadcast it
            message = client.recv(1024)
            broadcast(message)
        except:
            # Remove disconnected client and notify others
            index = clients.index(client)
            clients.remove(client)
            client.close()
            alias = aliases[index]
            broadcast(f'{alias} has left the chat room!'.encode('utf-8'))
            aliases.remove(alias)
            break

def receive():
    """
    Main function to accept and manage client connections.
    """
    while True:
        print('Server is running and listening...')
        # Accept a new client connection
        client, address = server.accept()
        print(f'Connection established with {str(address)}')

        # Ask the client for an alias
        client.send('alias?'.encode('utf-8'))
        alias = client.recv(1024).decode('utf-8')
        aliases.append(alias)
        clients.append(client)

        print(f'The alias of this client is {alias}')

        # Notify all clients about the new connection
        broadcast(f'{alias} has connected to the chat room'.encode('utf-8'))
        client.send('You are now connected!'.encode('utf-8'))

        # Start a new thread to handle the client
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

if __name__ == "__main__":
    receive()
