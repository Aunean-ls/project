import pymysql

if __name__ == '__main__':
    # **********begin********** #
    # 在名为 nudt 的数据库下，创建课程表（Course）和教师表（Teacher）

    # 连接database
    conn = pymysql.connect(host='localhost', port=3306,
                           user='root', passwd='qaz3357375',
                           charset='utf8', db='test')

    # 得到一个可以执行SQL语句的游标对象
    cursor = conn.cursor()

    sql = """
            CREATE TABLE IF NOT EXISTS Course (
                Cno CHAR(10) NOT NULL PRIMARY KEY,
                Cname CHAR(100),
                Tno CHAR(10)
            )
        """
    cursor.execute(sql)

    sql = """
            CREATE TABLE IF NOT EXISTS Teacher (
                Tno CHAR(10) NOT NULL PRIMARY KEY,
                Tname CHAR(100),
                Tsex CHAR(10)
            )
        """
    cursor.execute(sql)

    # 关闭游标对象
    cursor.close()
    # 关闭数据库连接
    conn.close()

    # **********end********** #


