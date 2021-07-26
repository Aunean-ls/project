import pymysql

if __name__ == '__main__':
    # **********begin***********#

    # 获取连接对象
    conn = pymysql.connect(host='localhost', port=3306,
                           user='root', passwd='qaz3357375',
                           charset='utf8', db='test')

    # 获取光标
    cursor = conn.cursor()

    # 执行SQL，统计教师的课程数量并按照教师名称倒序
    sql = "select Teacher.Tname,count(Course.Cname) from Course right join Teacher on Course.Tno = Teacher.Tno " \
          "group by Teacher.Tname order by Teacher.Tname desc"

    cursor.execute(sql)
    results = cursor.fetchall()
    # 获取结果集，将其赋予给变量 results
    for result in results:
        print(result[0], ":", result[1])

    # 遍历结果集，按照格式 --> 教师:课程数量 ，输出到控制台