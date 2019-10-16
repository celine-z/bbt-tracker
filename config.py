class Config(object):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost:3306/bbt_rater_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True

    DEBUG = True
    SECRET_KEY = 'SECRETKEY'
