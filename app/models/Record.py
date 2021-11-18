from app.extensions import db


class Record(db.Model):
    __tablename__ = "Record"
    recordId = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    userId = db.Column(db.Integer, nullable=False)
    itemId = db.Column(db.Integer, nullable=False)

    def __init__(self, userId, itemId):
        self.userId = userId
        self.itemId = itemId

