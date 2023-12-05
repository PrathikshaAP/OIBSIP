import socket
import threading

def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            print(message)
        except:
            print("Connection to the server has been lost.")
            break

def send_messages():
    while True:
        message = input()
        client_socket.send(message.encode('utf-8'))

# Get user's username
username = input("Enter your username: ")

# Connect to the server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 5555))

# Send the username to the server
client_socket.send(username.encode('utf-8'))

# Create threads for sending and receiving messages
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

send_thread = threading.Thread(target=send_messages)
send_thread.start()
