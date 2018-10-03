from flask import Flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy

import pymysql
pymysql.install_as_MySQLdb()

app = Flask(__name__,template_folder="muban")
# 指定连接数据库
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:zyh1997@localhost:3306/students"
# 指定让SQLAlchemy是否跟踪程序的修改
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# 设置自动提交
app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"] = True
# 为当前项目创建一个SQLAlchemy实例
db = SQLAlchemy(app)


class student(db.Model):
    __tablename__ = "students_table"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(32),nullable=False)
    age = db.Column(db.SmallInteger)
    score = db.Column(db.Numeric(5,2))

    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score


# 将实例映射到数据库
db.create_all()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/show")
def show():
    stud = db.session.query(student).all()
    return render_template("show.html",params=locals())


# 创建路由
@app.route("/insert",methods=["POST","GET"])
def index_info():
    if request.method == "GET":
        return render_template("insert_student_index.html")
    else:
        name = request.form.get("studentName")
        age = request.form.get("studentAge")
        score = request.form.get("studentScore")

        student_info = student(name,int(age),float(score))
        db.session.add(student_info)
        return redirect("/")


if __name__ == '__main__':
    app.run(debug=True)
