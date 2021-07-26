import os
basedir = os.path.abspath(os.path.dirname(__file__))
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#连接mysql数据库
class Config(object):

    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:qaz3357375@127.0.0.1:3306/db_data_2"
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True


app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

