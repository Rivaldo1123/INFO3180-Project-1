import os

class Config(object):
    """Base Config Object"""
    DEBUG = False
    SECRET_KEY = 'Som3$ec5etK*y'
    SQLALCHEMY_DATABASE_URI = 'postgresql://project1:1123@localhost/project1'
    SQLALCHEMY_TRACK_MODIFICATIONS = False # This is just here to suppress a warning from SQLAlchemy as it will soon be removed
    UPLOAD_FOLDER = './app/static/uploads'

class DevelopmentConfig(Config):
    """Development Config that extends the Base Config Object"""
    DEVELOPMENT = True
    DEBUG = True

class ProductionConfig(Config):
    """Production Config that extends the Base Config Object"""
    DEBUG = False