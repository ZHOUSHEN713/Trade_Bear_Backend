from app.extensions import db


class Question(db.Model):
    __tablename__ = "Question"
    questionId = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    userId = db.Column(db.Integer, nullable=False)
    itemId = db.Column(db.Integer, nullable=False)
    body = db.Column(db.String(200), nullable=False)
    answers = db.relationship("Answer", backref="Question")

    def __init__(self, userId, itemId, body):
        self.userId = userId
        self.itemId = itemId
        self.body = body

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
