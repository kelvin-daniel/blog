import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://kevon:37042490@localhost/blog'
    SQLALCHEMY_TRACK_MODIFICATIONS=True
    SECRET_KEY = os.environ.get('SECRET_KEY')
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    
    DEBUG = True