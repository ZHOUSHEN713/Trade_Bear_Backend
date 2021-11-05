from app.extensions import db
from datetime import datetime


class Item(db.Model):
    __tablename__ = "Item"
    itemId = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    title = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=False)
    postTime = db.Column(db.DateTime, default=datetime.now)
    category = db.Column(db.String(20), nullable=False)

    userId = db.Column(db.Integer, db.ForeignKey("User.userId"), nullable=False)

