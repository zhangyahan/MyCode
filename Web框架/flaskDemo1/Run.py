from flask import Flask, request, make_response, render_template
from time import *
import re

app = Flask(__name__)


@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "GET":
        res = make_response(render_template("index.html"))
        return res
    else:
        f = request.files["ufile"]
        res = re.findall("\d+", str(localtime()))
        filename = "".join(res[0:-3]) + f.filename
        f.save("static/imgs/" + filename)
        return "提交成功"


@app.route("/login",methods=["GET","POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        name = request.form["username"]
        password = request.form["password"]
        ispwd = request.form["ispwd"]
        print(name,password,ispwd)
        return "登录成功"


if __name__ == '__main__':
    app.run(debug=True)
