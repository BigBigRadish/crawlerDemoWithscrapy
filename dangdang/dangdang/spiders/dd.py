# -*- coding: utf-8 -*-
import scrapy
from dangdang.items import DangdangItem
from scrapy.http import  Request

class DdSpider(scrapy.Spider):
    name = 'dd'
    allowed_domains = ['dangdang.com']
    start_urls = ['http://www.dangdang.com/']

    def parse(self, response):
        Item=DangdangItem()
        Item['title']=response.xpath('//a[@class="pic"]/@title').extract()
        Item['link']=response.xpath('//a[@class="pic"]/@href').extract()
        Item['comments']=response.xpath('//a[@name="itemlist-review"]/text()').extract()
        yield Item
        for i in range(2,101):
            url="http://category.dangdang.com/pg"+str(i)+"-cp01.54.06.00.00.00.html"
            yield Request(url,callback=self.parse)
            
 