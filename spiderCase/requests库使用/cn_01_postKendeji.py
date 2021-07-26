import requests
import csv

url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0'
}
results = []
# input('请输入')
for i in range(1, 6):
    data = {
        'cname': '',
        'pid': '',
        'keyword': '天虹',
        'pageIndex': i,
        'pageSize': '10'
    }

    response = requests.post(url=url, data=data, headers=headers).json()
    info_list = (response['Table1'])

    for info in info_list:
        result = {
            'rank': info['rownum'],
            'storeName': info['storeName'] + '餐厅',
            'addressDetail': info['addressDetail'],
            'pro': info['pro'],
            'provinceName': info['provinceName'],
            'cityName': info['cityName']
        }
        results.append(result)
        print(result)

        # 第二种方式
        """
        rank = info['rownum'],
        storeName = info['storeName'] + '餐厅',
        addressDetail = info['addressDetail'],
        pro = info['pro'],
        provinceName = info['provinceName'],
        cityName = info['cityName']

        with open('storeData.csv', 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([rank, storeName, addressDetail, pro, provinceName, cityName])
        """

with open('storeData.csv', 'w', newline='', encoding='utf-8') as f:
    fieldnames = ['rank', 'storeName', 'addressDetail', 'pro', 'provinceName', 'cityName']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(results)
