import re
import requests

word = input('请输入搜索关键字：')
base_url = 'https://search.51job.com/list/190000,000000,0000,00,9,99,{},2,{}.html?'

headers = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)'
}
params = {
    'lang': 'c',
    'postchannel': '0000',
    'workyear': '99',
    'cotype': '99',
    'degreefrom': '99',
    'jobterm': '99',
    'companysize': '99',
    'ord_field': '0',
    'dibiaoid': '0',
    'line': '',
    'welfare': '',
}
end_page = input("请输入结束页：")

for page in range(1, int(end_page) + 1):
    url = base_url.format(word, end_page)
    response = requests.get(url=url, params=params, headers=headers).content.decode('gbk')
    pattern = r'"job_name":"(.*?)".*?"company_name":"(.*?)".*?providesalary_text":"(.*?)".*?"workarea_text":"(.*?)".*?companytype_text":"(.*?)".*?workyear":"(.*?)".*?"issuedate":"(.*?)".*?jobwelf":"(.*?)"'
    content = re.findall(pattern, response, re.S)
    for info in content:
        position = info[0].replace('\\', '')
        company = info[1]
        salary = info[2].replace('\\', '')
        work_place = info[3]
        company_type = info[4]
        work_year = info[5]
        update = info[6]
        welfare = info[7]
        data = position + "," + company + "," + salary + "," + work_place + "," + company_type \
               + "," + work_year + "," + update + "," + welfare

        with open('51jb.txt', 'a', encoding='utf-8', newline='') as f:
            f.write(data + '\n')
