# 将首字母转换为大写
# test = 'whh, alex, wpq, lhf, zyh, 666'
# v = test.capitalize()
# print(v)
# print: Whh, alex, wpq, lhf, zyh, 666

# 将所有的字母变小写, casefold更厉害
# test = 'whh, alex, wpq, lhf, zyh, 666'
# v1 = test.casefold()
# print(v1)
# print: whh, alex, wpq, lhf, zyh, 666
# v2 = test.lower()
# print(v2)
# print: whh, alex, wpq, lhf, zyh, 666

# 设置宽度, 并将内容居中, 20代表总长度, *代表空白位置填充(只能填一个字符, 可有可无)
# test = 'whh, alex, wpq, lhf, zyh, 666'
# v = test.center(66, '*')
# print(v)
# print: ******************whh, alex, wpq, lhf, zyh, 666*******************

# 匹配字符串中的符合第一个参数的字符次数, 从第二个参数的位置开始, 到第三个参数的位置结束
# test = 'whh, alex, wpq, lhf, zyh, 666'
# v = test.count('ex', 0, 4)
# print(v)
# print: 0

# 将字符串转为byte格式
# test = 'hello world'
# v = test.encode('utf-8')
# print(v)
# print: b'hello world'

# 将byte格式转换为字符串格式
# test = b'hello world'
# v = test.decode('utf-8')
# print(v)
# print: hello world

# 以参数结尾, 正确返回True, 错误返回False
# test = 'whh, alex, wpq, lhf, zyh, 666'
# v = test.endswith('x')
# print(v)  # False

# 以参数开头, 正确返回True, 错误返回False
# test = 'whh, alex, wpq, lhf, zyh, 666'
# v = test.startswith('x')
# print(v)  # False

# 从开始往后找, 找到第一个之后, 获取其位置, 没有找到, 返回-1
# test = 'whh, alex, wpq, lhf, zyh, 666'
# v = test.find('ex', start, end)
# index(): 功能一致, 找不着报错
# print(v)

# 格式化, 将一个字符串中的占位符替换为指定的值
# test = 'whh, alex, wpq, lhf, zyh, 666'
# test1 = 'i am {name}, age {a}'
# print(test1)
# v = test1.format(name=test, a=19)
# print(v)

# 格式化, 将一个字符串中的占位符替换为顺序位置的值
# test = 'whh, alex, wpq, lhf, zyh, 666'
# test1 = 'i am {0}, age {1}'
# print(test1)
# v = test1.format(test, 19)
# print(v)

# 格式化, 将一个字符串中的占位符替换为字典的值
# test = 'I am {name}, age {a}'
# v = test.format_map({'name': 'alex', 'a': 19})
# print(v)

# 判断字符串中是否只包含字母和数字, 返回bool值
# test = 'uasf890'
# v = test.isalnum()
# print(v)

# 判断字符串中是否只包含字母和汉字, 返回bool值
# test = 'uasf890'
# v = test.isalpha()
# print(v)

# 按参数进行分割字符串, 分割的字符串不够参数, 就以空格补全
# s = 'username\temail\tpassword\nzyh\tzyahan1997@163.com\t123456\n'
# v = s.expandtabs(30)
# print(v)
# username                      email                         password
# zyh                           zyahan1997@163.com            123456

# 判断当前字符串是否为数字, 2更强大
# test = '二'
# v1 = test.isdecimal()  # 1, 十进制小数
# v2 = test.isdigit()  # 2, 特殊符号
# v3 = test.isnumeric()  # 3, 支持中文,包含上面两个功能
# print(v1, v2, v3)

# 大小写转换, 字符串是大写时转小写, 字符串是小写时转大写
# test = 'alex'
# v = test.swapcase()
# print(v)  # ALEX

# 字母, 数字, 下划线: 标识符 def class
# 查看字符串是否符合标识符
# a = '_123'
# v = a.isidentifier()
# print(v)

# 判断是否存在不可显示的字符, 返回bool值
# test = 'odo\nas'
# v = test.isprintable()
# print(v)

# 判断是否全部都是空格, 返回bool值
# test = 'hello world'
# v = test.isspace()
# print(v)

# 判断是不是标题, 所有单词的首字母都是大写的为标题
# test = 'Hello World'
# v = test.istitle()
# print(v)
# # 转换为标题
# v = test.title()
# print(v)
# v = v.istitle()
# print(v)

# *****将字符串中的每一个元素按照指定的符号进行拼接
# test = '你是风儿我是沙'
# v = ' '.join(test)
# print(v)

# 1将字符串以左对齐的方式,右侧空格补齐
# 2将字符串以右对齐的方式,左侧空格补齐
# test = 'hello world'
# v = test.ljust(20)  # 1
# print(v)
# v = test.rjust(20)  # 2
# print(v)

# 判断是否为大小写和转换成大小写
# test = 'Alex'
# v = test.islower()
# print(v)
# v2 = test.lower()
# print(v2)
# v1 = test.isupper()
# v2 = test.upper()
# print(v1, v2)

# 包括\n, \t
# test = 'whh'
# test.lstrip()  # 去除左边空白
# test.rstrip()  # 去除右边空白
# test.strip()  # 去除两边空白

# test = 'wwhh'
# v = test.lstrip('w')  # 移除指定的字符, 贪婪匹配
# print(v)

# test = '你是风儿我是沙'
# test1 = '去你吗的风和沙'
# v = '你是风儿我是沙, 缠缠绵绵去你家'
# m = str.maketrans(test, test1)
# new_v = v.translate(m)
# print(new_v)  # 去和吗的风和沙, 缠缠绵绵去去家

# 分割字符串
# test = 'test, test, test, test'
# v = test.partition('s')  # ('te', 's', 't, test, test, test')
# v = test.rpartition('s')  # ('test, test, test, te', 's', 't')
# v = test.split('s', maxsplit=1)  # ['te', 't, test, test, test']
# print(v)

# 只能根据换行进行分割, 当参数是True或False, 代表是否保留换行
# test = 'sasddasda\ndsdasds\n'
# v = test.splitlines(True)
# print(v)  # ['sasddasda\n', 'dsdasds\n']



