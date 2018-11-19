# 自定义反转函数
# class Count:
#     def __init__(self, start):
#         self.start = start
#
#     def __iter__(self):
#         n = 0
#         while n <= self.start:
#             yield n
#             n += 1
#
#     def __reversed__(self):
#         n = self.start
#         while n >= 0:
#             yield n
#             n -= 1
#
# a = Count(5)
# for i in a:
#     print(i)
#
# for i in reversed(a):
#     print(i)


# class Room:
# #     tag = 1
# #
# #     def __init__(self, name, owner, width, height, length):
# #         self.name = name
# #         self.owner = owner
# #         self.width = width
# #         self.height = height
# #         self.length = length
# #
# #     # 将方法调用时变成属性
# #     @property
# #     def cal_area(self):
# #         return '{0.name}住在{0.owner}'.format(self)
# #
# #     def test(self):
# #         print('from test', self.name)
# #
# #     # 类方法,实例也可以调用到
# #     @classmethod
# #     def tell_info(cls, x):
# #         print('--------->', cls.tag, x)
# #
# # Room.tell_info('whh')
# r1 = Room('厕所', 'alex', 100, 100, 100)
# Room.tell_info(r1)
# r2 = Room('厕所', 'whh', 1, 1, 1)
# print(r1.cal_area)
# print(r2.cal_area)
# print(Room.tag)
# Room.test(r1)


# class Room:
#     tag = 1
#
#     def __init__(self, name, owner, width, height, length):
#         self.name = name
#         self.owner = owner
#         self.width = width
#         self.height = height
#         self.length = length
#
#     将方法调用时变成属性
#     @property
#     def cal_area(self):
#         return '{0.name}住在{0.owner}'.format(self)
#
#     def test(self):
#         print('from test', self.name)
#
#     类方法,实例也可以调用到
#     @classmethod
#     def tell_info(cls, x):
#         print('--------->', cls.tag, x)
#
#     静态方法, 只是名义上归属类管理,
#     不能使用类变量和实例变量,只是类的工具包
#     @staticmethod
#     def wash_body(a, b, c):
#         print('{},{},{}正在洗澡'.format(a, b, c))

# print(Room.__dict__)
# Room.wash_body('alex', 'whh', 'ltd')
# r1 = Room('厕所', 'alex', 100, 100, 100)
# r1.wash_body('alex', 'whh', 'ltd')
# print(r1.__dict__)


# 类的组合
# class School:
#     def __init__(self, name, address):
#         self.name = name
#         self.address = address
#
#     def zhao_sheng(self):
#         print('{}正在招生'.format(self.address))
#
#
# class Course:
#     def __init__(self, name, price, period, school):
#         self.name = name
#         self.price = price
#         self.period = period
#         self.school = school
#
#
# s1 = School('oldBoy', '北京')
# s2 = School('oldBoy', '南京')
# s3 = School('oldBoy', '东京')
#
# c1 = Course('Linux', 10, '1h', s1)
# c2 = Course('Python', 20, '2h', s2)
# c3 = Course('Java', 30, '3h', s3)
#
# print(c1.__dict__)
# print(c1.school.name)
# c1.school.zhao_sheng()


# 选课
# class School:
#     def __init__(self, name, address):
#         self.name = name
#         self.address = address
#
#     def zhao_sheng(self):
#         print('{}正在招生'.format(self.address))
#
#
# class Course:
#     def __init__(self, name, price, period, school):
#         self.name = name
#         self.price = price
#         self.period = period
#         self.school = school
#
#
# s1 = School('oldBoy', '北京')
# s2 = School('oldBoy', '南京')
# s3 = School('oldBoy', '东京')
#
# while True:
#     mag = '''
#         1 王花花 北京
#         2 李狗蛋 南京
#         3 李铁柱 东京
#     '''
#     menu = {
#         '1': s1,
#         '2': s2,
#         '3': s3,
#     }
#     print(mag)
#     choice = input('学校>>')
#     school_obj = menu[choice]
#
#     name = input('课程>>')
#     price = input('费用>>')
#     period = input('周期>>')
#
#     new_course = Course(name, price, period, school_obj)
#     print('课程{}, 费用{}, 周期{}, 学校{}, 地址{}'.format(
#           new_course.name, new_course.price, new_course.period,
#           new_course.school.name, new_course.school.address))







# 面向对象: 继承, 多态, 封装


# 类的继承: 分为单继承/多继承
# 继承重名不会覆盖, 会优先在自己的类中寻找,
# 当属性和方法找不到时, 再到父类中找
# 新式类: 广度优先(python3中都是新式类)
# 经典类: 深度优先,一条线走到底再换另一条线
# class Parent:
#     """这是父类"""
#     money = 10
#
#     def __init__(self, name):
#         print('父类')
#         self.name = name
#
#     def hit_son(self):
#         print('{}正在打儿子'.format(self.name))
#
#
# class Subclass(Parent):
#     money = 10000000000000000000
#
#
# # print(Subclass.money)
# # Subclass.hit_son()
# # print(Parent.__dict__)
# # print(Subclass.__dict__)
# s1 = Subclass('alex')
# print(s1.name)
# print(s1.money)
# print(Parent.money)
# print(s1.__dict__)
# s1.hit_son()


# 在子类中调用父类的方法
# class Vehicle:
#     Country = 'China'
#
#     def __init__(self, name, speed, load, power):
#         self.name = name
#         self.speed = speed
#         self.load = load
#         self.power = power
#
#     def run(self):
#         print('{}开动啦'.format(self.name))
#
#
# class Subway(Vehicle):
#     def __init__(self, line,name, speed, load, power):
#         Vehicle.__init__(self, name, speed, load, power)
#         self.line = line
#
#     def show_info(self):
#         print(self.name, self.line)
#
#     def run(self):
#         super().run(self)
#         print("{}{}开动啦".format(self.name, self.line))
#
# line13 = Subway('13号线', '地铁','10km/s', 100000000, '电')
#
# line13.show_info()
# line13.run()



# 类的多态
# class Prent(object):
#     def __init__(self, temp, name):
#         self.name = name
#         self.temp = temp
#
#     def turn_ice(self):
#         if self.temp < 0:
#             print('[{0}]结冰了'.format(self.name))
#         elif self.temp <= 100:
#             print('[{0}]变成水了'.format(self.name))
#         elif self.temp > 100:
#             print('[{0}]变成水蒸气了'.format(self.name))
#
#
# class Bing(Prent):
#     pass
#
#
# class Shui(Prent):
#     pass
#
# class Zheng(Prent):
#     pass
#
# b1 = Bing(-10, '冰')
# s1 = Shui(10, '水')
# z1 = Zheng(110, '水')
#
# def func(obj):
#     obj.turn_ice()
#
#
# func(b1)
# func(s1)
# func(z1)


# 类的封装
# __author__ = 'zyahan'
#
# class People(object):
#     __star = 'earth'
#     def __init__(self, id, name, age, aslary):
#         self.id = id
#         self.name = name
#         self.age = age
#         self.aslary = aslary
#
#     def get_id(self):
#         print('我是私有函数, 我获得的id是{}'.format(self.id))
#
#     def get_star(self):
#         print(self.__star)


# p1 = People('2121', 'alex', '18', '21212122121')
# print(p1.__star)
# print(People.__dict__)
# print(p1._People__star)
# p1.get_star()




# 反射: 为什么用反射, 可插拔, 判断有没有此属性或方法
# 如果有则执行, 没有的话执行其他逻辑
# hasattr(object:obj, name:str): 判断对象中有没有此属性
# class BlackMedium:
#     feture = 'Ugly'
#     def __init__(self, name, address):
#         self.name = name
#         self.address = address
#
#     def sell_hourse(self):
#         print('[{}]正在卖房子'.format(self.name))
#
#     def rent_hourse(self):
#         print('[{}]正在租房子'.format(self.name))
#
# b1 = BlackMedium('万成置地', '天露园')

# print(hasattr(BlackMedium, 'feture'))

# print(hasattr(b1, 'name'))  # 判断对象中有没有此属性
# print(hasattr(b1, 'sell_hourse'))
# print(b1.__dict__)

# 获取属性或方法, 没有的话返回default值
# print(getattr(b1, 'rent_hourse', '没有这个属性'))

# b1.sb = True
# setattr(b1, 'sb', True)  # 设置属性值
# setattr(b1, 'func', lambda x:x+1)
# setattr(b1, 'func1', lambda self:self.name + 'sb')
# print(b1.__dict__)
# print(b1.func)
# print(b1.func(10))
# print(b1.func1(b1))

# delattr(b1, 'sb')  # 删除属性
# print(b1.__dict__)







# 动态导入模块
# from .m1 import t
# module_t = __import__('m1.t')
# print(module_t)  # <module 'm1'>
# module_t.t.test1()

# from m1.t import *
# from m1.t import test1, _test2
# _test2()
# test1()

# import importlib
#
# m = importlib.import_module('m1.t')
# print(m)  # <module 'm1.t'>
# m.test1()
# m._test2()





# 双下划线开头的attr方法
# class Foo:
#     x = 1
#     def __init__(self, y):
#         self.y = y
#
#     # 当调用的对象不存在时触发
#     def __getattr__(self, item):
#         print('调用对象不存在')
#
#     # 当删除对象时触发
#     def __delattr__(self, item):
#         del self.__dict__[item]
#         print('删除操作')
#
#     def __setattr__(self, key, value):
#         print('__setattr__执行')
#         # self.key = value  # 无限递归
#         self.__dict__[key]  = value
#
# f1 = Foo(10)
# print(f1.__dict__)
# f1.z = 2
# print(f1.__dict__)
# print(f1.y)
# f1.ssssssssssssss
# del f1.y
# del f1.x

# class Foo:
#
#     def __getattr__(self, item):
#         print('-------------')
#
# print(Foo.__dict__)
# print(dir(Foo))
# f1 = Foo()
# print(f1.x)  # 只有在属性不存在时, 会自动触发__getattr__


# class Foo:
#
#     def __init__(self, name):
#         self.name = name
#
#     def __getattr__(self, item):
#         return '你找的属性{}不存在'.format(item)
#
#     # 当属性修改添加时调用
#     def __setattr__(self, key, value):
#         print('执行setattr', key, value)
#         if type(value) is str:
#             print('开始设置')
#             self.__dict__[key] = value
#         else:
#             print('必须是字符串类型')
#
#     def __delattr__(self, item):
#         print('执行__delattr__')
#         self.__dict__.pop(item)


# f1 = Foo('alex')
# f1.age = 18
# f1.gender = 'male'
# print(f1.name)
# print(f1.age)
# print(f1.gender)
# print(f1.__dict__)
# del f1.name
# print(f1.__dict__)





# class List(list):
#     # 自定义list类的append方法
#     def append(self, object):
#         if type(object) is str:
#             super().append(object)
#         else:
#             print('只能添加字符串类型')
#
#     def show_midlle(self):
#         middlle_index = int(len(self) / 2)
#         return self[middlle_index]

# l1 = List('helloworld')
# print(l1)
# print(l1, type(l1))
# l1.append('sdadsa')
# l1.append(111111111)
# print(l1.show_midlle())
# print(l1)

# l2 = list('hello world')
# print(l2, type(l2))






# 授权: 类似于组合的形式, 如果不定值, 直接使用__getattr__
# import time
#
# class Open:
#
#     def __init__(self, filename, mode='r', encoding='utf-8'):
#         # self.filename = filename
#         self.file = open(filename, mode, encoding=encoding)
#         self.mode = mode
#         self.encoding = encoding
#
#     def write(self, line):
#         print('---------->', line)
#         t = time.strftime('%Y-%m-%d %X')
#         self.file.write('{} {}'.format(t, line))
#
#     def __getattr__(self, item):
#         return getattr(self.file, item)


# f1 = Open('a.txt', 'w+')
# print(f1.__dict__)
# print(f1.file)
# print(f1.read)  # 触发的是__getattr__
# print(f1.write)
# f1.write('cpu负载过高\n')
# f1.write('内存空间不足\n')
# f1.write('cpu负载过高\n')
# f1.write('cpu负载过高\n')
# f1.seek(0)
# print('----->', f1.read())

# sys_file = open('b.txt', 'w+')
# print(getattr(sys_file, 'read'))























# aid1805n_pm@tedu.cn
# tMooc2018TTS