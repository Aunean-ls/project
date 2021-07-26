import requests
import json

url = 'https://fanyi.baidu.com/sug'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0'
}
wd = input("请输入：")
data = {
    'kw': wd
}
response = requests.post(url=url, data=data, headers=headers).json()
print(response['data'])
info_list = response['data']
with open('baidufanyi.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(info_list, indent=2, ensure_ascii=False))








