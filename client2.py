import socket
from cryptography.fernet import Fernet
import base64

HOST = '127.0.0.1'
PORT = 65432


def start_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))

        key = client_socket.recv(1024)
        cipher = Fernet(key)

        while True:
            encrypted_message_b64 = client_socket.recv(1024)
            if not encrypted_message_b64:
                break

            encrypted_message = base64.b64decode(encrypted_message_b64)
            decrypted_message = cipher.decrypt(encrypted_message)
            print(f"MSG: {decrypted_message.decode()}")


            confirmation = "MSG was received successfully:"
            client_socket.sendall(confirmation.encode())




if __name__ == "__main__":
    start_client()
