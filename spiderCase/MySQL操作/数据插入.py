import pymysql

if __name__ == '__main__':
    # **********begin********** #

    # 连接database
    conn = pymysql.connect(host='localhost', port=3306,
                           user='root', passwd='qaz3357375',
                           charset='utf8', db='test')
    cursor = conn.cursor()

    data1 = [('C1', '大学计算机基础', 'T1'), ('C10', '软件可靠性', 'T6'), ('C2', '大学计算机基础', 'T2'), ('C3', '数据库原理与技术', 'T2'),
             ('C4', '大学计算机基础', 'T5'), ('C5', '程序设计', 'T1'), ('C6', '程序设计', 'T4'), ('C7', '数字图像处理', 'T1'),
             ('C8', '抽象代数', 'T6'), ('C9', '离散数学', 'T5')]
    sql1 = 'insert into Course (Cno,Cname,Tno) values (%s,%s,%s);'

    data2 = [('T1', '周海芳', '女'), ('T2', '周竞文', '男'), ('T3', '谭春娇', '女'), ('T4', '陈立前', '男'), ('T5', '李暾', '男'),
             ('T6', '毛晓光', '男')]
    sql2 = 'insert into Teacher (Tno,Tname,Tsex) values (%s,%s,%s);'

    cursor.executemany(sql1, data1)
    cursor.executemany(sql2, data2)
    conn.commit()

    cursor.close()
    conn.close()
    # **********end********** #
