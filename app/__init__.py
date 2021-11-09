from flask import Flask
from config import DevelopmentConfig
from app.models import User, Item, Order, Question, Answer, ImgBox
from app.extensions import db, redis_client
from app.utils.token_operation import *


def create_app():
    """工厂函数，创建APP实例"""
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    register_extensions(app)
    register_blueprint(app)
    register_shell_context(app)
    return app


def register_extensions(app):
    db.init_app(app)
    redis_client.init_app(app)


def register_blueprint(app):
    from .api import UserApi, ItemApi
    app.register_blueprint(UserApi)
    app.register_blueprint(ItemApi)


def register_shell_context(app):
    @app.shell_context_processor
    def make_shell_context():
        return dict(db=db, User=User, Item=Item,
                    Order=Order, Question=Question,
                    Answer=Answer, ImgBox=ImgBox)
