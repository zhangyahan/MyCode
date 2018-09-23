from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/',methods=["GET","POST"])
def hello_world():
    return render_template("index.html")

@app.route("/url")
def index():
    url = url_for(hello_world)
    print(url)


if __name__ == '__main__':
    app.run()
