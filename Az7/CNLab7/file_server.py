import socket

def send_file(file_name, host, port):
    # Create TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"[SERVER] Waiting for client on {host}:{port}...")

    # Accept client connection
    client_socket, addr = server_socket.accept()
    print(f"[SERVER] Connected to {addr}")

    try:
        # Open and send file in chunks of 1024 bytes
        with open(file_name, 'rb') as file:
            while True:
                file_data = file.read(1024)  # Read 1KB at a time
                if not file_data:
                    break
                client_socket.send(file_data)
        print("[SERVER] File sent successfully!")

    except Exception as e:
        print(f"[SERVER] Error: {e}")

    finally:
        client_socket.close()
        server_socket.close()

# Example usage
send_file("example.txt", "127.0.0.1", 12345)