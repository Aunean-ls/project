import requests
from lxml import etree
import time
from UA.UAPool import UserAgent
import random
import os
import re
import asyncio

# 存放位置
folder_name = 'video/'
if not os.path.exists(folder_name):
    os.makedirs(folder_name)
headers = {
    'User-Agent': random.choice(UserAgent())
}
# 设置开始下载时间
start_time = time.time()
# 获取时间戳
target = "https://www.pearvideo.com/videoStatus.jsp?contId="


async def downMP4(item):
    # 视频下载
    url_num = item.replace('video_', '')
    url = target + url_num
    headers2 = {
        'User-Agent': random.choice(UserAgent()),
        'Referer': 'https://www.pearvideo.com/video_' + str(url_num)
    }
    # 获取视频地址
    html = requests.get(url=url, headers=headers2).text
    cont = 'cont-' + str(url_num)
    srcUrl = re.findall(f'"srcUrl":"(.*?)"', html)[0]
    # 拼接替换获取具体地址
    video_url = srcUrl.replace(srcUrl.split("-")[0].split("/")[-1], cont)

    # 获取视频名称
    video_page_url = 'https://www.pearvideo.com/' + item
    video_page_response = requests.get(url=video_page_url, headers=headers)
    video_page_content = video_page_response.text
    sel = etree.HTML(video_page_content)
    video_name = sel.xpath("//h1/text()")[0].strip()

    # 视频存储
    response_video = requests.get(video_url).content
    with open(folder_name+video_name, 'wb') as f:
        f.write(response_video)
    print(video_name + " 下载完成")


def parsePage():
    # 第一步，确定爬虫地址
    url = "https://www.pearvideo.com/category_8"
    # 第二步：发送请求
    response = requests.get(url=url, headers=headers)
    # 第三步：获取数据
    html_content = response.text
    with open('shetuwang1.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    sel = etree.HTML(html_content)
    item_list = sel.xpath('//ul[@class="category-list clearfix"]/li/div/a/@href')[0:3]

    loop = asyncio.get_event_loop()
    downMP4Task = []
    for i in range(len(item_list)):
        downMP4Proxy = downMP4(item_list[i])
        future = asyncio.ensure_future(downMP4Proxy)
        downMP4Task.append(future)
    loop.run_until_complete(asyncio.wait(downMP4Task))
    loop.close()

    finish_time = time.time()
    print("共耗时：{:.2f}".format(finish_time-start_time))


if __name__ == '__main__':
    parsePage()










