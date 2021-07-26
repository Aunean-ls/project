import scrapy
from chaoxingPro.chaojiying import Chaojiying_Client
import time
import requests


class ChaoxingSpider(scrapy.Spider):
    name = 'chaoxing'
    # allowed_domains = ['www.templates.com']
    start_urls = ['https://passport2.chaoxing.com/login']

    login_url = start_urls[0]
    # url = 'http://passport2.chaoxing.com/login?refer=http%3A%2F%2Fhnkjxy.fanya.chaoxing.com'
    headers = {
        'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)',
        # 'Cookie': 'route=98f17f0b052079b916f022bfaec8cf55; JSESSIONID=3018F693014C35D9E81E8EFB56B81E08; isfyportal=1; uname=13272436629; lv=1; fid=2401; pid=43897; _uid=108212747; uf=da0883eb5260151e5b714e8a11f97f736bd90470aabe0d3ea1070773eceafb0d874c7fab090ed98f861cac58e15dcf37913b662843f1f4ad6d92e371d7fdf64439b1b6d2dc18bd783341727ca9b9739f5558ebfe920d455c9cf486533594d13579f7e6e0c70bd528; _d=1623810810287; UID=108212747; vc=14C28E4DDEDEAABF9AC1D529DA5D6F93; vc2=BE48D2DE853448C3DC7EEDF25965ECB5; vc3=U8BQCxbYhIyVVn3J9528QvfjNwJpb%2BxdN%2FzVEesw1KnyYwb%2FRV9TL1JweqUkk59mJFq9WElehmbg1oTCxDG8sGY7PR%2F%2FZZcLYgbf07xtvYSwUG3j45x4NDOuXba5KDODgJtfLxG9rNoCJWPIUCFNMZzk8AnTCzezbnpXBgWMBHo%3D5e817f95202e0e5d798f2c7fdc59a604; xxtenc=441652e4382ce0240d4eb7108e154dc2; DSSTASH_LOG=C_38-UN_1063-US_108212747-T_1623810810289; fanyamoocs=1283EE8DB0E9DA0138B2E9C12A94008E; _dd108212747=1623810811117; thirdRegist=0; tl=1'
    }
    session = requests.session()

    def start_requests(self):
        return [scrapy.Request(self.start_urls[0], callback=self.parse)]

    def parse(self, response):
        # 拼凑当前验证码对应的 url
        img_url = 'http://passport2.chaoxing.com/num/code?' + str(time.time())
        yield scrapy.Request(url=img_url, meta={'cookiejar': 1}, callback=self.parse_postdata)

    def parse_postdata(self, response):
        print("正在登录...................")
        # 保存验证码图片 并且自动打开后 人工输入验证码
        fp = open('imageverify.jpg', 'wb')
        fp.write(response.body)
        fp.close()

        chaojiying = Chaojiying_Client('13272436629', 'qaz3357375', '916819')
        im = open('imageverify.jpg', 'rb').read()
        info = chaojiying.PostPic(im, 4004)
        code = info['pic_str']

        formdata = {
            'refer_0x001': 'http%3A%2F%2Fhnkjxy.fanya.chaoxing.com',
            'pid': '-1',
            'pidName': '',
            'fid': '2401',
            'allowJoin': '0',
            'isCheckNumCode': '1',
            'f': '0',
            'productid': '',
            't': 'true',
            'uname': 'MTMyNzI0MzY2Mjk=',
            'password': 'cWEzMzU3Mzc1',
            'numcode': code,
            'verCode': ''
        }

        yield scrapy.FormRequest(url=self.login_url, meta={'cookiejar': response.meta['cookiejar']},
                                 headers=self.headers, formdata=formdata, callback=self.parse_afterlogin)
        # yield scrapy.FormRequest.from_response(response,
        #                                   meta={"cookiejar": response.meta["cookiejar"]},
        #                                   # headers=self.headers,
        #                                   formdata=formdata,
        #                                   callback=self.parse_afterlogin,
        #                                   )

    def parse_afterlogin(self, response):
        print(response.text)
        # 访问登陆后才能访问的页面http://i.mooc.chaoxing.com/settings/info?t=1594542872701
        yield scrapy.Request("http://i.mooc.chaoxing.com/settings/info", meta={'cookiejar': True},
                             callback=self.parse_manager)

    # 保存文件
    def parse_manager(self, response):
        print(response.text)
        pass

    # def start_requests(self):
    #     return [scrapy.FormRequest('http://passport2.chaoxing.com/login?refer=http%3A%2F%2Fhnkjxy.fanya.chaoxing.com',
    #                                headers=self.headers, meta={"cookiejar":1}, callback=self.parse_before_login)]
    #
    # def parse_before_login(self, response):
    #     url = 'http://passport2.chaoxing.com/num/code?' + str(time.time())
    #     image = requests.get(url=url).content
    #     with open('imageverify.jpg', 'wb') as file:
    #         file.write(image)
    #     chaojiying = Chaojiying_Client('13272436629', 'qaz3357375', '916819')
    #     im = open('imageverify.jpg', 'rb').read()
    #     info = chaojiying.PostPic(im, 4004)
    #     code = info['pic_str']
    #
    #     formdata = {
    #         'refer_0x001': 'http%3A%2F%2Fhnkjxy.fanya.chaoxing.com',
    #         'pid': '-1',
    #         'pidName': '',
    #         'fid': '2401',
    #         'fidName': '湖南科技职业学院',
    #         'allowJoin': '0',
    #         'isCheckNumCode': '1',
    #         'f': '0',
    #         'productid': '',
    #         't': 'true',
    #         'uname': '13272436629',
    #         'password': 'cWEzMzU3Mzc1',
    #         'numcode': code,
    #         'verCode': ''
    #     }
    #     print(formdata)
    #
    #     yield scrapy.FormRequest.from_response(response, meta={"cookiejar": response.meta["cookiejar"]},
    #                                             headers=self.headers, formdata=formdata, callback=self.parse_after_login)
    #
    # def parse_after_login(self, response):
    #     print(response.text)
    #     title = response.xpath('//title/text()').extract_first()
    #     print(title)

    # def parse(self, response):
    #     url = 'http://passport2.chaoxing.com/num/code?' + str(time.time())
    #     image = requests.get(url=url).content
    #     with open('imageverify.jpg', 'wb') as file:
    #         file.write(image)
    #     chaojiying = Chaojiying_Client('13272436629', 'qaz3357375', '916819')
    #     im = open('imageverify.jpg', 'rb').read()
    #     info = chaojiying.PostPic(im, 4004)
    #     code = info['pic_str']
    #
    #     data = {
    #         'refer_0x001': 'http%3A%2F%2Fhnkjxy.fanya.chaoxing.com',
    #         'pid': '-1',
    #         'pidName': '',
    #         'fid': '2401',
    #         'fidName': '湖南科技职业学院',
    #         'allowJoin': '0',
    #         'isCheckNumCode': '1',
    #         'f': '0',
    #         'productid': '',
    #         't': 'true',
    #         'uname': '13272436629',
    #         'password': 'cWEzMzU3Mzc1',
    #         'numcode': code,
    #         'verCode': ''
    #     }
    #     yield scrapy.FormRequest.from_response(response, formdata=data, callback=self.after_login)
    #
    # def after_login(self, response):  # 验证是否请求成功
    #     print(response.text)

    # def start_requests(self):
    #     url = 'http://passport2.chaoxing.com/num/code?' + str(time.time())
    #     image = requests.get(url=url).content
    #     with open('imageverify.jpg', 'wb') as file:
    #         file.write(image)
    #     chaojiying = Chaojiying_Client('13272436629', 'qaz3357375', '916819')
    #     im = open('imageverify.jpg', 'rb').read()
    #     info = chaojiying.PostPic(im, 4004)
    #     code = info['pic_str']
    #     req = scrapy.Request(url=self.login_url, meta={'cookiejar': 1}, callback=self.chaoxing_login)
    #     req.meta['code'] = code
    #     yield req
    #
    # def chaoxing_login(self, response):
    #
    #     data = {
    #         'refer_0x001': 'http%3A%2F%2Fhnkjxy.fanya.chaoxing.com',
    #         'pid': '-1',
    #         'pidName': '',
    #         'fid': '2401',
    #         'fidName': '湖南科技职业学院',
    #         'allowJoin': '0',
    #         'isCheckNumCode': '1',
    #         'f': '0',
    #         'productid': '',
    #         't': 'true',
    #         'uname': '13272436629',
    #         'password': 'cWEzMzU3Mzc1',
    #         'numcode': response.meta['code'],
    #         'verCode': ''
    #     }
    #     print(response.meta['code'])
    #     req = scrapy.FormRequest(url=self.login_url, headers=self.headers, formdata=data, callback=self.parse_page)
    #     url = 'http://i.mooc.chaoxing.com/space/index.shtml'
    #     return [scrapy.FormRequest.from_response(response, headers=self.headers, formdata=data,
    #                                              meta={'cookie': response.meta['cookiejar']},
    #                                              callback=self.parse_page, dont_filter=True)]
    #     # req = scrapy.FormRequest(headers=self.headers, url=self.url, formdata=data,
    #     #                                        meta={'cookie': response.meta['cookiejar']},
    #     #                                        callback=self.parse_page, dont_click=True)
    #     # yield req
    #     # yield scrapy.FormRequest("http://passport2.chaoxing.com/login?refer=http%3A%2F%2Fhnkjxy.fanya.chaoxing.com",
    #     #                          formdata=form_data, callback=self.parse_page)
    #
    # def parse_page(self, response):
    #     # 打印登录成功后的学校名称
    #     print(response.text)
    #     # name = response.xpath('//title/text()').extract_first()
    #     # print(name)
