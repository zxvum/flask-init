import os
SECRET_KEY = os.urandom(32)

SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False