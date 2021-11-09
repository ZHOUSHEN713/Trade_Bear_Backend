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

    def __init__(self, title, price, description, category, userId):
        self.title = title
        self.price = price
        self.description = description
        self.category = category
        self.userId = userId

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
