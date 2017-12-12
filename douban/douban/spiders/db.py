# -*- coding: utf-8 -*-
#模拟自动登录豆瓣
import scrapy
from scrapy.http import Request,FormRequest
import urllib2
import pandas as pd 
from pandas import  DataFrame,Series
from pandas.tests.io.parser import index_col, usecols
class DbSpider(scrapy.Spider):
    name = "db"
    allowed_domains = ["douban.com"]
    header={"User-Agent:":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0"}
    '''
    start_urls = (
        'http://www.douban.com/',
    )
    '''
    data1=DataFrame(pd.read_csv("G://doubanDemo/user.csv",usecols=[0],header=0))
    print data1.head(10)
    def start_requests(self):
        return [Request("https://accounts.douban.com/login",callback=self.parse,meta={"cookiejar":1})]
    def parse(self, response):
        captcha=response.xpath("//img[@id='captcha_image']/@src").extract()
        url="https://accounts.douban.com/login"
        if len(captcha)>0:
            print("此时验证码")
            localpath="G:crawler/captcha.png"
            urllib2.urlretrieve(captcha[0],filename=localpath)
            print("请查看本地验证码图片并输入验证码")
            captcha_value=input()

            data={
                "form_email":"luozhukun@163.com",
                "form_password":"lzk15884706478",
                "captcha-solution":captcha_value,
                "redir":"https://www.douban.com/people/80285237/",
            }
        else:
            print("此时没有验证码")
            data={
                "form_email":"luozhukun@163.com",
                "form_password":"lzk15884706478",
                "redir":"https://www.douban.com/people/80285237/",
            }
        print("登陆中……")
        return [FormRequest.from_response(response,
                                              meta={"cookiejar":response.meta["cookiejar"]},
                                              headers=self.header,
                                              formdata=data,
                                              callback=self.next,
                                              )]

    def next(self,response):
        print("此时已经登陆完成并爬取了个人中心的数据")
        title=response.xpath("/html/head/title/text()").extract()
        note=response.xpath("//div[@class='note']/text()").extract()
        print(title[0])
        print(note[0])
    ''' 
    def run(self):
         for i in range(0,len(data1)): 
                print len(data1)
                print (data1["user"][i]).strip()
                url1="https://movie.douban.com/people/"+(data1["user"][i]).strip()+"/collect"
                data3=urllib2.urlopen(url1).read().decode('utf-8','ignore')
                print data3
                pat='<title>穆看过的电影(.*?)</title>'
                print pat
                nums = re.compile(pat).findall(data3)
                print nums[0]
                pat1='<a href="https://movie.douban.com/subject/(.*?)/" class>'
                pat2='<span class="rating(2)-t"></span>'
                for j in range(0,nums/15+1): 
                      print nums
                      url2="https://movie.douban.com/people/"+str(data1["user"][i])+"/collect?start="+j*15+"&sort=time&rating=all&filter=all&mode=grid"
                      data2=urllib2.urlopen(url2).read().decode('utf-8','ignore')
                      movieIds=re.compile(pat1).findall(data2)
                      movieRanks=re.compile(pat2).findall(data2)
                      print movieIds[i]+"+"+movieRanks[i] 
'''  
        
 
        
