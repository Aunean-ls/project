import requests
import re
from fontTools.ttLib import TTFont
import pandas as pd

url = 'https://maoyan.com/board/1'
headers = {
    'user-agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)',
}
all_content = []
response = requests.get(url=url, headers=headers).content.decode('utf-8')


def get_woff_file():
    file_url = re.findall(r"src:.*?,.*?url\('(.*?)'\) format\('woff'\);", response, re.S)[0]
    # print(file_url)
    with open('D:/temp/maoyan_base1.woff', 'wb') as fp:
        content = requests.get('http:' + file_url).content
        fp.write(content)

    with open('D:/temp/maoyan_new1.woff', 'wb') as fp:
        content = requests.get('http:' + file_url).content
        fp.write(content)


def parse_font():
    font = TTFont('D:/temp/maoyan_base1.woff')
    font.saveXML('D:/temp/maoyan_base1.xml')
    font_base_order = font.getGlyphOrder()[2:]
    # print(font_base_order)
    # 根据第一次下载的文件写出对应
    map_list = ['6', '3', '7', '9', '1', '8', '0', '4', '2', '5']

    font_new = TTFont('D:/temp/maoyan_new1.woff')
    font_new.saveXML('D:/temp/maoyan_new1.xml')
    font_new_order = font_new.getGlyphOrder()[2:]
    # print(font_new_order)

    base_flag_list = []
    new_flag_list = []
    # 得到两个二维列表，对里面没个一维列表进行内容的比对，得到对应的字体
    for i, j in zip(font_base_order, font_new_order):
        flag_base = font['glyf'][i].flags
        flag_new = font_new['glyf'][j].flags
        base_flag_list.append(list(flag_base))
        new_flag_list.append(list(flag_new))

    memory_dict = {}
    for index1, x in enumerate(base_flag_list):
        for index2, y in enumerate(new_flag_list):
            if common(x, y):
                key = font_new_order[index2]
                key = '&#x' + key.replace('uni', '').lower() + ';'
                memory_dict[key] = map_list[index1]
    # print(memory_dict)
    '''
    {'&#xf4ef;': '6', '&#xf848;': '3', '&#xf88a;': '7', '&#xe7a1;': '9', '&#xe343;': '1', '&#xe137;': '8', 
    '&#xf489;': '0', '&#xe5e2;': '4', '&#xf19b;': '2', '&#xe8cd;': '5'}
    '''
    return memory_dict


def get_data(memory_dict):
    # 获取每一个dd标签中的数据
    pattern = r'<dd>.*?<i class="board-index board-index(.*?)</dd>'
    all_data = re.findall(pattern, response, re.S)

    for data in all_data:
        # 电影名
        title = re.findall(r'title="(.*?)"', data, re.S)[0]
        # print(title)
        # 主演
        actor = re.findall(r'<p class="star">主演：(.*?)</p>', data, re.S)[0]
        # print(actor)
        # 上映时间
        time = re.findall(r'<p class="releasetime">上映时间：(.*?)</p>', data, re.S)[0]
        # print(time)
        # 实时票房
        realtimeBO = re.findall(r'<p class="realtime">实时票房:.*?class="stonefont">(.*?)</span></span>(.*?)</p>',
                                data, re.S)[0]
        realtimeBoxOffice = realtimeBO[0]
        for key, value in memory_dict.items():
            # 将 realtimeBoxOffice 加密数字 &#xf4ef;&#xf4ef;&#xe137;.&#xf848; 和 memory_dict 中的 key 进行匹配，解析出数据
            realtimeBoxOffice = realtimeBoxOffice.replace(key, value)
        realtimeBoxOffice = realtimeBoxOffice + realtimeBO[1].strip()
        # print(realtimeBoxOffice)
        # 总票房
        totalBO = re.findall(r'<p class="total-boxoffice">总票房:.*?class="stonefont">(.*?)</span></span>(.*?)</p>',
                             data, re.S)[0]
        totalBoxOffice = totalBO[0]
        for key, value in memory_dict.items():
            totalBoxOffice = totalBoxOffice.replace(key, value)
        totalBoxOffice = totalBoxOffice + totalBO[1].strip()
        # print(totalBoxOffice)
        content = {
            'title': title,
            'actor': actor,
            'time': time,
            'realtimeBoxOffice': realtimeBoxOffice,
            'totalBoxOffice': totalBoxOffice
        }
        print(content)
        all_content.append(content)


# 存储数据
def save_data():
    df = pd.DataFrame(data=all_content, columns=['title', 'actor', 'time', 'realtimeBoxOffice', 'totalBoxOffice'])
    df.to_csv("maonyan.csv", encoding='utf-8', index=False)


# 进行数据对比以及保证数据的顺序
def common(list1, list2):
    len1 = len(list1)
    len2 = len(list2)
    if len1 != len2:
        return False
    for i in range(len1):
        if list1[i] != list2[i]:
            return False
    return True


if __name__ == '__main__':
    get_woff_file()
    memory_dict = parse_font()
    get_data(memory_dict)
    save_data()

