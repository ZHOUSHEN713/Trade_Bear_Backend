class Config(object):
    """MySQL Configure"""
    MYSQL_USER = "root"
    MYSQL_PASSWORD = "123456"
    MYSQL_HOST = "127.0.0.1"
    MYSQL_PORT = 3306
    DATABASE = "Trade_Bear"
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{DATABASE}"
    # 是否自动提交事务
    SQLALCHEMY_COMMIT_ON_TEARDOWN = False
    # 是否开启追踪
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # """Redis Configure"""
    # REDIS_HOST = '81.70.0.250'
    # REDIS_PORT = 6379
    # REDIS_DB = 1
    # # session数据存储到redis数据库
    # SESSION_TYPE = 'redis'
    # SESSION_REDIS = StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)


class DevelopmentConfig(Config):
    DEBUG = True
    PORT = 6666
    HOST = "0.0.0.0"
