# 编写视图文件
from config import app
from models import db, area_time, hour_count
from flask import render_template
from sqlalchemy import *


@app.route('/')
def my_echart():
    # 2018通话总时长最多的三个省和三个最少的省
    total_A = []
    total_B = []
    total_C = []
    time_all = db.session.query(area_time.area, area_time.total_time).order_by(area_time.total_time).all()
    for total in time_all:
        total_A.append(total[0])
        total_B.append(total[1])
    for C in range(len(total_A)):
        total_C.append([total_B[C], total_A[C]])
    # print(total_C)

    # print(total_A)
    # print(total_B)

    ##2017年7月里所有在各个小时的通话总次数
    time_A = []
    count_A = []
    time_all = db.session.query(hour_count.time_point).all()

    for time in time_all:
        time_A.append(time[0])
    # print(time_A)

    count_all = db.session.query(hour_count.count).all()
    for count in count_all:
        count_A.append(count[0])
    # print(count_A)

    return render_template('echarts_front.html', total_A=total_A,
                           total_B=total_B, time_A=time_A, total_C=total_C,
                           count_A=count_A)


if __name__ == "__main__":
    app.run(debug=True)
