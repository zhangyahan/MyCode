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


# poll()方法多路复用
p = poll()
# 创建地图
fdmap = {sockfd.fileno():sockfd}
# 添加关注列表
p.register(sockfd, POLLIN | POLLERR)

while True:
    # 进行IO监控
    events = p.poll()
    for fd,event in events:
        if fd == sockfd.fileno():
           # 从地图中找到相应的对象
            conn, addr = fdmap[fd].accept()
            print("客户端{}已连入".format(addr))
            # 创建新的IO 维护字典
            p.register(conn,POLLIN)
            fdmap[conn.fileno()] = conn
        else:
            # 如果不是服务器套接字，就一定是客户端套接字
            data = fdmap[fd].recv(1024)
            if not data:
                # 从关注列表移除
                p.unregister(fd)
                # 关闭套接字
                fdmap[fd].close()
                # 从字典移除
                del fdmap[fd]
            else:
                print(data.decode())
                fdmap[fd].send("收到".encode())


# select()多路复用
# 创建IO列表,将服务器套接字放入
rlist = [sockfd]
wlist = []
xlist = [sockfd]
while True:
    print("等待IO发生")
    rs, ws, xs = select(rlist, xlist, wlist)

    # 遍历准备就绪的列表
    for r in rs:
        if r is sockfd:
            connfd, addr = r.accept()
            print("客户端",addr)
            rlist.append(connfd)
        else:
            data = r.recv(1024)
            if not data:
                rlist.remove(r)
                r.close()
            else:
                print(data.decode())
                r.send("收到".encode())
    for w in ws:
        pass

    for x in xs:
        pass




