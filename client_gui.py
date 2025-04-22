import tkinter as tk
import socket
from cryptography.fernet import Fernet

HOST = '127.0.0.1'
PORT = 65433

def send_message():
    global msg
    message = msg.get()
    if message:
        encrypted_message = cipher.encrypt(message.encode())
        client_socket.sendall(encrypted_message)
        print(f"Message Sent: {message}")
        msg.delete(0, tk.END)


def start_client():
    global client_socket, cipher, msg

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    key = client_socket.recv(1024)
    cipher = Fernet(key)

    root = tk.Tk()
    root.title("Secure Chat")

    message_label = tk.Label(root, text="Enter message:")
    message_label.pack()

    message_entry = tk.Entry(root, width=50)
    message_entry.pack()

    send_button = tk.Button(root, text="Send", command=send_message)
    send_button.pack()

    root.mainloop()

if __name__ == "__main__":
    start_client()
