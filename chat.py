import socket
import threading

# Server configuration
HOST = '127.0.0.1'  # Localhost
PORT = 12345

# List to keep track of connected clients
clients = []

# Function to handle client connections
def handle_client(client_socket):
    while True:
        try:
            # Receive message from client
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(f"Received message: {message}")
                broadcast(message, client_socket)
            else:
                remove_client(client_socket)
                break
        except:
            continue

# Function to broadcast message to all clients
def broadcast(message, connection):
    for client in clients:
        if client != connection:
            try:
                client.send(message.encode('utf-8'))
            except:
                remove_client(client)

# Function to remove client from list
def remove_client(connection):
    if connection in clients:
        clients.remove(connection)

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)
    print(f"Server started on {HOST}:{PORT}")

    while True:
        client_socket, client_address = server.accept()
        clients.append(client_socket)
        print(f"Connection from {client_address}")

        # Start a new thread to handle the client
        threading.Thread(target=handle_client, args=(client_socket,)).start()

# Function to receive messages from server
def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(message)
            else:
                break
        except:
            break

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    # Start a new thread to receive messages from the server
    threading.Thread(target=receive_messages, args=(client,)).start()

    while True:
        message = input()
        client.send(message.encode('utf-8'))

def main():
    choice = input("Enter 's' to start the server, 'c' to start the client: ").lower()
    if choice == 's':
        start_server()
    elif choice == 'c':
        start_client()
    else:
        print("Invalid choice. Please enter 's' or 'c'.")

if __name__ == "__main__":
    main()
