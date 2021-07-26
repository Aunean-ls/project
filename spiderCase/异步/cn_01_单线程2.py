import requests
from lxml import etree
import time
from UA.UAPool import UserAgent
import random

headers = {
    'User-Agent': random.choice(UserAgent())
}

start_time = time.time()


def downMP4(html, names):
    video_name = names.replace("<strong>", '').replace('</strong>', '')+".mp4"
    video_url = "https:" + html
    response_video = requests.get(video_url).content
    with open(video_name, 'wb') as f:
        f.write(response_video)
    print(video_name + " 下载完成")


def parsePage():

    url = "https://ibaotu.com/tupian/gongjiangjingshen/7-0-0-0-0-0-0.html?format_type=0"
    # 第二步：发送请求
    response = requests.get(url=url, headers=headers)
    # 第三步：获取数据
    html_content = response.text

    sel = etree.HTML(html_content)
    video_list = sel.xpath('//video[@preload="none"]/@src')
    names = sel.xpath("//ul/li/@pr-data-title")

    for i in range(len(video_list)):
        downMP4(video_list[i], names[i])
    end_time = time.time()
    print("共耗时：{:.2f}".format(end_time-start_time))


if __name__ == '__main__':
    parsePage()











