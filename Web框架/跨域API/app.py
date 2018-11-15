import json

import requests
from flask import Flask, request, render_template

app = Flask(__name__)


def a():
    url = "http://www.weather.com.cn/data/sk/101010100.html"
    respon = requests.get(url)
    if respon.status_code == 200:
        return respon.text
    else:
        return ""


@app.route('/')
def hello_world():
    # a = request.args["callback"]
    # dic = {
    #     "name": "sfz",
    #     "age": 18
    # }
    # print(a)
    # return "OK"
    # return "{}({})".format(a, json.dumps(dic))
    dic = json.loads(a())
    weather = dic["weatherinfo"]
    return render_template("API.html", paemas=locals())


if __name__ == '__main__':
    app.run(debug=True)



