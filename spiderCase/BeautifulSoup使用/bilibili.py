import requests
from bs4 import BeautifulSoup

# 步骤一：确定url
url = 'https://search.bilibili.com/all?'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
}

# 存放内容
content = []
# 步骤二：发送 HTTP 请求
word = input('请输入搜索关键字：')
end_page = input('请输入结束页：')

for page in range(1, int(end_page) + 1):
    params = {
        'keyword': word,
        'page': str(page)
    }
    # 步骤三：获取响应数据
    response = requests.get(url=url, headers=headers, params=params).content.decode('utf-8')

    # 步骤四：数据解析
    soup = BeautifulSoup(response, 'lxml')

    li_list = soup.select('ul.video-list.clearfix > li')
    for i in range(len(li_list)):
        # 标题
        title = li_list[i].select('a.title')[0]['title']
        # 视频时长
        duration = li_list[i].select('a > div.img > span.so-imgTag_rb')[0].text
        tg = li_list[i].select('div > div.tags > span')
        # 观看人数
        person_number = tg[0].text.strip()
        # 弹幕数量
        comment_number = tg[1].text.strip()
        # 上传时间
        time = tg[2].text.strip()
        # up主
        up = tg[3].text

        data = {
            'title': title,
            'duration': duration,
            'person_number': person_number,
            'comment_number': comment_number,
            'time': time,
            'up': up,
        }
        print(data)
        content.append(data)

# 步骤五：存储数据
for value in content:
    with open('bilibili.txt', 'a', encoding='utf-8') as f:
        f.write(str(value) + '\n')



