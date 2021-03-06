from app.extensions import db

class Order(db.Model):
    __tablename__ = "Order"
    orderId = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    buyerId = db.Column(db.Integer, nullable=False)
    sellerId = db.Column(db.Integer, nullable=False)
    itemId = db.Column(db.Integer, nullable=False)

    def __init__(self, buyerId, sellerId, itemId):
        self.buyerId = buyerId
        self.sellerId = sellerId
        self.itemId = itemId

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
