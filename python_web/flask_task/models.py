#编写数据模型文件
from config import db

#对应area_time表
class area_time(db.Model):
    __tablename__ = "area_time"
    area = db.Column(db.String(255))
    total_time = db.Column(db.Integer)
    id  = db.Column(db.Integer,primary_key=True)

#对应hour_count表
class hour_count(db.Model):
    __tablename__ = "hour_count"
    time_point = db.Column(db.String(255))
    count = db.Column(db.Integer)
    id = db.Column(db.Integer,primary_key=True)


