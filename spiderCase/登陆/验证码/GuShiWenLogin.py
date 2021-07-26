import requests
from lxml import etree
import pytesseract
from PIL import Image
from io import BytesIO

# 设置全局变量U-A
headers = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)'
}
session = requests.session()


def login():
    #
    url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'

    response = session.get(url=url, headers=headers)
    response.encoding = response.apparent_encoding
    html = response.text
    sel = etree.HTML(html)

    VIEWSTATE = sel.xpath('//form/div/input[@name="__VIEWSTATE"]/@value')[0]
    VIEWSTATEGENERATOR = sel.xpath('//form/div/input[@name="__VIEWSTATEGENERATOR"]/@value')[0]

    image_url = 'https://so.gushiwen.cn/' + sel.xpath('//img[@id="imgCode"]/@src')[0]

    image = session.get(image_url, headers=headers).content
    with open('imageverify.jpg', 'wb') as file:
        file.write(image)

    # 灰度图处理
    img = Image.open(BytesIO(image))
    img.show()
    # img = img.convert('L')  # 转化为灰度图像 1：二值图像  L：灰度图像
    # threshold = 200
    # table = []
    # for i in range(256):
    #     if i < threshold:
    #         table.append(0)
    #     else:
    #         table.append(1)
    # img = img.point(table, "1")
    # security_code = pytesseract.image_to_string(img)
    # print(security_code)
    img.close()

    # 手动输入验证码
    code = input('请输入验证码:')
    # 登陆所需表单
    data = {
        '__VIEWSTATE': VIEWSTATE,
        '__VIEWSTATEGENERATOR': VIEWSTATEGENERATOR,
        'from': 'http://so.gushiwen.cn/user/collect.aspx',
        'email': '13272436629',
        'pwd': 'qaz3357375',
        'code': code,
        'denglu': '登录',
    }
    # 登陆的url
    login_url = 'https://so.gushiwen.cn/user/login.aspx'
    response = session.post(url=login_url, data=data, headers=headers)
    print(response.history)
    return data


def crawler(data):
    # 内容页的url
    verify_url = 'http://so.gushiwen.cn/user/collect.aspx'
    verify_response = session.get(url=verify_url, data=data)
    html = verify_response.text
    sel = etree.HTML(html)
    # 验证是否登陆成功，获取登陆后的手机号码
    phone = sel.xpath('//div[@class="shisoncont"]/div[3]/span/text()')[0]
    print(phone)


if __name__ == '__main__':
    data = login()
    crawler(data)

