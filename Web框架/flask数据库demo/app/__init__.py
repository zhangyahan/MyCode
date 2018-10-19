# 定义app 和 数据库初始化
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql
pymysql.install_as_MySQLdb()

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:zyh1997@localhost:3306/flaskdemo"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"] = True
    app.config["DEBUG"] = True
    app.config["SECRET_KEY"] = "~!@#$%^&*("
    db.init_app(app)

    from .main import main as blueprint_main
    app.register_blueprint(blueprint_main)

    return app
