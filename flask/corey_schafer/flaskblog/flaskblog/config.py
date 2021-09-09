from flaskblog import config_values, mail_credentials

class Config:

    SECRET_KEY = config_values.SECRET_KEY
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = mail_credentials.USERNAME
    MAIL_PASSWORD = mail_credentials.PASSWORD

