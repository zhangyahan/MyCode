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
        filename = res + f.filename
        f.save("static/imgs/" + filename)
        return "提交成功"


if __name__ == '__main__':
    app.run(debug=True)
