# 匿名函数 ： 为解决功能很简单的需求而设计的一句话函数
# calc = lambda n ： n ** n
# 函数名  关键字  参数  返回值
# 请把以下函数变成匿名函数
# def add(x,y):
#     return x+y

add = lambda x,y : x + y
print(add(1,2))
a = 10
b = 20
c = 15
print("做") if a > b else (print("又有") if c >b else print("aa"))
print("hello")
print("hello")