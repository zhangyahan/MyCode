import mysql_info


student_mysql = mysql_info.student_info_mysql()

# 增
def student_insert():
    student_name = input("请输入学生姓名")
    student_age = int(input("请输入学生年龄"))
    student_score = int(input("请输入学生成绩"))
    student_mysql.insert_data(student_name,student_age,student_score)

# 查
def student_show():
    datas = student_mysql.show_all_data()
    print("+" + "-"*9 + "+" + "-"*22 + "+" + "-"*12 + "+" + "-"*12 + "+")
    print("|" + "Serial".center(9) + "|" + "name".center(22) + "|"
          + "age".center(12) + "|" + "socre".center(12) + "|")
    print("+" + "-" * 9 + "+" + "-" * 22 + "+" + "-" * 12 + "+" + "-" * 12 + "+")
    for data in datas:
        student_serial_number = str(data[0])
        student_name = data[1]
        student_age = str(data[2])
        student_score = str(data[3])
        print("|" + student_serial_number.center(9) + "|" + student_name.center(22) + "|"
              + student_age.center(12) + "|" + student_score.center(12) + "|")
        print("+" + "-" * 9 + "+" + "-" * 22 + "+" + "-" * 12 + "+" + "-" * 12 + "+")

# 改
def student_update():
    pass

# 删
def student_delete():
    pass