from dotenv import load_dotenv
from os import environ

load_dotenv()


class Config:
  SECRET_KEY = environ.get('SECRET_KEY')


class ProdConfig(Config):
  FLASK_ENV = 'production'
  DEBUG     = False
  TESTING   = False
  SQLALCHEMY_DATABASE_URI = environ.get('PROD_DATABASE_URI')


class DevConfig(Config):
  FLASK_ENV = 'development'
  DEBUG     = True
  TESTING   = True
  SQLALCHEMY_DATABASE_URI = environ.get('DEV_DATABASE_URI')
