"""
Theme: Chat Room Connection - Client-To-Client

Description:
This script represents a chat room client that connects to a server,
provides an alias, and enables real-time communication with other clients
in the chat room.

Author: Your Name
Date: 06 April 2025
"""

import threading
import socket

# Ask the user to choose an alias
alias = input('Choose an alias: ')

# Create a socket instance
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client.connect(('127.0.0.1', 59000))

def client_receive():
    """
    Function to receive messages from the server.
    """
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == "alias?":
                # Send the alias to the server
                client.send(alias.encode('utf-8'))
            else:
                # Print received messages
                print(message)
        except:
            # Handle connection errors
            print('Error! Connection closed.')
            client.close()
            break

def client_send():
    """
    Function to send messages to the server.
    """
    while True:
        message = f'{alias}: {input("")}'
        client.send(message.encode('utf-8'))

# Start threads for sending and receiving messages
receive_thread = threading.Thread(target=client_receive)
receive_thread.start()

send_thread = threading.Thread(target=client_send)
send_thread.start()
