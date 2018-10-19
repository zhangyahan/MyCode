from flask import render_template

from . import main
from ..models import *
from ..models import db


@main.route("/")
@main.route("/index")
def index_views():
    user = User.query.all()
    # print(user.name)
    return render_template("01-index.html", params=locals())
