# -*- coding: utf-8 -*-
import scrapy
import copy

class QimingSpider(scrapy.Spider):
    name = 'qiming'
    # allowed_domains = ['5156edu.com']
    start_urls = ['http://xh.5156edu.com/xm/nu.html']

    def parse(self, response):
        last_name = '刘'
        name_list = response.xpath('//a[@class="fontbox"]/text()').extract()
        two_name_list = []
        for name in name_list:
            for name2 in name_list:
                two_name = name + name2
                two_name_list.append(two_name)
        name_list = name_list + two_name_list
        print(len(name_list))

        for name in name_list:
            form = {
                'isbz': '1',
                'txtName': last_name,
                'name': name,
                'rdoSex': '0',
                'data_type': '0',
                'cboYear': '2016',
                'cboMonth': '11',
                'cboDay': '25',
                'cboHour': '14 - 未时',
                'cboMinute': '8分',
                'pid': '长沙',
                'cid': '选择城市',
                'zty': '0'
            }
            url = 'https://www.threetong.com/ceming/baziceming/xingmingceshi.php'
            # post 的方法
            req = scrapy.FormRequest(url=url, formdata=form, callback=self.check_name_vaildate)
            req.meta['wanted_name'] = last_name + name

            yield req

    def check_name_vaildate(self, response):
        lishu_score = response.xpath('//div[@class="sm_pingfen"]/span[1]/text()').extract_first()[7:]
        bazi_score = response.xpath('//div[@class="sm_pingfen"]/span[2]/text()').extract_first()[9:]
        # print(lishu_score, bazi_score)
        if float(lishu_score) > 70 and float(bazi_score) > 70:
            print('你的名字为：', response.meta['wanted_name'], lishu_score, bazi_score)
