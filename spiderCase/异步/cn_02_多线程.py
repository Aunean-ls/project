import requests
from lxml import etree
import time
from concurrent.futures import ThreadPoolExecutor
from UA.UAPool import UserAgent
import random
import os


folder_name = 'video/'
if not os.path.exists(folder_name):
    os.makedirs(folder_name)
headers = {
    'User-Agent': random.choice(UserAgent())
}
start_time = time.time()


def downMP4(item):
    video_page_url = 'https://699pic.com/' + item
    video_page_response = requests.get(url=video_page_url, headers=headers)
    video_page_content = video_page_response.text
    sel = etree.HTML(video_page_content)
    video_name = sel.xpath("//div[@class='video-view-title clearfix']/h1/text()")[0].strip()
    video_url = 'https:' + sel.xpath('//video/source/@src')[0]
    response_video = requests.get(video_url).content
    with open(folder_name+video_name+".mp4", 'wb') as f:
        f.write(response_video)
    print(video_name + " 下载完成")


def parsePage():

    # 第一步，确定爬虫地址
    url = "https://699pic.com/album/video/0/1142643.html"
    # 第二步：发送请求
    response = requests.get(url=url, headers=headers, allow_redirects=True)
    # 第三步：获取数据
    html_content = response.text.replace("location.href = 'http://' + str;", "").replace("fxxkClone();", "")
    # 第四部：保存在本地
    # with open('shetuwang.html', 'w', encoding='utf-8') as f:
    #     f.write(html_content)

    sel = etree.HTML(html_content)

    item_list = sel.xpath('//ul[@class="clearfix"]/li/a[1]/@href')[0:2]

    # 使用线程池的方式修改
    # executor = ThreadPoolExecutor(4)
    # for item in item_list:
    #     executor.submit(downMP4, item)
    # executor.shutdown(True)

    with ThreadPoolExecutor(4) as executor:
        futures = executor.map(downMP4, item_list)

    # for future in futures:
    #     print(future)

    finish_time = time.time()
    print('下载总耗费时间：' + str(round(finish_time-start_time, 2)))


if __name__ == '__main__':
    parsePage()
