from multiprocessing import Process
from time import *


# Process创建进程
# def func1():
#     sleep(1)
#     print("我是子进程1")
#
#
# def func2():
#     sleep(2)
#     print("我是子进程2")
#
#
# def func3():
#     sleep(3)
#     print("我是子进程3")
#
#
# funcLst = [func1,func2,func3]
# process = []
#
# for func in funcLst:
#     p = Process(target=func)
#     process.append(p)
#     p.start()
#
# for i in process:
#     i.join()


# daemon函数用法，当父进程结束子进程也会跟着结束
# def func1():
#     while True:
#         print(ctime())
#
#
# p = Process(target=func1)
#
# p.daemon = True
# p.start()
# print("完了")


# 传参
# def func1(m,name):
#     for _ in range(3):
#         sleep(m)
#         print("Im ",name)
#
#
# p = Process(target=func1,args=(2,),kwargs={"name":"张雅涵"})
#
# p.start()
# p.join()



# 进程池
def worker():
    print()

