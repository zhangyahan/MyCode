from socket import *
from select import *

"""
    练习IO多路复用
    select()
    poll()
    epool()
"""


# 创建套接字
sockfd = socket(AF_INET,SOL_SOCKET)
sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
sockfd.bind(("127.0.0.1",9999))
sockfd.listen(5)

# select()多路复用
# # 创建IO列表,将服务器套接字放入
# rlist = [sockfd]
# wlist = []
# xlist = [sockfd]
# while True:
#     print("等待IO发生")
#     rs, ws, xs = select(rlist, xlist, wlist)
#
#     # 遍历准备就绪的列表
#     for r in rs:
#         if r is sockfd:
#             connfd, addr = r.accept()
#             print("客户端",addr)
#             rlist.append(connfd)
#         else:
#             data = r.recv(1024)
#             if not data:
#                 rlist.remove(r)
#                 r.close()
#             else:
#                 print(data.decode())
#                 r.send("收到".encode())
#     for w in ws:
#         pass
#
#     for x in xs:
#         pass

# poll()多路复用


