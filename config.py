from redis import StrictRedis


class Config(object):
    """MySQL Configure"""
    user = "root"
    password = "123456"
    host = "localhost"
    port = 3036
    database = "Trade_Bear"
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{user}:{password}@{host}:{port}/{database}'
    # 是否自动提交事务
    SQLALCHEMY_COMMIT_ON_TEARDOWN = False
    # 是否开启追踪
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    """Redis Configure"""
    REDIS_HOST = '81.70.0.250'
    REDIS_PORT = 6379
    REDIS_DB = 1
    # session数据存储到redis数据库
    SESSION_TYPE = 'redis'
    SESSION_REDIS = StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)
