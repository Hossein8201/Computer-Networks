import socket
from datetime import datetime

# Server configuration
HOST = '127.0.0.1'
PORT = 12345

# Create UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((HOST, PORT))

print("UDP Server is listening...")

while True:
    # Receive data from client
    data, addr = server_socket.recvfrom(1024)
    print("Received from client:", data.decode())

    # Send current time back to client
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    server_socket.sendto(current_time.encode(), addr)