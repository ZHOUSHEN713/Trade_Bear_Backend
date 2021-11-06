from flask import Flask
from config import DevelopmentConfig
from flask_cors import CORS
import redis
from app.models import User, Item, Order, Question, Answer
from app.extensions import db


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


def register_blueprint(app):
    from .api import UserApi
    app.register_blueprint(UserApi)


def register_shell_context(app):
    @app.shell_context_processor
    def make_shell_context():
        return dict(db=db, User=User, Item=Item, Order=Order, Question=Question, Answer=Answer)
