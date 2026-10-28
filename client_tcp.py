import socket
import sys

HOST = "127.0.0.1"
PORT = 5000

NAME = sys.argv[1] if len(sys.argv) > 1 else "Client1"

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

client_socket.send(f"REGISTER|{NAME}".encode())

response = client_socket.recv(1024)
print(response.decode())
print(f"Вы вошли как {NAME}")

while True:
    target = input("Получатель: ")
    priority = input("Приоритет (NORMAL/HIGH): ").upper()
    message = input("Сообщение: ")

    data = f"{target}|{priority}|{message}"
    client_socket.send(data.encode())

    if message.lower() == "exit":
        break

client_socket.close()
print("Клиент завершил работу.")