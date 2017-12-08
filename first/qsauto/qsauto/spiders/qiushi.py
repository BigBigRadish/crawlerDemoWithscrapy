# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from qsauto.items import  QsautoItem
from scrapy.http import  Request


class QiushiSpider(CrawlSpider):
    name = 'qiushi'
    allowed_domains = ['qiushibaike.com']
    '''
    start_urls = ['http://www.qiushibaike.com/']
    '''
    def start_requests(self):
        ua={"user-agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0"}#设置代理
        yield Request("http://www.qiushibaike.com/",headers=ua)
        
    rules = (
        Rule(LinkExtractor(allow=r'article'), callback='parse_item', follow=True),#foloww 代表连接是否跟进
    )
    def parse_item(self, response): 
         item=QsautoItem()
         item["content"]=response.xpath("//div[@class='content']/text()").extract()#提取段子
         item["link"]=response.xpath("//a[@rel='canonical']/@herf").extract()#提取链接  
         print  item["content"] 
         for i in range(0,len(item["content"])): 
          fh=open('G://crawler/qiushi.txt','a')
          fh.write(item["content"][i])
          yield ()
