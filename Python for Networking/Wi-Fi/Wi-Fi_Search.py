"""
Explanation:

Importing subprocess: The subprocess module allows you to spawn new processes, connect to their input/output/error
pipes, and obtain their return codes. It's used here to run the netsh command. Getting the connected Wi-Fi network:
The subprocess.check_output() function runs the netsh wlan show network command, which displays information about the
Wi-Fi networks available to the computer. The output is captured as a byte string.

Decoding the output:

The output from the subprocess.check_output() function is in bytes, so it needs to be decoded into a human-readable
string using ASCII encoding. Printing the network details: Finally, the decoded string, which contains the details of
the connected Wi-Fi network, is printed to the console."""



import subprocess

# Use Case: This script retrieves and displays the name of the Wi-Fi network to which the computer is currently connected.
# It uses the 'netsh' command-line utility available on Windows to fetch network details.

# Get the name of the connected Wi-Fi network
# The subprocess.check_output() function runs the 'netsh wlan show network' command and captures its output.
connected_network = subprocess.check_output(['netsh', 'wlan', 'show', 'network'])

# Decode the output from bytes to a string using ASCII encoding.
decoded_connected_network = connected_network.decode('ascii')

# Print the decoded network details to the console.
print(decoded_connected_network)
