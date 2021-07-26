# -*- coding: utf-8 -*-
import scrapy
import base64
# from zahopinPro.items import ZhaopinproItem

class ZhaopingSpider(scrapy.Spider):
    name = 'zhaoping'

    # allowed_domains = ['www.templates.com']
    # start_urls = ['http://www.xxx.com/']
    def start_requests(self):
        for i in range(1, 2):
            page = str(i) + '-alice'
            result = base64.b64encode(page.encode()).decode()
            url = 'http://localhost:8080/page/' + result + '/12/749'
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        id_list = response.xpath('//legend/a/@id').extract()

        edu_level_list = response.xpath('//*[@id="article-list"]//div/fieldset//div[1]/div[4]/text()').extract()
        create_time_list = response.xpath('//div[@class="info"]/span[2]/text()').extract()
        company_size_list = response.xpath('//div[@class="layui-row"]/div[@class="layui-col-md2"]/span/text()').extract()
        workingExp_list = response.xpath('//*[@id="article-list"]/div//fieldset//div[1]/div[3] /text()').extract()
        for i in id_list:
            result = base64.b64encode(i.encode()).decode()
            # print(result)
            detail_url = 'http://localhost:8080/getPosition?id=' + result
            req = scrapy.Request(url=detail_url, callback=self.detail_parse)
            req.meta['edu_level_list'] = edu_level_list
            req.meta['create_time_list'] = create_time_list
            req.meta['company_size_list'] = company_size_list
            req.meta['workingExp_list'] = workingExp_list
            yield req

    def detail_parse(self, response):
        company_name_list = []
        job_name_list = []
        salary_list = []
        city_name_list = []
        welfare_list = []
        responsibility_list = []
        place_list = []
        edu_level_list = []
        company_name = response.xpath('//*[@id="affix-side"]/div[1]/div/div/div[2]/p/text()').extract_first()
        company_name_list.append(company_name)

        job_name = response.xpath('//h3/text()').extract_first()
        job_name_list.append(job_name)

        salary = response.xpath('//div[@class="layui-card"]/div[2]/text()').extract_first()
        salary_list.append(salary)

        city_name = response.xpath('//*[@id="affix-side"]/div[1]//div[2]/span/text()').extract_first()
        city_name_list.append(city_name)

        welfare = response.xpath('//*[@id="article-list"]//div[2]//div[2]/text()').extract_first()
        welfare_list.append(welfare)

        if len(response.xpath('//*[@id="article-list"]//div[3]//div[2]/text()').extract()) == 0:
            responsibility = 'null'
        else:
            responsibility = response.xpath('//*[@id="article-list"]//div[3]//div[2]/text()').extract_first()
        responsibility_list.append(responsibility)

        place = response.xpath('//*[@id="article-list"]//div[4]/div/div[2]/text()').extract_first()
        place_list.append(place)

        edu_level_list.append(response.meta['edu_level_list'])
        req = scrapy.Request(url=self.start_urls, callback=self.data)
        req.meta['city_name_list'] = city_name_list
        yield req

    def data(self, response):
        print(response.meta['city_name_list'])

        # print(response.meta['edu_level_list'])
        # for i in range(len(company_name_list)):
        #     for j in range(i+1):
        #
        #         data = {
        #             'company_name': company_name_list[i],
        #             'edu_level_list': edu_level_list[i][j],
        #             'job_name': job_name_list[i],
        #             'salary': salary_list[i],
        #
        #             'city_name': city_name_list[i],
        #
        #             'welfare': welfare_list[i].replace(',', '，'),
        #             'responsibility': responsibility_list[i].replace(',', '，').replace('\xa0', ''),
        #             'place': place_list[i].replace(',', '，')
        #
        #         }
        #         print(data)
