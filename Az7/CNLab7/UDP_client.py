import socket

# Client configuration
HOST = '127.0.0.1'  # Server IP (localhost)
PORT = 12345        # Server port

# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    # Send message to server (encoded to bytes)
    message = "Request time"
    client_socket.sendto(message.encode(), (HOST, PORT))
    print("Sent to server:", message)

    # Receive response from server (max 1024 bytes)
    data, addr = client_socket.recvfrom(1024)
    print("Received from server:", data.decode())

except socket.error as e:
    print("UDP Error:", e)

finally:
    client_socket.close()