from app.extensions import db


class ImgBox(db.Model):
    __tablename__ = "ImgBox"
    imgId = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    itemId = db.Column(db.Integer, nullable=False)
    imgUrl = db.Column(db.String(200), nullable=False)

    def __init__(self, itemId, imgUrl):
        self.itemId = itemId
        self.imgUrl = imgUrl
