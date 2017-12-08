# -*- coding: utf-8 -*-
import scrapy
from first.items import FirstItem

class Demo1Spider(scrapy.Spider):
    name = 'demo1'
    allowed_domains = ['baidu.com']
    start_urls = ['http://baidu.com/']

    def parse(self, response):
        item=FirstItem()
        item["content"]=response.xpath("//title/text()").extract()
        yield item#用yield返回