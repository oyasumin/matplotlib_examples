# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from os.path import basename, dirname, join

from scrapy.pipelines.files import FilesPipeline
from urllib.parse import urlparse


class MatplotlibExamplesPipeline:
    def process_item(self, item, spider):
        return item

class MyFilesPipeline(FilesPipeline):
    def file_path(self, request, response=None, info=None):
        # urlparse("http://www.baidu.com/a/v")
        # ParseResult(scheme='http', netloc='www.baidu.com', path='/a/v', params='', query='', fragment='')
        # .path取出urlparse解析出来的文件资源路径
        path = urlparse(request.url).path
        # basename获取路径最后的值，dirname获取路径中除了最后值的前面的部分
        return join(basename(dirname(path)), basename(path))
