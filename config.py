import os


basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = True
# SQLALCHEMY_DATABASE_URI = "mysql+pymysql://zak:zGolf38!@192.168.1.106:3306/golf"
SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://kondorAdmin:i*5wQ9KCWNe638758U$Lfd7FI3MP2Q@127.0.0.1:5432/kondor"
SECRET_KEY = b'T\x86\x89_\xa5\xc4?\xc9\r\xcf Kp\xe9\x13\xad[\x89\xc8\xbf\xbe\x19\xa7\xfa\xe8\xc0|\x8b\x19\x05\x16'
SECURITY_REGISTERABLE = True
SECURITY_PASSWORD_SALT = b'p\xc1\xdb\x84y/\xefuE\xde\xb6Q^t\x0e\x99'

MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USERNAME = 'kondorgolfapp@gmail.com'
MAIL_PASSWORD = "Q8u5!xhz4mu%Gl7Br113Zl!Y!xgl3@"