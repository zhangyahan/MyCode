from socket import *


sock_server = socket(AF_INET, SOCK_STREAM)

sock_server.bind(("127.0.0.1", 9999))

sock_server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

sock_server.listen(4)

while True:
    connfd,addr = sock_server.accept()
    while True:
        data = connfd.recv(1024)
        if data:
            print(data.decode())
            connfd.send(b"OK")
        else:
            connfd.close()



