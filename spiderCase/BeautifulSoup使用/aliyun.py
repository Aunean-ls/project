import requests
from bs4 import BeautifulSoup

# 设置 U-A
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)'
}


def crawle(url):
    # 步骤二三：发送HTTP请求，获取响应数据
    response = requests.get(url=url, headers=headers).content.decode('utf-8')

    # 步骤四：数据解析
    # 构建bs4对象
    soup = BeautifulSoup(response, 'lxml')
    # 文章标题
    title = soup.select('h1')[1].text
    # 简介
    intro = soup.select('div.article-desc > span')[0].text
    # 文章内容
    content_list = soup.select('div.article-inner.markdown-body > p')
    content_text = ''
    for content in content_list:
        content_text += content.text.strip() + '\n'

    with open('aliyun.txt', 'w', encoding='utf-8') as f:
        f.writelines([title + '\n', intro + '\n', content_text])
        print('数据写入完毕')


if __name__ == '__main__':
    # 步骤一：确定 url
    url = 'https://developer.aliyun.com/article/783318?spm=a2c6h.12873581.0.0.e40646ccwzBRpg&groupCode=bigdata'
    crawle(url)
