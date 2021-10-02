import os
_DO_NOT_USE = "[override]"

basedir = os.path.abspath(os.path.dirname(__file__))
PATH = os.path.realpath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    APPLICATION_ROOT = "/"
    TESTING = False
    SQLALCHEMY_DATABASE_URI = ""
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECURITY_PASSWORD_SALT = _DO_NOT_USE
    SECRET_KEY = _DO_NOT_USE
    def __init__(self):
        self.SQLALCHEMY_DATABASE_URI = "sqlite:///%s" % (
            os.path.join(basedir, "lamevadb.db")
        )

