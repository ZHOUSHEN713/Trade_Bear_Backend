from app import db


class User(db.Model):
    __tablename__ = "User"
    userID = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    userName = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(500), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    credit = db.Column(db.Integer, default=0)
    gender = db.Column(db.Integer, default=-1)  # unknown:-1 man:1 women:0
    region = db.Column(db.String(10), nullable=False)



