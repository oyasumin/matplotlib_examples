# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor

from matplotlib_examples.items import ExampleItem


class ExamplesSpider(scrapy.Spider):
    name = 'examples'
    allowed_domains = ['matplotlib.org']
    start_urls = ['http://matplotlib.org/examples/index.html']

    def parse(self, response):
        le = LinkExtractor(restrict_css='div.toctree-wrapper.compound', deny="/index.html$")
        # le = LinkExtractor(restrict_css='div.toctree-wrapper.compound li.toctree-l2')
        links = le.extract_links(response)
        print(len(links))
        for link in links:
            yield scrapy.Request(link.url, callback=self.parse_example)

    # 例子页面的解析函数
    def parse_example(self, response):
        href = response.css('a.reference.external::attr(href)').extract_first()
        url = response.urljoin(href)
        example = ExampleItem()
        example['file_urls'] = [url]
        return example