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
it = iter(i*2 for i in range(10) if i % 2 !=0)
while True:
    try:
        print(next(it))
    except StopIteration:
        break

print("hello")