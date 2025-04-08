import socket
from cryptography.fernet import Fernet


HOST = '127.0.0.1'
PORT = 65432

def start_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))

        key = client_socket.recv(1024)
        cipher = Fernet(key)

        while True:
            message = input("Enter MSG: ")
            if message.lower() == 'exit':  
                break
            
            encrypted_message = cipher.encrypt(message.encode())
            client_socket.sendall(encrypted_message)  

if __name__ == "__main__":
    start_client()
