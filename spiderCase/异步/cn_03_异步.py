import requests
from lxml import etree
import time
from UA.UAPool import UserAgent
import random
import os
import asyncio
import aiohttp
from concurrent.futures import ThreadPoolExecutor

folder_name = 'video/'
if not os.path.exists(folder_name):
    os.makedirs(folder_name)
headers = {
    'User-Agent': random.choice(UserAgent())
}
start_time = time.time()


async def downMP4(html, names):
    video_name = names.replace("<strong>", '').replace('</strong>', '')+".mp4"
    video_url = "https:" + html

    # 同步下载
    # response_video = requests.get(video_url).content
    # with open(folder_name+video_name, 'wb') as f:
    #     f.write(response_video)
    # print(video_name + " 下载完成")

    # 异步下载
    async with aiohttp.ClientSession() as session:
        async with session.get(url=video_url, headers=headers) as video_response:
            video_content = await video_response.read()
            with open(folder_name+video_name, 'wb') as f:
                f.write(video_content)
        print(video_name + " 下载完成")


def parsePage():
    # 第一步，确定爬虫地址
    url = "https://ibaotu.com/tupian/gongjiangjingshen/7-0-0-0-0-0-0.html?format_type=0"
    # 第二步：发送请求
    response = requests.get(url=url, headers=headers)
    # 第三步：获取数据
    html_content = response.text

    sel = etree.HTML(html_content)
    video_list = sel.xpath('//video[@preload="none"]/@src')
    names = sel.xpath("//ul/li/@pr-data-title")

    # 多线程
    # executor = ThreadPoolExecutor(4)
    # for i in range(len(video_list)):
    #     executor.submit(downMP4, video_list[i], names[i])
    # executor.shutdown(True)

    # 协程
    loop = asyncio.get_event_loop()
    downMP4Task = []
    for i in range(len(video_list)):
        downMP4Proxy = downMP4(video_list[i], names[i])
        future = asyncio.ensure_future(downMP4Proxy)
        downMP4Task.append(future)
    loop.run_until_complete(asyncio.wait(downMP4Task))
    loop.close()

    finish_time = time.time()
    print('下载总耗费时间：' + str(round(finish_time-start_time, 2)))


if __name__ == '__main__':
    parsePage()

