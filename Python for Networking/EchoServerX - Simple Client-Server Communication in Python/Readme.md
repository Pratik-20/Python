# **PyConnect - Simple Client-Server Communication in Python**  

## 🚀 Project Overview  
PyConnect is a simple Python-based client-server communication project that demonstrates how sockets work to facilitate data exchange between a server and a client. The server listens for incoming connections, and the client connects to the server to receive a welcome message.

## 🔹 Features  
- ✅ Establishes a basic TCP connection between a client and a server  
- ✅ Uses Python's built-in `socket` module  
- ✅ Sends and receives messages between client and server  
- ✅ Lightweight and easy to understand  

## 📁 Project Structure  

PyConnect/ │── server.py # Server-side script that listens for client connections │── client.py # Client-side script that connects to the server │── README.md # Project documentation

PyConnect/ │── server.py # Server-side script that listens for client connections │── client.py # Client-side script that connects to the server │── README.md # Project documentation


## 🛠 Getting Started  
Follow the steps below to run the project on your local machine:

### **Prerequisites**  
- 🐍 Python 3 installed  
- 📝 Basic understanding of Python and sockets  

## ⚙️ **How to Run**  

#### **Step 1: Start the Server**  
Open a terminal and run:  
sh
python server.py
You'll see messages indicating the server is listening for connections.

Step 2: Run the Client
Open another terminal and execute:

sh
python client.py
The client will connect to the server and receive a welcome message.

🖥 Example Output
Server Output:
- ✅ Socket Successfully Created...!
- ✅ Socket binded to the port 56789
- ✅ Socket is listening for incoming connections..!
- ✅ Got connection from ('127.0.0.1', 54321)
Client Output:
- ✅ Socket Successfully Created...!
- ✅ Connected to the server at 127.0.0.1:56789
Thank You For connecting..!

## 🚀 Future Enhancements
- 🔄 Implement multi-client support

- 🔒 Add message encryption for secure communication

- 🎨 Build a GUI for better user interaction

- 📜 License
- This project is released under the MIT License.
