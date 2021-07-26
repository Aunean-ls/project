import pymysql


# 添加课程信息，输入课程信息格式为：Cno,Cname,Tno
def addCourse(cs):
    courseInfo = input("请输入数据")
    '1,Learn Java,T001'
    # **********begin********** #
    sql = "insert into Course (Cno,Cname,Tno) values (%s,%s,%s);"
    cs.execute(sql, tuple(courseInfo.split(',')))
    # **********end********** #


# 修改课程信息（通过课程编号修改课程名称），输入新课程信息格式为：Cno,Cname
def updateCourse(cs):
    courseInfo = input("请输入数据")
    'C1,Learn Python'
    # **********begin********** #
    sql = "update Course SET Cname='{Cname}' WHERE Cno='{Cno}'".format(Cname=(tuple(courseInfo.split(",")))[1], Cno=(tuple(courseInfo.split(",")))[0])
    cs.execute(sql)
    # **********end********** #
'''
(('C1', 'Learn Python', 'T1'), ('C10', '软件可靠性', 'T6'), ('C2', '大学计算机基础', 'T2'), ('C3', '数据库原理与技术', 'T2'), ('C4', '大学计算机基础', 'T5'), ('C5', '程序设计', 'T1'), ('C6', '程序设计', 'T4'), ('C7', '数字图像处理', 'T1'), ('C8', '抽象代数', 'T6'), ('C9', '离散数学', 'T5'))
'''

# 查询课程信息（通过课程编号查询课程信息），输入课程编号 Cno
# 将课程信息打印到控制台
def findCourseByCno(cs):
    courseId = input("请输入数据")
    'C1'
    # **********begin********** #
    sql = "SELECT * FROM Course WHERE Cno='%s'" % courseId
    cs.execute(sql)
    # **********end********** #
'''
(('C1', '大学计算机基础', 'T1'),)
(('C1', '大学计算机基础', 'T1'), ('C10', '软件可靠性', 'T6'), ('C2', '大学计算机基础', 'T2'), ('C3', '数据库原理与技术', 'T2'), ('C4', '大学计算机基础', 'T5'), ('C5', '程序设计', 'T1'), ('C6', '程序设计', 'T4'), ('C7', '数字图像处理', 'T1'), ('C8', '抽象代数', 'T6'), ('C9', '离散数学', 'T5'))

'''

# 删除课程信息（通过课程编号删除课程信息），输入课程编号 Cno
def deleteCourse(cs):
    courseId = input("请输入数据")
    # **********begin********** #
    sql = "DELETE FROM Course WHERE Cno='%s'" % courseId
    cs.execute(sql)
    # **********end********** #


# 通过教师名称查询课程名称并将其打印到控制台,输入教师名称 Tname
# 打印格式为：课程名  （一个课程名一行，不含其它字符）
def findCourseByTeacherName(cs):
    tname = input("请输入数据")

    '''
    05
    周海芳
    
    大学计算机基础
    程序设计
    数字图像处理
    '''
    # **********begin********** #
    sql = "SELECT Course.Cname FROM Course join Teacher on Course.Tno = Teacher.Tno WHERE Teacher.Tname='%s'" % tname
    cs.execute(sql)
    results = cs.fetchall()
    for result in results:
        print(result[0])

    # **********end********** #


# 通过课程名称查询教师名称并将其打印到控制台，输出课程名称 Cname
# 打印格式为：教师名  （一个教师名一行，不含其它字符）
def selectTeacherByCname(cs):
    cname = input("请输入数据")

    '''
    06
    大学计算机基础
    
    周海芳
    周竞文
    李暾
    '''
    # **********begin********** #
    sql = "SELECT Teacher.Tname FROM Course join Teacher on Course.Tno = Teacher.Tno WHERE Course.Cname='%s'" % cname
    cs.execute(sql)
    results = cs.fetchall()
    for result in results:
        print(result[0])

    # **********end********** #

def Test(cs):
    sql = "select * from Course"
    cs.execute(sql)
    courseInfo = cs.fetchall()
    print(courseInfo)


if __name__ == '__main__':
    conn = pymysql.connect(host='localhost', port=3306,
                           user='root', passwd='qaz3357375', db="test", charset='utf8')
    command = input("请输入数字")
    cs = conn.cursor()
    if command == '01':
        addCourse(cs)
    elif command == '02':
        updateCourse(cs)
    elif command == '03':
        findCourseByCno(cs)
    elif command == '04':
        deleteCourse(cs)
    elif command == '05':
        findCourseByTeacherName(cs)
    elif command == '06':
        selectTeacherByCname(cs)
    conn.commit()
    Test(cs)
    cs.close()
    conn.close()
