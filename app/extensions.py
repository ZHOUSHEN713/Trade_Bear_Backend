from flask_sqlalchemy import SQLAlchemy
from flask_redis import FlaskRedis
from flask_httpauth import HTTPBasicAuth

db = SQLAlchemy()
redis_client = FlaskRedis()
auth = HTTPBasicAuth()
