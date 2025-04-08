# Project Theme -

# To retrieve the password of the connected Wi-Fi network,
# you can use the following Python script.
# This script will list the profiles of all Wi-Fi networks your computer has
# connected to and then retrieve the password for the currently connected network


# Explanation:

# Get Connected Network: The script first retrieves the name of the currently connected Wi-Fi network.
# Retrieve Profile Information: It then fetches the profile details of the connected network.
# Extract Password: Finally, it extracts the password from the profile details.


import subprocess

# Get the name of the connected Wi-Fi network
connected_network = subprocess.check_output(['netsh', 'wlan', 'show', 'interfaces'])
decoded_connected_network = connected_network.decode('ascii')
print(decoded_connected_network)
network_name = None

for line in decoded_connected_network.split('\n'):
    if "SSID" in line:
        network_name = line.split(":")[1].strip()
        break

if network_name:
    # Get the Wi-Fi profile details
    profile_info = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', network_name, 'key=clear'])
    decoded_profile_info = profile_info.decode('ascii')

    # Extract the password
    password = None
    for line in decoded_profile_info.split('\n'):
        if "Key Content" in line:
            password = line.split(":")[1].strip()
            break

    if password:
        print(f"The password for the Wi-Fi network '{network_name}' is: {password}")
    else:
        print(f"No password found for the Wi-Fi network '{network_name}'")
else:
    print("No Wi-Fi network is currently connected.")
