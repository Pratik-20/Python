"""
Project Theme: Simple Client-Server Communication in Python

Description:
This script implements a basic server using Python's socket module.
The server listens for incoming connections and sends a thank-you message
to the connected client.

Author: Pratik Thorawdae
Date: 05 April 2025
"""

import socket

# Create a socket object
s = socket.socket()
print("✅ Socket Successfully Created...!")

# Define the port on which the server will listen
port = 56789

# Bind the socket to the port and start listening for connections
s.bind(('', port))
print(f'✅ Socket binded to the port {port}')
s.listen(5)
print('✅ Socket is listening for incoming connections..!')

# Continuously accept incoming connections
while True:
    c, addr = s.accept()  # Accept a connection
    print(f'✅ Got connection from {addr}')

    # Send a message to the connected client
    message = 'Thank You For connecting..!'
    c.send(message.encode())

    # Close the connection with the client
    c.close()
