# 数据库的配置变量
HOSTNAME = '39.99.62.76'
PORT = '3306'
DATABASE = 'chikexing'
USERNAME = 'root'
PASSWORD = 'wl991224'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True

DEBUG = True

SECRET_KEY = 'sdfsdfsdf123'

# 邮箱配置
MAIL_SERVER = 'smtp.qq.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_DEBUG = True
MAIL_USERNAME = ''
MAIL_PASSWORD = ''
MAIL_DEFAULT_SENDER = ''
