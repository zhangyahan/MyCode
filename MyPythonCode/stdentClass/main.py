import sys
import menu
from student import *


'''
    学生管理系统主函数
'''


def main():
    while True:
        menu.show()
        user_input = input(">>>")
        if user_input == "Q":
            sys.exit("感谢使用学生管理系统")
        elif user_input == "1":
            # 增
            student_insert()
        elif user_input == "2":
            # 查
            student_show()


if __name__ == '__main__':
    main()
