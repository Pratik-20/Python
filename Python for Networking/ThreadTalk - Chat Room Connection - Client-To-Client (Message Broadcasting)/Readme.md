# **ThreadTalk - Chat Room Connection - Client-To-Client (Message Broadcasting)**

## 📌 Project Overview  
This project implements a **multi-client chat room** using Python’s `socket` and `threading` modules. Instead of opening multiple terminal windows, multiple client scripts (`Client_1.py`, `Client_2.py`, `Client_3.py`, and `Client_4.py`) are created, allowing different clients to connect to a single server (`Server_1.py`).  

The server handles connections, broadcasts messages to all connected clients, and ensures seamless communication among them.

## 🎯 Features  
- ✅ **Multi-client support** – Up to four clients can join and chat in real time.  
- ✅ **Message broadcasting** – Messages are sent to all connected clients.  
- ✅ **Alias system** – Each client assigns an alias for identification.  
- ✅ **Thread-based handling** – Each client connection runs in a separate thread.  
- ✅ **Automatic disconnection handling** – Alerts other clients when one leaves.  

## 🔧 Project Structure  

ThreadTalk/ │── Server_1.py # The chat server that manages client connections │── Client_1.py # First client script │── Client_2.py # Second client script │── Client_3.py # Third client script │── Client_4.py # Fourth client script │── README.md # Project documentation


## 🛠 Requirements  
Before running the project, ensure you have the following installed:

- **Python 3.6+**  
- `socket` and `threading` modules (built-in in Python)  

## 🚀 How to Run  

### **Step 1: Start the Server**  
1. Open **Terminal or Bash** and navigate to the project folder:  
   ```bash
   cd /path/to/ThreadTalk
Run the server:

bash
python Server_1.py
The server will start listening for incoming client connections.

Step 2: Run Multiple Clients
Open four separate terminal tabs or use multiple scripts.

Run each client in a new tab:

bash
python Client_1.py
python Client_2.py
python Client_3.py
python Client_4.py
Each client will prompt for an alias (nickname) before joining.

Step 3: Start Chatting
Clients can send messages, and the server broadcasts them to all connected clients.

If a client disconnects, the server informs others.

🔄 Example Output
Server Output:
- ✅ Server is running and listening...
- ✅ Connection established with ('127.0.0.1', 54321)
- ✅ The alias of this client is Alice
- ✅ Alice has connected to the chat room
- ✅ Connection established with ('127.0.0.1', 54322)
- ✅ The alias of this client is Bob
- ✅ Bob has connected to the chat room
Client Output (Client_1.py):
Choose an alias: Alice
- ✅ Connected to the server!
Bob: Hello, everyone!
Alice: Hi Bob!
Disconnection Handling:
If a client disconnects:

Bob has left the chat room!
📅 Future Enhancements
🔹 Support more clients dynamically

🔹 Implement message encryption for security

🔹 Add a GUI for better user experience

📜 License
This project is released under the MIT License.
