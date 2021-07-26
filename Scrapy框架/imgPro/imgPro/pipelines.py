# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
# DropItem是用来删除下载图片失败的item的
from scrapy.exceptions import DropItem
# 导入系统文件images.py里的ImagesPipeline类
from scrapy.pipelines.images import ImagesPipeline


# class imagesPipeLine(ImagesPipeline):
#     image_name = ''
#
#     def get_media_requests(self, item, info):
#         img_name = item['img_name']
#         self.image_name = img_name
#         print(item['img_url'])
#         yield scrapy.Request(item['img_url'])
#
#     def file_path(self, request, response=None, info=None):
#         imgName = request.url.split('/')[-1]
#         return imgName
#         # file_name = self.image_name
#         # print(file_name)
#         # return file_name
#
#     def item_completed(self, results, item, info):
#         print(results)
#         return item


class ImgproPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        yield scrapy.Request(url=item['img_url'], dont_filter=False)

    def file_path(self, request, response=None, info=None):
        url = request.url
        file_name = url.split('/')[-1]
        print(file_name)
        return file_name

    def item_completed(self, results, item, info):
        print(results)
        # image_paths = [x['path'] for ok, x in results if ok]
        # print(str(image_paths))
        # if not image_paths:
        #     raise DropItem('下载失败')
        return item
