# 读操作
# f = open('test.txt', 'r', encoding='utf-8')
# open打开一个文件, 返回文件流
# open函数自动检索当前系统的编码, 会按照系统编码进行解码
# data = f.read()  # 将文件流中的信息读出, 返回数据对象
# print(data)
# print(f.readable())  # 判断是否可读
# print(f.readline())  # 只读一行
# print(f.readlines())  # 将内容全部读出,按行分割,返回列表
# f.close()

# 写操作
# w创建一个空文件
# f = open('test.txt', 'w', encoding='utf-8')
# f.write("1111111111111\n")
# f.write("22222222222222\n")
# # f.writable()
# f.writelines(['333\n', '444\n'])  # 传递一个列表
# f.close()
# 写的参数必须是字符串

# 写模式 - a
# 以追加的模式写入

# b模式, 字节方式打开文件


