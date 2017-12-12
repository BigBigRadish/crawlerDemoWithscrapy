# -*- coding: utf-8 -*-
import pymysql
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DangdangPipeline(object):
    def process_item(self, item, spider):
        conn=pymysql.connect(host="127.0.0.1",user="root",password="147258",db="dangdang")
        for i in range(0,len(item["title"])):
            title=item["title"][i]
            link=item["link"][i]
            comment= item["comment"][i]
            sql="insert into goods(title,link,comment) values('"+title+"','"+link+"','"+comment+ "')"
            conn.query(sql)
            conn.close()
        return item
