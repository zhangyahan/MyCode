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

# 按参数进行分割字符串, 分割的字符串不够参数, 就以空格补全
# s = 'username\temail\tpassword\nzyh\tzyahan1997@163.com\t123456\n'
# v = s.expandtabs(30)
# print(v)
# username                      email                         password
# zyh                           zyahan1997@163.com            123456

# 替换指定字符串
# str.replace('', '')
