# -*- coding:utf-8 -*-

# 列表中的元素支持所有的数据类型

# li = [1, 2, [1, 2, 3], 3, 4, 5]
# li[1:3] = [40, 50]
# print(li)

# v = li[3][2]  # 递归索引
# print(v)

# str = "adsdasdsad"
# list = 
# 字符串转换列表直接转换 

# ###########列表方法###########

li = ["whh", "ltd", "sd", "qd"]

li.append(5)
li.append("zyh")  # 将参数整体添加在列表尾部

li.clear()  # 清空列表中的元素

v = li.copy()  # 拷贝，浅拷贝

v = li.count(22)  # 计算参数在列表中出现的次数

li.extend([1, 2, 3, 4])  # 扩展原列表， 参数：可迭代对象

li.index("whh", 0, 5)  # 根据值获取当前值索引位置，从左开始，

li.insert(1, "alex")  # 在指定索引位置插入元素

v = li.pop(1)  # 删除某个值（可以指定某个索引的值，默认删除最后一个），返回删除对象

li.remove(22)  # 删除列表中指定的值， 左边优先

li.reverse()  # 将当前列表进行反转

li.sort(reverse=True)  # 进行排序,默认升序



# 列表的有序的，可变的





