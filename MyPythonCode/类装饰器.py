#
# def typed(**kwargs):
#     def deco(obj):
#         for key, val in kwargs.items():
#             setattr(obj, key, val)
#         return obj
#     return deco


# 一切皆对象
# @deco
# def test():
#     print('test')
# print(test.__dict__)
# test.x = 1
# test.y = 2

# @typed(x=1, y=2, z=3)  # Foo = deco(Foo)
# class Foo:
#     pass
#
#
# print(Foo.__dict__)
#
#
# @typed(name='alex')
# class Bar:
#     pass
#
#
# print(Bar.__dict__)
# print(Bar.name)



# 装饰器的应用
# 河北工业大学城市学院   软件工程
