# 元组：tuple
# 元素不可被修改，元组不能被增加和删除
# 一般写元组的时候在最后一个元素加逗号

# tu = (1, "whh", "ltd",)

# 索引取值
# v = tu[0]

# 切片取值
# v = tu[0:2]

# s = "sdsadsa"
# li = ["dsa", 123]
# tu = (12, 123, "asd")

# v = tuple(s)
# print(v)

# v = tuple(li)
# print(v)

# v = list(tu)
# print(v)

# v = "_".join(tu)  # join方法对象中必须都是字符串
# print(v)


# 元组的一级元素不可修改/删除/增加
# tu = (111, "alex", (11, 22), [(33, 44)], True, 33, 44,)
# 元组，有序
# v = tu[3][0][0]
# print(v)  # 33

# v = tu[3]
# print(v)  # [(33, 44)]

# tu[3][0] = 567
# print(tu)  # 元组下标为3的元素中下标为0的元素修改为567

# ##########元组的方法############

# tuple.count(): 获取指定元素在元组中出现的次数

# tuple.index()：获取指定下标的元素

