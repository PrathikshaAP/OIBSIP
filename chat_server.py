import socket
import threading

def handle_client(client_socket, username):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break

            print(f"{username}: {message}")

            # Broadcast the message to all clients
            for client in clients:
                if client != client_socket:
                    try:
                        client.send(f"{username}: {message}".encode('utf-8'))
                    except:
                        # Remove the broken connection
                        remove_client(client)

        except:
            # Remove the broken connection
            remove_client(client_socket)
            break

def remove_client(client_socket):
    if client_socket in clients:
        clients.remove(client_socket)
        client_socket.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 5555))
    server.listen(2)
    print("Server is listening for incoming connections...")

    while True:
        client_socket, client_address = server.accept()
        print(f"Connection from {client_address} has been established.")

        username = client_socket.recv(1024).decode('utf-8')
        clients.append(client_socket)

        client_socket.send("You are now connected to the chat server.".encode('utf-8'))

        # Create a new thread for each client
        client_handler = threading.Thread(target=handle_client, args=(client_socket, username))
        client_handler.start()

clients = []

if __name__ == "__main__":
    start_server()
