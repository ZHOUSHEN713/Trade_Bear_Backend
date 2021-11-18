from app.extensions import db


class Answer(db.Model):
    __tablename__ = "Answer"
    answerId = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    body = db.Column(db.String(200), nullable=False)
    userId = db.Column(db.Integer, nullable=False)
    questionId = db.Column(db.Integer, db.ForeignKey("Question.questionId"), nullable=False)

    def __init__(self, userId, questionId, body):
        self.body = body
        self.userId = userId
        self.questionId = questionId

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


