import requests
from lxml import etree
from spiderCase.登陆.验证码.chaojiying import Chaojiying_Client

# 设置全局变量U-A
headers = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)'
}
session = requests.session()


class Spider():

    def __init__(self):
        self.VIEWSTATE = None,
        self.VIEWSTATEGENERATOR = None

    def img_get(self):
        #
        url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'

        response = session.get(url=url, headers=headers)
        response.encoding = response.apparent_encoding
        html = response.text
        sel = etree.HTML(html)
        self.VIEWSTATE = sel.xpath('//form/div/input[@name="__VIEWSTATE"]/@value')[0]

        self.VIEWSTATEGENERATOR = sel.xpath('//form/div/input[@name="__VIEWSTATEGENERATOR"]/@value')[0]

        image_url = 'https://so.gushiwen.cn/' + sel.xpath('//img[@id="imgCode"]/@src')[0]

        image = session.get(image_url, headers=headers).content
        with open('imageverify.jpg', 'wb') as file:
            file.write(image)

        # self.login(self.VIEWSTATE, self.VIEWSTATEGENERATOR)

    def login(self, code):
        # 登陆所需表单
        self.data = {
            '__VIEWSTATE': self.VIEWSTATE,
            '__VIEWSTATEGENERATOR': self.VIEWSTATEGENERATOR,
            'from': 'http://so.gushiwen.cn/user/collect.aspx',
            'email': '13272436629',
            'pwd': 'qaz3357375',
            'code': code,
            'denglu': '登录',
        }
        # 登陆的url
        login_url = 'https://so.gushiwen.cn/user/login.aspx'
        response = session.post(url=login_url, data=self.data, headers=headers)
        print(response.history)
        self.crawler()
        
    def crawler(self):
        # 内容页的url
        verify_url = 'http://so.gushiwen.cn/user/collect.aspx'
        verify_response = session.get(url=verify_url, data=self.data)
        html = verify_response.text
        sel = etree.HTML(html)
        # 验证是否登陆成功，获取登陆后的手机号码
        phone = sel.xpath('//div[@class="shisoncont"]/div[3]/span/text()')[0]
        print(phone)


if __name__ == '__main__':

    Spider().img_get()  # 下载图片
    chaojiying = Chaojiying_Client('13272436629', 'qaz3357375', '916819')
    im = open('imageverify.jpg', 'rb').read()
    info = chaojiying.PostPic(im, 1004)
    print(info)
    code = info['pic_str']  # 获取验证码信息
    Spider().login(code)


