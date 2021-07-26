from lxml import etree
import requests

headers = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)'
}
# 验证网站
targetUrl = 'https://www.sogou.com/web?'

proxyHost = '122.143.228.112'  # ip地址
proxyPort = '4256'  # 端口号
params = {
    'query': 'ip'
}
proxyMeta = "http://%(host)s:%(port)s" % {
    "host": proxyHost,
    "port": proxyPort,
}
# print(proxyMeta)
proxies = {
    "http": proxyMeta,
    "https": proxyMeta
}
print(proxies)
resp = requests.get(targetUrl, headers=headers,params=params, proxies=proxies).content.decode('utf-8')
sel = etree.HTML(resp)
# print(resp)
ip = sel.xpath('//*[@id="ipsearchresult"]/strong/text()')
print(ip)
# import io
# import sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gbk')
# headers = {
#     'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)'
# }
# # 验证网站
# targetUrl = 'https://ip.tool.chinaz.com/'
#
# proxyHost = '122.236.230.69'  # ip地址
# proxyPort = '4256'  # 端口号
#
# proxyMeta = "http://%(host)s:%(port)s" % {
#     "host": proxyHost,
#     "port": proxyPort,
# }
# # print(proxyMeta)
# proxies = {
#     "http": proxyMeta,
#     "https": proxyMeta
# }
# print(proxies)
# resp = requests.get(targetUrl, headers=headers, proxies=proxies)
# resp.encoding = resp.apparent_encoding
# sel = etree.HTML(resp.text)
# # print(resp.text)
# ip = sel.xpath('//*[@id="rightinfo"]/div[1]/dl/dd[1]/text()')[0]  # IP地址
# addr = sel.xpath('//*[@id="rightinfo"]/div[1]/dl/dd[2]/text()')[0]  # 来自
# print(ip)
# print(addr)





