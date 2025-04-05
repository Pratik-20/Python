"""
Project Theme: Simple Client-Server Communication in Python

Description:
This script implements a basic client that connects to a predefined server
and receives a message from it.

Author: Pratik Thorawade
Date: 05 April 2025
"""

import socket

# Create a socket object
s = socket.socket()
print("✅ Socket Successfully Created...!")

# Define the server details
port = 56789
server_address = '127.0.0.1'  # Localhost server

# Connect to the server
s.connect((server_address, port))
print(f'✅ Connected to the server at {server_address}:{port}')

# Receive and print the message from the server
print(s.recv(1024).decode())

# Close the connection with the server
s.close()
