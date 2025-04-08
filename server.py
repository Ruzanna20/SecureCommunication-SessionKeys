import socket
import threading
from cryptography.fernet import Fernet
import base64

HOST = '127.0.0.1'
PORT = 65432

clients = []
key = Fernet.generate_key()
cipher = Fernet(key)

def handle_client(conn, addr):
    print(f"Connect client {addr}")
    
    conn.sendall(key)  

    try:
        while True:
            message = conn.recv(1024)
            if not message:
                break
            
            print(f"MSG recv. {addr}: {message.decode()}")

            encrypted_message = cipher.encrypt(message)
            encrypted_message_b64 = base64.b64encode(encrypted_message)

            for client in clients:
                if client != conn:
                    client.sendall(encrypted_message_b64)

    except:
        print(f"Fail connect:{addr} ")
    finally:
        clients.remove(conn)
        conn.close()


def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen()
        print("Server is done...")
        
        while True:
            conn, addr = server_socket.accept()
            clients.append(conn)
            thread = threading.Thread(target=handle_client, args=(conn, addr))
            thread.start()

if __name__ == "__main__":
    start_server()
