import requests
from spiderCase.登陆.验证码.chaojiying import Chaojiying_Client

headers = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)'
}
# 获取session对象
session = requests.session()


# 构建爬虫类
class BZDTSpider():
    def img_get(self):
        url = 'http://bzdt.ch.mnr.gov.cn/sbsm/supermap/codeImg.do'
        image = session.get(url=url, headers=headers).content
        with open('code.jpg', 'wb') as f:
            f.write(image)

    def login(self, code):

        login_url = 'http://bzdt.ch.mnr.gov.cn/sbsm/supermap/login.do'
        # 构建表单
        data = {
            'userName': '13272436629',
            'enPassWord': '626c4f9b0f43bc57460c4b71d3a8cf7d',
            'passWord': 'qaz3357375',
            'validataCade': code
        }

        response = session.post(url=login_url, data=data, headers=headers)
        print(response.text)  # 打印登陆后的信息
        # 保存登录后的信息
        with open('BZDT.html', 'w', encoding='utf-8') as f:
            f.write(response.text)


if __name__ == '__main__':
    BZDTSpider().img_get()  # 下载图片到本地
    chaojiying = Chaojiying_Client('13272436629', 'qaz3357375', '916819')
    im = open('code.jpg', 'rb').read()
    info = chaojiying.PostPic(im, 1004)
    print(info)
    code = info['pic_str']  # 获取验证码信息
    BZDTSpider().login(code)  # 登录
