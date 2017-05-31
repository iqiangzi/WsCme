import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__)+"/../")

class Config(object):
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    MSSQL_DB = {
        "uid": "cmemaster",
        "pwd": "cme28122661",
        "host": "192.168.1.109",
        "db": "WSCME"
    }
    @staticmethod
    def init_app(app):
        pass

class DevlopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mssql+pymssql://{uid}:{pwd}@{ip}/{db}"\
        .format(uid=Config.MSSQL_DB["uid"],pwd=Config.MSSQL_DB["pwd"],ip=Config.MSSQL_DB["host"],db=Config.MSSQL_DB["db"])

config = {
    'development':DevlopmentConfig,
    'default':DevlopmentConfig
}


