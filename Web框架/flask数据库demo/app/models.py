from . import db


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True, nullable=False)
    age = db.Column(db.SmallInteger)

    def __init__(self,name,age):
        self.name = name
        self.age = age


# db.create_all()