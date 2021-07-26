import requests
import os

url = 'https://movie.douban.com/j/search_subjects?'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0'
}
params = {
    'type': 'movie',
    'tag': '热门',
    'sort': 'recommend',
    'page_limit': '20',
    'page_start': '0',
}

response = requests.get(url=url, params=params, headers=headers).json()
dic = response['subjects']
for i in dic:
    data = {
        'title': i['title'],
        'score': i['rate'],
        'img': i['cover'],
    }
    img = data['img']
    title = data['title']
    print(data)
    path = 'douban_img/'
    if not os.path.exists(path):
        os.makedirs(path)
    img_data = requests.get(url=img, headers=headers).content
    img_name = title + '.' + img.split('.')[-1]
    with open(path + img_name, 'wb') as f:
        f.write(img_data)

