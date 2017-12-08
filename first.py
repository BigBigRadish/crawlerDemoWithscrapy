# -*- coding: utf-8 -*-
from scrapy.spiders import Spider
class firstSpider(Spider):
  name="first"#设置爬虫名字
  allowed_domains=["baidu.com"]#控制爬的域名
  start_urls=["http://www.baidu.com"]#设置起始地址
  def parse(self,response): #回调方法
    pass#占位符，遇到任何事情不执行
  
