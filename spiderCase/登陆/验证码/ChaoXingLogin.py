import requests
from lxml import etree
from PIL import Image
from io import BytesIO
import time

# 登录url
url = 'http://passport2.chaoxing.com/login?refer=http%3A%2F%2Fhnkjxy.fanya.chaoxing.com'

headers = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)'
}
# 获取session对象
session = requests.session()


def login():
    # 获取图片的url
    image_url = 'http://passport2.chaoxing.com/num/code?' + str(time.time())
    image = session.get(image_url, headers=headers).content
    with open('imageverify.jpg', 'wb') as file:
        file.write(image)
    img = Image.open(BytesIO(image))
    img.show()
    img.close()

    code = input("请输入验证码：")
    data = {
        'refer_0x001': 'http%3A%2F%2Fhnkjxy.fanya.chaoxing.com',
        'pid': '-1',
        'pidName': '',
        'fid': '2401',
        'fidName': '湖南科技职业学院',
        'allowJoin': '0',
        'isCheckNumCode': '1',
        'f': '0',
        'productid': '',
        't': 'true',
        'uname': '13272436629',
        'password': 'cWEzMzU3Mzc1',
        'numcode': code,
        'verCode': ''
    }
    response = session.post(url=url, data=data, headers=headers).text
    return response


def crawler(response):
    sel = etree.HTML(response)

    # 打印学校名称
    title = sel.xpath('//title/text()')[0].strip()
    print(title)
    # 获取推荐课程数据
    datas = sel.xpath('//div[@class="tj_cour leftF"]/ul/li')
    for info in datas:
        # 排行
        num = info.xpath('./div/span[1]/text()')[0]
        # 课程名
        title = info.xpath('./div/a/@title')[0]
        # 老师名
        teacher = info.xpath('./div/p[2]/text()')[0].replace('教师： ', '').strip()
        # 观看数
        watcher = info.xpath('./div/span[2]/text()')[0]

        dic1 = {
            'row': num,
            'title': title,
            'teacher': teacher,
            'watcher': watcher
        }
        print(dic1)


if __name__ == '__main__':
    response = login()
    crawler(response)

