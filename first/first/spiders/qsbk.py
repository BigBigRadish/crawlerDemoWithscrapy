# -*- coding: utf-8 -*-
#糗事百科自动爬虫
import scrapy
from first.items import FirstItem
from scrapy.http import  Request
class QsbkSpider(scrapy.Spider):
    name = 'qsbk'
    allowed_domains = ['qiushibaike.com']
    '''
    start_urls = ['http://www.qiushibaike.com/']
    '''
    def start_requests(self):
        ua={"user-agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0"}#设置代理
        yield Request("http://www.qiushibaike.com/",headers=ua)
    def parse(self, response):
         item=FirstItem()
         item["content"]=response.xpath("//div[@class='content']/span/text()").extract()#提取段子
         item["link"]=response.xpath("//a[@class='contentHerf']/@herf").extract()#提取链接
         yield item