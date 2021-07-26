import pandas as pd
import requests
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)'
}
all_data = []
url_list = ['http://www.tianqihoubao.com/lishi/changsha/month/20210{}.html'.format(i) for i in range(1, 5)]
for url in url_list:
    response = requests.get(url=url, headers=headers).content.decode('gbk')
    sel = etree.HTML(response)

    tr_list = sel.xpath('//table/tr[position()>1]')

    for tr in tr_list:
        time = tr.xpath('./td[1]/a/text()')[0].strip()
        weather = tr.xpath('./td[2]/text()')[0].replace('\r\n', '').replace(' ', '').strip()
        tem = tr.xpath('./td[3]/text()')[0].replace('\r\n', '').replace(' ', '').strip()
        wind = tr.xpath('./td[4]/text()')[0].replace('\r\n', '').replace(' ', '').strip()

        data = {
            'time': time,
            'weather': weather,
            'tem': tem,
            'wind': wind
        }
        print(data)
        all_data.append(data)

df = pd.DataFrame(data=all_data, columns=['time', 'weather', 'tem', 'wind'])
df.to_excel("D:/info/dataWeather.xls", encoding='gbk', index=False)
