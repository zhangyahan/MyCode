# 在此创建蓝图
from flask import blueprints
main = blueprints.Blueprint("main", __name__)
from . import views