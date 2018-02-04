# _*_ coding: utf-8 _*_

import os


class BaseConfig(object):
    SECRET_KEY = str(os.urandom(24))
    ADMIN_PER_PAGE = 15
    INDEX_PER_PAGE = 12

    
class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql+mysqldb://root@localhost:3306/simplejob?charset=utf8"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAX_CONTENT_LENGTH = 3 * 1024 * 1024
    PDFS = tuple("pdf")
    UPLOADED_PDFS_ALLOW = PDFS
    UPLOADED_PDFS_DEST = os.path.join(
            os.path.abspath(os.path.dirname(__file__)),
            "static", "resumes") 


class ProductionConfig(BaseConfig):
    pass


class TestingConfig(BaseConfig):
    pass


configs = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "testing": TestingConfig,
}
