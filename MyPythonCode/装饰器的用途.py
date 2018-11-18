# 装饰器模拟用户登录与session验证
import sys

user_list = [
    {"username": "alex", "password": '123'},
    {"username": "whh", "password": '123'},
    {"username": "ltd", "password": '123'},
    {"username": "sd", "password": '123'},
]

current_dic = {"username": None, "login": False}

def auth(aotu_type='filedb'):        
    def login(func):
        def inner(*args, **kwargs):
            print('认证类型是', aotu_type)
            if aotu_type == 'filedb':
                if current_dic["username"] and current_dic["login"]:
                    res = func(*args, **kwargs)
                    return res
                while True:
                    username = input("username").strip()
                    if not username:
                        return sys.exit('bye') 
                    password = input("password").strip()
                    for user_dic in user_list:
                        if username == user_dic["username"] \
                        and password == user_dic["password"]:
                            current_dic['username'] = username
                            current_dic['login'] = True
                            res = func(*args, **kwargs)
                            return res 
                    else:
                        print("username or password is NO")
            else:
                return sys.exit('不会玩')
        return inner
    return login


@auth(aotu_type='filedb')
def index():
    print("主页")

@auth(aotu_type='aas')
def home(name):
    print("欢迎回家{}".format(name))

@auth(aotu_type='saa')
def shopping_car():
    print("购物车")

print('before', current_dic)
index()
home('张雅涵')
shopping_car()
print('after', current_dic)

