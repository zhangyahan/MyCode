def login(func):
    a = 0
    while True:
        if a == 0:
            print('请登录')
            name = input("name")
            if name == '':
                break
            passwd = input("password")
            if name == "zyh"  and passwd == "123":
                a = 1
            else:
                print("用户名密码错误, 请重新登录")
        else:
            def inner(name):
                res = func(name)
                return res
            return inner


def index():
    pass

@login
def home(name):
    print("欢迎回家{}".format(name))


def shopping_car():
    pass


def order():
    pass


home('张雅涵')

