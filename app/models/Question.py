from app.extensions import db


class Question(db.Model):
    __tablename__ = "Question"
    questionId = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    body = db.Column(db.String(200), nullable=False)
    answers = db.relationship("Answer", backref="Question")

    def __init__(self, body):
        self.body = body
