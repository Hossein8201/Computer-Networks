import socket

# Socket configuration
HOST = '127.0.0.1'  # Localhost IP address
PORT = 1443         # Target port

try:
    # Create a TCP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Attempt to connect to the server
    client_socket.connect((HOST, PORT))
    print("Successfully connected to the server!")

except socket.error as e:  # Handle socket-related errors
    print(f"Connection failed: {e}")

except Exception as e:    # Handle other unexpected errors
    print(f"An error occurred: {e}")

finally:
    # Close the socket to free resources
    client_socket.close()
    print("Socket closed.")