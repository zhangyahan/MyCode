# 初始化app配置，
# 以及配置数据库连接字符串

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql
pymysql.install_as_MySQLdb()

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    # 设置模式为调试模式
    app.config["DEBUG"] = True
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    # 设置数据库连接字符串
    app.config["SQLALCHEMY_DATABASE_URI"] = \
    "mysql://root:zyh1997@localhost:3306/flask"
    # 设置数据库自动提交
    app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"] = True
    # 配置sessions所需要的密匙
    app.config["SECRET_KEY"] = "~!@#$%^&*()_+"
    # 设置数据库初始化
    db.init_app(app)

    # 在此将蓝图关联起来
    from .main import main as index_bp
    app.register_blueprint(index_bp)

    return app


