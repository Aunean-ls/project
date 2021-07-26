# import requests
# from selenium import webdriver
# from lxml import etree
# import re
# import time
#
#
# class LagouSpider(object):
#     """爬虫类"""
#     def __init__(self):
#         self.driver = webdriver.Chrome()
#         self.url = "https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&city=%e5%b9%bf%e5%b7%9e&suginput="
#
#     def run(self):
#         self.driver.get(self.url)
#         source = self.driver.page_source
#
#
# if __name__ == "__main__":
#     LagouSpider().run()


import requests
from selenium import webdriver
from lxml import etree
import re
import time
import csv


class LagouSpider(object):
    """爬虫类"""
    def __init__(self):
        """初始化, 新建lagou_detail_position.csv文件（类excel文件)来保存数据"""
        self.driver = webdriver.Chrome()
        self.url = "https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput="
        # 新建excel文件，保存内容
        headers = ['name', 'company_name', 'salary', 'city', 'work_years', 'education', 'desc']  # 列表
        with open('lagou_detail_position.csv', 'w', newline='', encoding='utf-8') as fp:
            writer = csv.writer(fp)
            writer.writerow(headers)  # 写入头部

    def run(self):
        try:
            self.driver.get(self.url)
            time.sleep(5)
            # 输入框webelement
            inputTag = self.driver.find_element_by_id("keyword")
            # 默认有内容，得clear一下
            inputTag.clear()
            inputTag.send_keys("python爬虫")  # 这里输入你需要爬取的岗位内容
            # 提交button的webelement
            submitTag = self.driver.find_element_by_id("submit")
            submitTag.click()
            while True:
                # 获取当前列表页的页数
                now_number = self.driver.find_element_by_xpath("//span[@class='pager_is_current']")
                now_number = now_number.get_attribute("page")
                print("*"*30)
                print("正在下载第%s页面的内容\n" % now_number)
                time.sleep(2)
                # 获取列表页的内容
                source = self.driver.page_source
                self.parse_list_page(source)
                print("已经下载完第%s页面的内容" % now_number)
                # 获取下一个的按钮元素webelement
                next_btn = self.driver.find_element_by_xpath("//div[@class='pager_container']/span[last()]")
                # 判断是否还有下一页，没有就退出循环
                if "pager_next pager_next_disabled" in next_btn.get_attribute("class"):
                    break
                next_btn.click()
        finally:
            time.sleep(2)
            self.driver.quit()

    def parse_list_page(self, source):
        """获取列表页中各个详情页的内容"""
        html = etree.HTML(source)
        links = html.xpath("//a[@class='position_link']/@href")
        for link in links:  # 依次遍历各个岗位的详情页
            print(link)
            self.request_detail_page(link)
            time.sleep(4)

    def request_detail_page(self, url):
        """跳转到详情页页面"""
        # 重新打开个窗口
        window_open = "window.open('"+url+"')"
        self.driver.execute_script(window_open)
        # 跳转到新的窗口
        self.driver.switch_to_window(self.driver.window_handles[1])
        source = self.driver.page_source
        self.parse_detail_page(source)
        # 关闭详情页的窗口
        self.driver.close()
        # 调回至列表页的窗口
        self.driver.switch_to_window(self.driver.window_handles[0])

    def parse_detail_page(self, source):
        """详情页提取具体内容"""
        # 将source转换成可以xpath的element对象
        html = etree.HTML(source)
        # 职位名称
        position_name = html.xpath("//div[@class='job-name']/@title")[0]
        # 公司名称
        company_name = html.xpath("//img[@class='b2']/@alt")[0]
        # 岗位需求
        job_request_spans = html.xpath("//dd[@class='job_request']//span")
        # 工资
        salary = job_request_spans[0].xpath(".//text()")[0].strip()
        # 所在城市
        city = job_request_spans[1].xpath(".//text()")[0].strip()
        city = re.sub(r"[\s/]", "", city)
        # 需要的工作经验
        work_years = job_request_spans[2].xpath(".//text()")[0].strip()
        work_years = re.sub(r"[\s\/]", "", work_years).strip()
        # 需要的教育程度
        education = job_request_spans[3].xpath(".//text()")[0].strip()
        education = re.sub(r"[\s/]", "", education)
        # 岗位描述
        desc = "".join(html.xpath("//dd[@class='job_bt']//text()")).strip()
        desc = re.sub(r"[\n\s]", "", desc)
        position = [position_name, company_name, salary, city, work_years, education, desc]
        self.save_data(position)

    def save_data(self, position):
        # 保存获取到的数据
        with open('lagou_detail_position.csv', 'a', newline='', encoding='utf-8') as fp:
            writer = csv.writer(fp)
            writer.writerow(position)  # 多行写入


if __name__ == "__main__":
    LagouSpider().run()
