# print(abs(-1))  # 1,获取绝对值
#
# print(all([1, 2, '1']))  # 判断参数的bool值, 全部为真返回True
#
# print(any([0, '']))  # 判断参数的bool值, 有一个为真返回True
#
# print(bin(3))  # 返回二进制
#
# print(bool(''))  # 判断bool值
#
# print(bytes('你好', encoding='utf-8'))  # 将字符串转换为二进制模式
# print(bytes('你好', encoding='utf-8').decode('utf-8'))  # ascii不能编码中文
#
# print(divmod(10, 3))  # 返回商/余
#
# dic = {
#     'name': 'alex'
# }
# dic_str = str(dic)
# print(eval(dic_str), type(eval(dic_str)))  # 将字符串中的数据结构给提取出来
#
# express = '1+2+3+4'
# print(eval(express))  # 将字符串中的内容执行
#
# # 可哈希的数据类型即不可变数据类型
# # 不可哈希的数据类型即可变数据类型
# print(hash('zhangyahan'))  # 进行哈希运算
# print(hash('zhangyahan'))  # 进行哈希运算
# print(hash('zhangyahan'))  # 进行哈希运算
#
# print(bin(10))  # 10转2
# print(hex(10))  # 10转16
# print(oct(10))  # 10转8
#
# print(isinstance(1, int))  # 判断是不是别人的示例
#
# print(__file__)  # 绝对路径
#
# p = {
#     'name': 'alex',
#     'age': 18,
#     'gender': 'none'
# }
# # 参数为序列就ok, 重点****************************
# print(list(zip(p.keys(), p.values())))
#  拉链函数, 可迭代对象一一对应, 优先最少, 返回参数个数的元组
# 数量为参数中最小的长度的位置
# # [('name', 'alex'), ('age', 18), ('gender', 'none')]
# # print(list(p.keys()))
# # print(list(p.values()))
#
# age_dic = {
#     'whh_age': 18,
#     'ltd_age': 12,
#     'sd_age': 13,
#     'td_age': 14,
# }
# print(max(age_dic.values()))
# # 默认比较的是字典的key
# print(max(age_dic))
# print('----->', age_dic.keys(), age_dic.values())
# print(list(max(zip(age_dic.values(), age_dic.keys()))))  # [18, 'whh_age']
#
# lst = [
#     (1, 'a'),
#     (2, 'b'),
#     (3, 'c'),
#     (4, 'd'),
# ]
# print(max(lst))

# people = [
#     {'name': 'alex', 'age': 1800},
#     {'name': 'whh', "age": 18},
#     {'name': 'hlw', "age": 9},
#     {'name': 'dt', "age": 30},
# ]
#
# print("people------>", max(people, key=lambda dic: dic['age']))
# max函数处理的是可迭代对象, 相当于一个for循环取出每个元素进行比较
# 注意: 不同类型不能进行比较
# 每个元素间进行比较, 是从每个元素的第一个位置一次比较,
# 如果这一位置分出大小, 后面的都不需要比较, 直接得出这俩元素的大小

# print(chr(97))
# print(ord('a'))  # 显示ascii表中的对应的数字

# print(pow(x, y, z))  # 获取 x ** y % z

# reversed()  # 返回反转后的结果

# print(round(1.5))  # 四舍五入

# print(set('hello'))  # 集合

# l = 'hello'
# s = slice(3, 5, 2)  # 返回一个切片对象
# print(s.start, s.stop, s.step)
# print(l[3:5])
# print(l[s])

# people = [
#     {'name': 'alex', 'age': 1800},
#     {'name': 'whh', "age": 18},
#     {'name': 'hlw', "age": 9},
#     {'name': 'dt', "age": 30},
# ]
# age = sorted(people, key=lambda dic: dic['age'], reverse=True)
# print(age)  # 排序本质就是在比较大小, 不同类型之间不能比较

# money_dic = {
#     'alex': 200,
#     'whh': 300,
#     'lll': 600,
# }
# print(sorted(money_dic,
#              key=lambda key: money_dic[key],
#              reverse=True))
# # ['lll', 'whh', 'alex']
# print(sorted(
#                 zip(money_dic.values(),
#                     money_dic.keys()),
#                 reverse=True))

# dic_str = str({'a': 1})
# print(type(dic_str))
# print(type(eval(dic_str)))  # 将字符串中的数据结构提取出来


# def test():
#     msg = '敖德萨多撒多撒'
#     print(locals())
#     print(vars())  # 功能一致


# test()

# print(vars(int))  # 将参数的方法显示出来

# def say_hi():
#     print('hello, Mr.Lin')

# import  # 导入文件名, 不能导入字符串
# __import__()  # 当文件名是字符串是时使用, 返回模块对象
