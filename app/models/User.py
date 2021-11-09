from config import Config
from app.extensions import db
from passlib.hash import pbkdf2_sha256 as sha256
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer


class User(db.Model):
    __tablename__ = "User"
    userId = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    userName = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(500), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    credit = db.Column(db.Integer, default=0)
    gender = db.Column(db.Integer, default=-1)  # unknown:-1 man:1 women:0
    region = db.Column(db.String(100), nullable=False)
    icon = db.Column(db.String(200))

    items = db.relationship("Item", backref="User")

    def __init__(self, userName, password, email, gender, region):
        self.userName = userName
        self.password = self.generate_hash(password)
        self.email = email
        self.gender = gender
        self.region = region

    def __repr__(self):
        return '<User %r>' % self.userName

    def verify_password(self, password):
        return sha256.verify(password, self.password)

    @staticmethod
    def generate_hash(password):
        return sha256.hash(password)

    def generate_token(self):
        serializer = Serializer(Config.SECRET_KEY, Config.TOKEN_EXPIRATION)
        token = serializer.dumps({"userId": self.userId, "userName": self.userName, "password": self.password}).decode('utf-8')
        return token
