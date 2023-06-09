import socket
import os
import json
import csv
from PIL import Image


# Function to send a file to the server
def send_file(filename, server_ip, server_port):
    # Create a TCP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to the server
        client_socket.connect((server_ip, server_port))

        # Send the file name to the server
        client_socket.sendall(filename.encode())

        # Open the file
        with open(filename, 'rb') as file:
            # Read and send the file contents in chunks
            while True:
                chunk = file.read(1024)
                if not chunk:
                    break
                client_socket.sendall(chunk)

        print("File sent successfully!")

    except Exception as e:
        print("Error occurred while sending the file:", str(e))

    finally:
        # Close the socket connection
        client_socket.close()


# Function to receive and visualize a file from the server
def receive_file(client_socket):
    try:
        # Receive the file name from the server
        filename = client_socket.recv(1024).decode()

        # Send a confirmation message to the server
        client_socket.sendall("Filename received".encode())

        # Check the file type based on its extension
        _, file_ext = os.path.splitext(filename)

        if file_ext == '.jpg' or file_ext == '.png':
            # Receive and display an image file
            with open(filename, 'wb') as file:
                while True:
                    chunk = client_socket.recv(1024)
                    if not chunk:
                        break
                    file.write(chunk)

            # Open and display the image file
            img = Image.open(filename)
            img.show()

        elif file_ext == '.csv':
            # Receive and display a CSV file
            with open(filename, 'wb') as file:
                while True:
                    chunk = client_socket.recv(1024)
                    if not chunk:
                        break
                    file.write(chunk)

            # Open and read the CSV file
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    print(row)

        elif file_ext == '.json':
            # Receive and display a JSON file
            with open(filename, 'wb') as file:
                while True:
                    chunk = client_socket.recv(1024)
                    if not chunk:
                        break
                    file.write(chunk)

            # Open and parse the JSON file
            with open(filename, 'r') as file:
                data = json.load(file)
                print(data)

        else:
            print("Unsupported file type:", file_ext)

    except Exception as e:
        print("Error occurred while receiving the file:", str(e))


# Main client program
def main():
    # Server details
    server_ip = '127.0.0.1'
    server_port = 12345

    # File to send
    file_to_send = 'img.jpg'
    file_name = os.path.basename(file_to_send)

    # Send the file to the server
    send_file(file_name, server_ip, server_port)

    # Create a TCP socket for receiving files
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to the server
        client_socket.connect((server_ip, server_port))

        # Receive and visualize the file from the server
        receive_file(client_socket)

    except Exception as e:
        print("Error occurred while receiving the file:", str(e))

    finally:
        # Close the socket connection
        client_socket.close()


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