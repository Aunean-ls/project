# import pymysql
# import uuid
# from hashlib import md5
# # 1.连接数据库  2.创建游标对象  3.写sql语句  4.执行sql语句   5.释放游标，连接对象
#
# # 连接数据库
# conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='qaz3357375', db='crawler')
# # 生成游标对象
# cursor = conn.cursor()
# # 创建表
# # cursor.execute('DROP TABLE IF EXISTS USER')
# # sql = '''
# #     CREATE TABLE USER(
# #         ID VARCHAR(64) NOT NULL PRIMARY KEY,
# #         USERNAME  VARCHAR(32) NOT NULL,
# #         PASSWORD VARCHAR(32) NOT NULL)
# # '''
# # cursor.execute(sql)
#
# password = md5('qaz3357375'.encode('utf-8')).hexdigest()
# print(password)
#
# # 插入数据
# # data = [(str(uuid.uuid1()), 'user2', md5('123'.encode('utf-8')).hexdigest()),
# #         (str(uuid.uuid1()), 'user3', md5('123234sfa'.encode('utf-8')).hexdigest()),
# #         (str(uuid.uuid1()), 'user4', md5('123dsf'.encode('utf-8')).hexdigest())]
# #
# # sql = 'INSERT INTO USER(ID,USERNAME,PASSWORD) VALUES(%s,%s,%s)'
# #
# # try:
# #     cursor.executemany(sql, data)
# #     conn.commit()
# # except:
# #     conn.rollback()  # 数据库回滚
#
# # 取出数据
# sql = "SELECT * FROM USER"
# data = cursor.execute(sql)
# print(data)
# all_data = cursor.fetchall()
# print(all_data)
# for data in all_data:
#     print(data)
#
# cursor.close()
# conn.close()



