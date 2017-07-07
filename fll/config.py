import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
	DEBUG = False
	SQLALCHEMY_DATABASE_URI = "postgresql://localhost/fll_dev"

class DevelopmentConfig(Config):
	DEBUG = True
	DEVELOPMENT = True
	NAME = "Fll"

