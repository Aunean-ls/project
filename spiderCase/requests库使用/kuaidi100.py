import requests
import time

url1 = "https://www.kuaidi100.com/autonumber/autoComNum?"
url2 = "https://www.kuaidi100.com/query?"

orderNum = input("请输入快递单号：")
data = {
    "text": orderNum
}
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
}

response = requests.post(url1, data=data, headers=header)
content = response.json()
info_list = content["auto"]
for list in info_list:
    timestamp = str(time.time())
    comCode = list['comCode']
    param = {
        'type': comCode,
        'postid': orderNum,
        'temp': timestamp,
        'phone': ''
    }
    response2 = requests.get(url2, params=param, headers=header)
    content2 = response2.json()
    info_list2 = content2["data"]
    for list in info_list2:
        time = list["time"]
        context = list["context"]
        ftime = list["ftime"]
        print(time, context, ftime)


