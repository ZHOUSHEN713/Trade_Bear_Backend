from app.extensions import db


class Answer(db.Model):
    __tablename__ = "Answer"
    answerId = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    body = db.Column(db.String(200), nullable=False)
    questionId = db.Column(db.Integer, db.ForeignKey("Question.questionId"), nullable=False)

    def __init__(self, body, questionId):
        self.body = body
        self.questionId = questionId



