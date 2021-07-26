import requests
from lxml import etree
import time
from UA.UAPool import UserAgent
import random

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
    with open(video_name, 'wb') as f:
        f.write(response_video)
    print(video_name + " 下载完成")


def parsePage():
    start_time = time.time()
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

    for item in item_list:
        # video = 'https://699pic.com' + item
        downMP4(item)
    end_time = time.time()
    print("共耗时：{:.2f}".format(end_time-start_time))


if __name__ == '__main__':
    parsePage()











