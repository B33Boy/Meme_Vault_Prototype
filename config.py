import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """This class defines the primary application configuration."""

    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'default-random-config-value'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
