from socket import *


sock_client = socket(AF_INET, SOCK_STREAM)

sock_client.connect(("127.0.0.1", 9999))

while True:
    msg = input(">>>")
    sock_client.send(msg.encode())
    data = sock_client.recv(1024)
    print(data.decode())




