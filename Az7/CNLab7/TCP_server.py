import socket

# Server configuration
HOST = '127.0.0.1'      # Localhost IP
PORT = 12345            # Port to listen on

# Create a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Bind the socket to the address and port
    server_socket.bind((HOST, PORT))
    
    # Listen for incoming connections (max 5 queued connections)
    server_socket.listen(5)
    print(f"Server is listening on {HOST}:{PORT}...")

    # Accept a client connection
    client_socket, addr = server_socket.accept()
    print(f"Connection established with {addr}")

    # Send a welcome message to the client (encoded to bytes)
    client_socket.send("Welcome to the server!".encode())

    # Receive data from the client (max 1024 bytes)
    data = client_socket.recv(1024)
    print(f"Received from client: {data.decode()}")

except socket.error as e:
    print(f"Server error: {e}")

finally:
    # Close the client and server sockets
    client_socket.close()
    server_socket.close()
    print("Server shut down.")