import requests
from bs4 import BeautifulSoup

# 设置 U-A
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)'
}


def crawle(url):
    # 步骤二三：发送HTTP请求，获取响应数据
    response = requests.get(url, headers).content.decode('utf-8')

    # 步骤四：数据解析
    # 构建bs4对象
    soup = BeautifulSoup(response, 'lxml')
    # 文章标题
    title = soup.find('span', itemprop="articleSection").text
    # 作者
    author = soup.find_all('span', itemprop="name")[1].text.strip()
    # 时间
    time = soup.find_all('span', itemprop="datePublished")[0].text
    # 文章内容
    content_list = soup.find_all('p')
    content_text = ''
    for content in content_list:
        content_text += content.text.strip() + '\n'
    # 步骤五持久化存储
    with open('bokee.txt', 'w', encoding='utf-8') as f:
        f.writelines([title + '\n', author + '\n', time + '\n', content_text])
        print('数据写入完毕')


if __name__ == '__main__':
    # 步骤一：确定 url
    url = 'http://tiantianxs2009.bokee.com/507186348.html'
    crawle(url)
