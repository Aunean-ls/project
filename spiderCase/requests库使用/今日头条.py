import requests
import os
import json

url = 'https://www.toutiao.com/api/search/content/?'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0',
}
data_list = []
params = {
    'aid': 24,
    'app_name': 'web_search',
    'offset': 60,
    'format': 'json',
    'keyword': '动漫',
    'autoload': 'true',
    'count': 20,
    'en_qc': 1,
    'cur_tab': 1,
    'from': 'search_tab',
    'pd': 'synthesis',

}

response = requests.get(url=url, params=params, headers=headers).json()

try:

    for dic in response["data"]:

        if 'image_url' in dic.keys():
            img = dic['image_url']

        title = dic['title']
        data = {
            'title': title,
            'img': img
        }
        data_list.append(data)

        print(title, img)
        path = 'jinri_img/'
        if not os.path.exists(path):
            os.makedirs(path)
        img_data = requests.get(url=img, headers=headers).content
        img_name = img.split('/')[-1] + '.jpg'
        with open(path + img_name, 'wb') as f:
            f.write(img_data)

except Exception:
    print(Exception)
with open('jinri.json', 'w', encoding='utf-8') as file:
    file.write(json.dumps(data_list, indent=2, ensure_ascii=False))
