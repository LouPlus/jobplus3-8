# _*_ coding: utf-8 _*_
import os


class BaseConfig(object):
    SECRET_KEY = str(os.urandom(24))
    INDEX_PER_PAGE = 10

class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql+mysqldb://root@localhost:3306/simplejob?charset=utf8"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(BaseConfig):
    pass


class TestingConfig(BaseConfig):
    pass


configs = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "testing": TestingConfig,
}
