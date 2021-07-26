import scrapy
from gushiwenPro.chaojiying import Chaojiying_Client
import requests
from scrapy.http import Request, FormRequest


class GushiwenSpider(scrapy.Spider):
    name = 'gushiwen'
    # allowed_domains = ['www.templates.com']
    start_urls = ['https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx']
    headers = {
        'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)'
    }
    login_url = start_urls[0]

    def start_requests(self):
        return [Request("https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx",
                        callback=self.Login, meta={"cookiejar": 1})]

    def Login(self, response):
        VIEWSTATE = response.xpath('//form/div/input[@name="__VIEWSTATE"]/@value').extract_first()
        VIEWSTATEGENERATOR = response.xpath('//form/div/input[@name="__VIEWSTATEGENERATOR"]/@value').extract_first()
        image_url = 'https://so.gushiwen.cn/' + response.xpath('//img[@id="imgCode"]/@src').extract_first()
        session = requests.session()
        image = session.get(image_url, headers=self.headers).content
        with open('imageverify.jpg', 'wb') as file:
            file.write(image)
        chaojiying = Chaojiying_Client('13272436629', 'qaz3357375', '916819')
        im = open('imageverify.jpg', 'rb').read()
        info = chaojiying.PostPic(im, 1004)
        print(info)
        code = info['pic_str']
        data = {
            '__VIEWSTATE': VIEWSTATE,
            '__VIEWSTATEGENERATOR': VIEWSTATEGENERATOR,
            'from': 'http://so.gushiwen.cn/user/collect.aspx',
            'email': '13272436629',
            'pwd': 'qaz3357375',
            'code': code,
            'denglu': '登录',
        }

        return [FormRequest.from_response(response,
                                          meta={"cookiejar": response.meta["cookiejar"]},
                                          headers=self.headers,
                                          formdata=data,
                                          callback=self.crawlerdata,
                                          )]

        # yield scrapy.FormRequest(url=self.login_url, meta={'cookiejar': response.meta['cookiejar']},
        #                          headers=self.headers, formdata=data, callback=self.crawlerdata)

    def crawlerdata(self, response):
        print(response.text)
        yield scrapy.Request("http://so.gushiwen.cn/user/collect.aspx", meta={'cookiejar': True}, callback=self.parse_manager)

    def parse_manager(self, response):
        print('*'*20)
        print(response.text)


    # def parse(self, response):
    #     session = requests.session()
    #     VIEWSTATE = response.xpath('//form/div/input[@name="__VIEWSTATE"]/@value').extract_first()
    #     VIEWSTATEGENERATOR = response.xpath('//form/div/input[@name="__VIEWSTATEGENERATOR"]/@value').extract_first()
    #     image_url = 'https://so.gushiwen.cn/' + response.xpath('//img[@id="imgCode"]/@src').extract_first()
    #     image = session.get(image_url, headers=self.headers).content
    #     with open('imageverify.jpg', 'wb') as file:
    #         file.write(image)
    #     chaojiying = Chaojiying_Client('13272436629', 'qaz3357375', '916819')
    #     im = open('imageverify.jpg', 'rb').read()
    #     info = chaojiying.PostPic(im, 1004)
    #     print(info)
    #     code = info['pic_str']
    #     data = {
    #         '__VIEWSTATE': VIEWSTATE,
    #         '__VIEWSTATEGENERATOR': VIEWSTATEGENERATOR,
    #         'from': 'http://so.gushiwen.cn/user/collect.aspx',
    #         'email': '13272436629',
    #         'pwd': 'qaz3357375',
    #         'code': code,
    #         'denglu': '登录',
    #     }
    #     print(data)
    #
    #     login_url = 'https://so.gushiwen.cn/user/login.aspx'
    #     response = session.post(url=login_url, data=data, headers=self.headers)
    #     print(response.text)
    # from lxml import etree
    # verify_url = 'http://so.gushiwen.cn/user/collect.aspx'
    # verify_response = session.get(url=verify_url, data=data)
    # html = verify_response.text
    # sel = etree.HTML(html)
    # # 验证是否登陆成功，获取登陆后的手机号码
    # phone = sel.xpath('//div[@class="shisoncont"]/div[3]/span/text()')[0]
    # print(phone)
    #     yield scrapy.FormRequest(url=self.login_url, meta={'cookiejar': 1},
    #                              headers=self.headers, formdata=data, callback=self.parse_afterlogin)
    #
    # # 登录后继续使用该cookie信息去访问登录后才能访问的页面，就不会被拦截到登录页面了
    # def parse_afterlogin(self, response):
    #     print(response.text)
