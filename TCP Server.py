import socket


# Function to receive a file from a client
def receive_file(client_socket):
    try:
        # Receive the file name from the client
        filename = client_socket.recv(1024).decode()

        # Send a confirmation message to the client
        client_socket.sendall("Filename received".encode())

        # Read and write the file contents in chunks
        with open(filename, 'wb') as file:
            while True:
                chunk = client_socket.recv(1024)
                if not chunk:
                    break
                file.write(chunk)

        print("File received:", filename)

    except Exception as e:
        print("Error occurred while receiving the file:", str(e))


# Main server program
def main():
    # Server details
    server_ip = '127.0.0.1'
    server_port = 12345

    # Create a TCP socket for accepting client connections
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Bind the socket to the server address
        server_socket.bind((server_ip, server_port))

        # Listen for incoming connections
        server_socket.listen(1)
        print("Server started and listening for connections...")

        while True:
            # Accept a client connection
            client_socket, client_address = server_socket.accept()
            print("Client connected:", client_address)

            # Receive the file from the client
            receive_file(client_socket)

            # Close the client connection
            client_socket.close()

    except Exception as e:
        print("Server error:", str(e))

    finally:
        # Close the server socket
        server_socket.close()


if __name__ == '__main__':
    main()

# References
# - GitHub: https://github.com/
# - Stack Overflow: https://stackoverflow.com/
# - PyPI (Python Package Index): https://pypi.org/
# - ActiveState Code: https://code.activestate.com/recipes/langs/python/
# - Awesome Python: https://awesome-python.com/
# - Reddit's r/learnpython: https://www.reddit.com/r/learnpython/    
# - GeeksforGeeks: https://www.geeksforgeeks.org/socket-programming-python/