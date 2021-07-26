# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from scrapy.exporters import JsonItemExporter


class LiepinproPipeline(object):

    # 构造方法（初始化对象时执行的方法）
    def __init__(self):
        # 使用 'wb' （二进制写模式）模式打开文件
        self.json_file = open('data3.json', 'wb')
        # 构建 JsonItemExporter 对象，设定不使用 ASCII 编码，并指定编码格式为 'UTF-8'
        self.json_exporter = JsonItemExporter(self.json_file, ensure_ascii=False, encoding='UTF-8', indent=2)
        # 声明 exporting 过程 开始，这一句也可以放在 open_spider() 方法中执行。
        self.json_exporter.start_exporting()

    # 爬虫 pipeline 接收到 Scrapy 引擎发来的 item 数据时，执行的方法
    def process_item(self, item, spider):
        # 将 item 存储到内存中
        self.json_exporter.export_item(item)
        return item

    def close_spider(self, spider):
        # 声明 exporting 过程 结束，结束后，JsonItemExporter 会将收集存放在内存中的所有数据统一写入文件中
        self.json_exporter.finish_exporting()
        # 关闭文件
        self.json_file.close()



