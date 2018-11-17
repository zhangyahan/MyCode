# import time
# 
# 
# def producer():
#     for i in range(1000):
#         time.sleep(0.1)
#         yield "包子{}".format(i)
# 
# 
# def consumer(res):
#     for index, content in enumerate(res):
#         time.sleep(0.1)
#         yield "第{}个人吃了{}".format(index, content)
# 
# 
# baozi = producer()
# for i in consumer(baozi):
#     print(i)

# def test():
#     print("开始啦")
#     res = yield 1
#     print("第一次", res)
#     yield 2
#     print("第二次")
# 
# 
# t = test()
# res = t.__next__()
# print(res)
# t.send(res)
# send可以想yield传值传给上一次停留在的位置
# yield与return控制的都是函数的返回值
# x = yield的另外一个特性,接受send传过来的值,赋值给x


import time


def consumer(name):
    print("我是{},我准备开始吃包子了".format(name))
    while True:
        baozi = yield
        time.sleep(2)
        print("{}很开心的吃了{}".format(name, baozi))


def producer():
    c1 = consumer("wupeiqi")
    c2 = consumer("alex")
    c1.__next__()
    c2.__next__()
    for i in range(10):
        time.sleep(2)
        c1.send("屎馅包子{}".format(i))     
        c2.send("屎馅包子{}".format(i))    
producer()
