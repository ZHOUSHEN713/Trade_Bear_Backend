from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_cors import CORS
import redis

db = SQLAlchemy()
redis_conn = None


def create_app():
    """工厂函数，创建APP实例"""
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(Config)
    # db初始化
    db.init_app(app)

    global redis_conn
    redis_conn = redis.StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)

    # 注册蓝图
    from app.api import UserApi
    app.register_blueprint(UserApi)

    return app
