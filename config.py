import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://kevon:37042490@localhost/blog'
    SQLALCHEMY_TRACK_MODIFICATIONS=True
    SECRET_KEY = 'the_key'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'kaymutor@gmail.com'
    MAIL_PASSWORD = '37042490'
    
    DEBUG = True