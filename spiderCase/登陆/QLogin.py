import requests

url = 'https://ssl.ptlogin2.qq.com/login'

headers = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)'
}

data = {
    'u': '1269187774',
    'verifycode': '!XYU',
    'pt_vcode_v1': '0',
    # 'pt_verifysession_v1': '97d193c1bc8f9b91034004ba96e03622b38397638ea668262b8baa5d6b4437cf11d695606f74d750cbeac84cca5974b4b0f9b39d05ff8ff1',
    'p': '2F8PDKhPCHq9Ucikqv303wY1v0kUHPpCfXTQes4OP*oktxmQa7kKqmIUaMcJb3cVeeYocAVaC8980VZAUV5gR6dLqOW8J9x2heNdmyFxkR1IrnXjqs41jkZ4KY-E2TjJrQZDiHzG0a8xHEK*GTneeNjTYzLqvOcUGR7o8A9WXaGBc*z50VOGBggxKN*laN-jklzDKK*QPBSLgXb9Jgyoo5xrZQUXrBMAoK*OqVhyvxJheTo0Fr7wAMHYUwNozz2OycFfNB1XaPOa8r**C3-fqm*mWQ6l8JO2ZteDvr4WmTiUSKibRkdTPFAvQZJ4V7lZy1dZzYUEb80**FQ1YOcqbg__',
    'pt_randsalt': '2',
    'u1': 'https://qzs.qzone.qq.com/qzone/v5/loginsucc.html?para=izone',
    'ptredirect': '0',
    'h': '1',
    't': '1',
    'g': '1',
    'from_ui': '1',
    'ptlang': '2052',
    'action': '3-10-1621212168894',
    'js_ver': '21050810',
    'js_type': '1',
    # 'login_sig': 'eVYvSqIM0vJQxhbv38CURZTp - LyNBbsBGtdchzSV3RY4FalWLIqXmmStzccp61tS',
    'pt_uistyle': '40',
    'aid': '549000912',
    'daid': '5',
    # 'ptdrvs': 'Dw3f1kJrqKmZIjJD - BYXuS0fXsdOXsGnnL8 - tPE1grUTvRJuy * RY4nF6iDoBBzHs',
    # 'sid': '5702160340849113372',
}

session = requests.session()

response = session.post(url=url, headers=headers, data=data)
response.encoding = response.apparent_encoding

html_content = response.text
print(response.status_code)
print(html_content)
with open('QLogin.html', 'w', encoding='utf-8') as f:
    f.write(html_content)
