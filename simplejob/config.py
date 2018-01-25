# _*_ coding: utf-8 _*_
import os


class BaseConfig(object):
    SECRET_KEY = str(os.urandom(24))
    ADMIN_PER_PAGE = 15
    INDEX_PER_PAGE = 10

    UPLOADED_PATH = os.getcwd() + "/uploads"
    DROPZONE_ALLOWED_FILE_CUSTOM = True
    DROPZONE_ALLOWED_FILE_TYPE = ".pdf"
    DROPZONE_PARALLEL_UPLOADS = 1
    DROPZONE_INPUT_NAME = "file"
    DROPZONE_DEFAULT_MESSAGE = "请拖动或点击上传您的简历（仅PDF格式）"

    WHOOSH_BASE = os.getcwd() + "/whoosh_base"

    
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
