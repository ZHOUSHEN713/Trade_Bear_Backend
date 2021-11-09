class Config(object):
    """
    Basic Configure
    """
    # MySQL 配置
    MYSQL_USER = "root"
    MYSQL_PASSWORD = "123456"
    MYSQL_HOST = "127.0.0.1"
    MYSQL_PORT = 3306
    DATABASE = "Trade_Bear"
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{DATABASE}?charset=utf8mb4"
    SQLALCHEMY_COMMIT_ON_TEARDOWN = False  # 是否自动提交事务
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # 是否开启追踪
    # Redis 配置
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379
    REDIS_DB = 1
    REDIS_URL = f"redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}"
    # ----------------------------------------------------------------
    SECRET_KEY = "daxueshenmai"  # Token生成秘钥
    TOKEN_EXPIRATION = 60 * 60  # Token有效时间(秒)


class DevelopmentConfig(Config):
    DEBUG = True
    PORT = 6666
    HOST = "0.0.0.0"
