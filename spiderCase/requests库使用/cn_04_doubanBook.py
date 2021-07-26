import requests
from lxml import etree
import random
import os

user_agent_list = [
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/61.0",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15"
]

header = {
    "User-Agent": random.choice(user_agent_list),
    'Cookie': 'll="118267"; bid=tbI1B79Sn4s; __utmc=30149280; gr_user_id=7d144cc7-0e9b-4d69-a7a7-1d6b658d115c; __utmc=81379588; _vwo_uuid_v2=DAC705D324A20044A0A31BD66101901EE|e7170573cd8abcb55a043a79e9368d92; gr_cs1_e2cfe00d-af0c-409f-9cf9-baf87899b372=user_id%3A0; _pk_ref.100001.3ac3=%5B%22%22%2C%22%22%2C1615193303%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_ses.100001.3ac3=*; dbcl2="227321226:12t9gxpvi+k"; ck=-Voe; __utmz=30149280.1615193332.2.2.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utma=30149280.203182467.1615173251.1615173251.1615193332.2; __utmz=81379588.1615193332.2.2.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utma=81379588.1202507266.1615174008.1615174008.1615193332.2; push_doumail_num=0; push_noty_num=0; gr_session_id_22c937bbd8ebd703f2d8e9445f7dfd03=ece6904a-1c95-4e9f-959c-82672a0c8a90; gr_cs1_ece6904a-1c95-4e9f-959c-82672a0c8a90=user_id%3A1; gr_session_id_22c937bbd8ebd703f2d8e9445f7dfd03_ece6904a-1c95-4e9f-959c-82672a0c8a90=true; __utmt_douban=1; __utmt=1; __utmb=30149280.8.10.1615193332; __utmb=81379588.8.10.1615193332; _pk_id.100001.3ac3=293d9e28a397bf6f.1615174008.2.1615194182.1615174008.; ct=y'
}


def parse(urls):
    for url in urls:
        print(url)
        html = requests.get(url, headers=header).content.decode('utf-8')
        sel = etree.HTML(html)
        li_list = sel.xpath('//*[@id="subject_list"]/ul/li')

        for li in li_list:
            try:
                link = li.xpath('./div/a/@href')[0]
                img_url = li.xpath('./div/a/img/@src')[0]

                info = li.xpath('./div[2]/div[1]/text()')[0].strip()
                info = str(info).split('/')
                author = info[0].rstrip()
                translator = info[1].strip()
                press = info[2].strip()
                # time = info[3].strip()
                price = info[4].strip()

                html = requests.get(url=link, headers=header).content.decode('utf-8')
                sel = etree.HTML(html)
            except Exception as e:
                print(e)
            try:
                title = sel.xpath('//h1/span/text()')[0]
                time = sel.xpath('//*[@id="info"]/text()[last()-11]')[0].strip()
                if time is '':
                    time = sel.xpath('//*[@id="info"]/text()[last()-9]')[0].strip()
                page = sel.xpath('//*[@id="info"]/text()[last()-9]')[0].strip()
                if len(page.split('-')) > 1:
                    page = sel.xpath('//*[@id="info"]/text()[last()-7]')[0].strip()
                binding = sel.xpath('//*[@id="info"]/text()[last()-5]')[0].strip()
                ISBN = sel.xpath('//*[@id="info"]/text()[last()-1]')[0].strip()
                score = sel.xpath('//*[@id="interest_sectl"]/div/div[2]/strong/text()')[0].strip()
                comments = sel.xpath('//*[@id="interest_sectl"]/div/div[2]/div/div[2]/span/a/span/text()')[0]
                print(title)

                with open('doubanBook.txt', 'a', encoding='utf-8') as f:

                    f.writelines([ISBN + ',', title + ',', author + ',', score + ',', price + ',', page
                                  + ',', time + ',', press + ',', translator + ',', binding + ',', comments + ',', link
                                  + ',', img_url + '\n'])

                path = 'doubanBook_img/'
                if not os.path.exists(path):
                    os.makedirs(path)
                img_data = requests.get(url=img_url, headers=header).content
                img_name = img_url.split('/')[-1]
                with open(path + img_name, 'wb') as f:
                    f.write(img_data)
            except Exception as e:
                print(e)


if __name__ == '__main__':
    urls = ['https://book.douban.com/tag/%E6%97%A5%E6%9C%AC%E6%96%87%E5%AD%A6?start={}&type=T'.format(i) for i in
            range(0, 60, 20)]
    parse(urls)
