import requests
from lxml import etree
import time
from UA.UAPool import UserAgent
import random
import os
import asyncio
import aiohttp

folder_name = 'images/'
if not os.path.exists(folder_name):
    os.makedirs(folder_name)
headers = {
    'User-Agent': random.choice(UserAgent())
}
start_time = time.time()
page = 0
all_data = []
downIMGTask = []


async def downIMG(img_url, img_name):
    # 异步下载
    async with aiohttp.ClientSession() as session:
        async with session.get(url=img_url, headers=headers) as video_response:
            video_content = await video_response.read()
            with open(folder_name + img_name, 'wb') as f:
                f.write(video_content)
        # print(img_name + " 下载完成")


def parsePage(url):

    # 第二步：发送请求
    response = requests.get(url=url, headers=headers)
    # 第三步：获取数据
    html_content = response.text

    sel = etree.HTML(html_content)
    li_list = sel.xpath('//ul[@class="clearfix"]/li')
    for li in li_list:
        detail_url = li.xpath('./a/@href')[0]
        detail_url = 'http://pic.netbian.com' + detail_url
        response = requests.get(url=detail_url, headers=headers).content.decode('gbk')
        sel = etree.HTML(response)
        img_url = sel.xpath('//div[@class="photo-pic"]/a/img/@src')[0]
        img_url = 'http://pic.netbian.com' + img_url
        img_name = sel.xpath('//div[@class="photo-pic"]/a/img/@title')[0] + '.jpg'
        data = {
            'img_url': img_url,
            'img_name': img_name
        }
        print(data)
        all_data.append(data)


def async1():
    # 协程
    loop = asyncio.get_event_loop()
    for i in range(len(all_data)):
        downIMGProxy = downIMG(all_data[i]['img_url'], all_data[i]['img_name'])
        future = asyncio.ensure_future(downIMGProxy)
        downIMGTask.append(future)
    loop.run_until_complete(asyncio.wait(downIMGTask))
    loop.close()


if __name__ == '__main__':
    urls = ['http://pic.netbian.com/4kdongman/index_{}.html'.format(i) for i in range(2, 10)]
    for url in urls:
        parsePage(url)
    async1()
    print('下载总耗费时间：' + str(round(time.time() - start_time, 2)))
