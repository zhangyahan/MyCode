# 迭代器 ： iter 和 next
# iter ： 可以把可迭代对象生成迭代器
# next ： 可以从迭代器中取到下一个元素
# lst = [1,2,3,4,5,6,7,8,9]
# it = iter(lst)
# while True:
#     try:
#         print(next(it))
#     except StopIteration:
#         break

# 生成器（生成器函数，生成器表达式）
# 生成器函数
# def func(n):
#     for i in range(n):
#         yield i
#
# for i in func(9):
#     print(i)
# 生成器表达式
# it = iter(i*2 for i in range(10) if i % 2 !=0)
# while True:
#     try:
#         print(next(it))
#     except StopIteration:
#         break
#
# print("hello")
# print("hello")

# 迭代器协议: 对象必须提供一个next方法,执行该方法要么返回迭代中的下一项
# 要么就引起一个Stoplteraion异常,已终止迭代(只能往后走不能往前退)

# 迭代器对象: 实现了迭代器协议的对象(如何实现:对象内部定义一个__iter__方法)

# 协议是一种约定,可迭代对象实现了迭代器协议, Python的内部工具
# (如for循环,sum,min,max函数等)使用迭代器协议访问对象

# l = [1, 2, 3]
# for i in l:
#     print(i)


# x = "hello"

# iter_test = x.__iter__()
# print(iter_test)
# try:
#     print(iter_test.__next__())
#     print(iter_test.__next__())
#     print(iter_test.__next__())
#     print(iter_test.__next__())
#     print(iter_test.__next__())
#     print(iter_test.__next__())
#     print(iter_test.__next__())
# except StopIteration:
#     pass


# def shengchanbaozi():
#     for i in range(100):
#         yield '一屉包子{}'.format(i)
# 
# 
# for i in shengchanbaozi():
#     print(i)

# def mujixiadan():
#     ret = []
#     for i in range(10000):
#         ret.append("鸡蛋{}".format(i))
#     return ret
# 
# dan = mujixiadan()
# print(dan)

# 缺点1:占用空间大
# 缺点2:效率低

def mujixiadan():
    for i in range(1000):
        yield '鸡蛋{}'.format(i)

alex_jidan = mujixiadan()
jidan = alex_jidan.__next__()
print("鸡蛋%s" % jidan)

# 生成器总结
# 语法上和函数类似: yield可以保存状态,
# 优点1:生成器的好处是延迟计算,一次返回一个结果
# 也就是说,它不会




