# 可以组成多少个不同的数
# count = 0
# for i in range(1, 9):
#     for y in range(1, 9):
#         if i != y:
#             count += 1
#             print(i, y)
#
# print(count)


# 九九乘法表
# for i in range(1, 10):
#     for y in range(1, i+1):
#         print('{}x{}={}\t'.format(y, i, y*i), end='')
#     print()


# 公鸡5文钱一只， 母鸡3文钱一只, 小鸡3只一文钱, 用100文买100鸡
# 都可以买到多少个组合的鸡
# for x in range(1, 100//5):  # 公鸡最多买100//5只
#     for y in range(1, 100//3):  # 母鸡最多买100//3只
#         for z in range(1, 101):  # 小鸡最多买100只
#             # 如果鸡的个数是100和鸡的钱数是100时
#             if x + y + z == 100 and x*5 + y*3 + z/3 == 100:
#                 print(x, y, z)

# l = ['alex', 'eric', 123]
# cont = ''  # 定义一个空字符串
# l2 = len(l)  # 获取列表的长度
# for i in l:  # 循环变量列表
#     if type(i) == int:  # 如果i为数字
#         if l.index(i) == l2-1:  # 如果当前i的下标为最后一个
#             cont += str(i)  # 直接加i不加_
#         else:
#             cont += str(i) + '_'  # 否则加i加_
#     else:
#         if l.index(i) == l2-1:  # 如果当前i的下标为最后一个
#             cont += i  # 直接加i不加_
#         else:
#             cont += i + '_'  # 加i加_
#
# print(cont)


# tu = [1, 2, 3, 4]
# s = enumerate(tu, 10)  # 返回一个元组, (10, tu[0])
# for i in s:
#     print(i)
# # (10, 1)
# # (11, 2)
# # (12, 3)
# # (13, 4)
#
# print(dir(s))

# nums = [2, 7, 11, 15, 1, 8, 7]
# # 找到列表中两个元素相加等于9的元素
# for i in nums:
#     for y in range(nums.index(i), len(nums)):
#         if i + nums[y] == 9:
#             print(i, nums[y])

