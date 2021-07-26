import scrapy


class TougeSpider(scrapy.Spider):
    name = 'touge'
    # allowed_domains = ['www.templates.com']
    start_urls = ['https://data.educoder.net/api/accounts/login.json']
    url = 'https://data.educoder.net/api/accounts/login.json'
    headers = {
        'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)',
        'Referer': 'https://www.educoder.net/',
    }

    def start_requests(self):
        # 登录参数
        data = {
            'autologin': 'true',
            'login': "13272436629",
            'password': "qaz3357375"
        }
        yield scrapy.FormRequest(url=self.url, formdata=data, meta={'cookiejar': 1}, callback=self.after_login)

    def after_login(self, response):
        print(response.text)
        print(response.meta['cookiejar'])
        yield scrapy.Request('https://data.educoder.net/api/users/get_user_info.json?school=1',
                             meta={'cookiejar': response.meta['cookiejar']},
                             headers=self.headers, callback=self.user_account)

    def user_account(self, response):
        # 打印账号管理界面信息
        print(response.text)

