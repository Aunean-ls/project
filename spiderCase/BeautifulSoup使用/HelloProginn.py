import requests
from bs4 import BeautifulSoup

# 步骤一：确定url
url = 'https://www.proginn.com/search'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)'
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
    # 用户名标签列表
    name = soup.select('p.user-name')
    # 职位标签列表
    title = soup.select('div.title > a.info')
    # 技能
    skill = soup.select('p.desc-item:nth-child(2) > span')
    # 工作内容
    work = soup.select('p.desc-item:nth-child(3) > span')
    # 工作地点和时间父节点列表
    father = soup.select('div.work-time')

    for i in range(len(name)):
        # 用户名
        cName = name[i].text
        # 职位
        cTitle = title[i].attrs['title']
        # 技能
        cSkills = skill[i].text
        # 工作内容
        cWorks = work[i].text
        # 工作地点
        cAddress = father[i].div.text
        # 工作时间
        for t in father[i].div.next_siblings:
            cTime = t.text
        data = {
            'name': cName,
            'position': cTitle,
            'skills': cSkills,
            'works': cWorks,
            'address': cAddress,
            'time': cTime
        }
        content.append(data)
        print(data)

# 步骤五：存储数据
for value in content:
    with open('roginn.txt', 'a', encoding='utf-8') as f:
        f.write(str(value) + '\n')
