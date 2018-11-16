from functools import reduce


# num_l = [1, 2, 3, 4, 5, 6, 7, 100]
# num_sum = 0
# for i in num_l:
#     num_sum += i
# print(num_sum)


# def reduce_test(func, array, init=None):
#     if init is None:
#         num_sum = array.pop(0)
#     else:
#         num_sum = init
#     for i in array:
#         num_sum = func(num_sum, i)
#     return num_sum
#
#
# num_l = [1, 2, 3, 4, 5, 6, 7, 100]
# print(reduce_test(lambda x, y: x*y, num_l))


# reduce函数
# num_l = [1, 2, 3, 4, 5, 6, 7, 100]
# print(reduce(lambda x, y: x * y, num_l, 3.14))


# map/filter/reduce区别
# map: 逐个遍历出来处理, 不改变原数据结构
# filter: 逐个遍历出来处理, 移除指定数据后返回一个新的数据结构
# reduce: 逐个遍历出来处理, 将所有元素进行合并, 返回一个结果
