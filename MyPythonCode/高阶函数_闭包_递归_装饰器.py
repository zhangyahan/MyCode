# 高阶函数 ： 函数的参数是函数或者返回一个函数
# def f(n):
#     return n*n
#
# def foo(f,a,b):
#     res = f(a) + f(b)
#     return res
#
# print(foo(f,3,3))


# 闭包 ： 内嵌函数要使用外部函数变量，外部函数哇哦返回内部函数
# def outfunc(num):
#     def inner():
#         print(num)
#     return inner
#
# f = outfunc(18)
# f()


# 递归 ： 函数直接或间接调用自身，递归函数一定要控制递归条件
# 阶乘函数
# def foo(n):
#     if n == 1:
#         return 1
#     return n * foo(n-1)
#
# print(foo(4))
# 有5个人坐在一起，问第五个人多少岁？他说比第4个人大2岁。
# 问第4个人岁数，他说比第3个人大2岁。
# 问第三个人，又说比第2人大两岁。
# 问第2个人，说比第一个人大两岁。
# 最后问第一个人，他说是10岁。
# 请问第五个人多大？
# n表示人数
# def age(n):
#     if n == 1:
#         return 10
#     return age(n-1)+2
#
# print(age(5))


# 装饰器 ： 在不修改原函数及其调用方法的情况下为其扩展内容
# import time
# def login(g=""):
#     def show_time(func):
#         def inner(*args,**kwargs):
#             start = time.time()
#             res = func(*args,**kwargs)
#             end = time.time()
#             if g == "true":
#                 print(end-start)
#             return res
#         return inner
#     return show_time
#
# @login(g='true')
# def foo(*args,**kwargs):
#     time.sleep(2)
#     print(args)
#     print(kwargs)
#     return [i for i in args],[kwargs[i] for i in kwargs]
#
# print(foo(10,20,name="张三",age=19))


# def show_time(func):
#     def inner(*args, **kwargs):
#         import time
#         start = time.time()
#         res = func(*args, **kwargs)
#         end = time.time()
#         print(end-start)
#         return res
#     return inner
#
#
# @show_time
# def foo(*args, **kwargs):
#     import time
#     time.sleep(3)
#     print(args)
#     print(kwargs)
#
#
# foo(1, 2, 3, name='张三', age=18)


def quanxian(fn):

    def inner(name, money):
        username = input('账号')
        password = int(input('密码'))
        if username == 'root' and password == 123456:
            s = fn(name, money)
            return s
        else:
            print('账号或密码错误')
    return inner

@quanxian
def insert(name, money):
    print(name, "存钱", money, '元')


insert('老王', 1000)

type(insert)