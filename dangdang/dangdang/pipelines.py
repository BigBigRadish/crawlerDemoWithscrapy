# -*- coding: utf-8 -*-
import pymysql
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DangdangPipeline(object):
    def process_item(self, item, spider):
        conn=pymysql.connect(host="localhost",user="root",password="147258",db="dangdang")
        for i in range(0,len(item["title"])):
            title=item["title"][i].encode("utf-8","ignore")
            link=item["link"][i].encode("utf-8","ignore")
            comments= item["comments"][i].encode("utf-8","ignore")
            sql="insert into goods(title,link,comments) values('"+title+"','"+link+"','"+comments+"')" 
            conn.query(sql)           
        conn.close()        
        return item
