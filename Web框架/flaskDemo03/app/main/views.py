from flask import render_template
from ..models import User
from . import main


@main.route("/")
def index_views():
    user = User.query.filter_by(id=1).first()
    return render_template("index.html", params=locals())
