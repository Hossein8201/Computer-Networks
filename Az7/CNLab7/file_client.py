import socket

def receive_file(file_name, server_ip, server_port):
    # Create TCP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))
    print(f"[CLIENT] Connected to server at {server_ip}:{server_port}")

    try:
        # Receive file in chunks of 1024 bytes
        with open(file_name, 'wb') as file:
            while True:
                file_data = client_socket.recv(1024)  # Receive 1KB at a time
                if not file_data:
                    break
                file.write(file_data)
        print("[CLIENT] File received successfully!")

    except Exception as e:
        print(f"[CLIENT] Error: {e}")

    finally:
        client_socket.close()

# Example usage
receive_file("received_example.txt", "127.0.0.1", 12345)