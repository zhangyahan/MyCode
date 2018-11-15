a = '123'
# 将字符串转换为整数, 字符串必须全部是数字
b = int(a)
print(b)

a = '1010'
# 将字符串以二进制进行转换
b = int(a, base=2)
print(b)


a = 123
# 将数字以二进制的位数进行转换
b = a.bit_length()
print(b)
