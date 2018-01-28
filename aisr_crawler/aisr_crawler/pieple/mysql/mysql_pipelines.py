# this is use python script!
# -*- coding: UTF-8 -*-
from twisted.enterprise import adbapi
import pymysql
import codecs
import json
from logging import log
from aisr_crawler.pieple.mysql.dbhelper import DBHelper as db

# class JsonWithEncodingPipeline(object):
#
#     def __init__(self):
#         pymysql.install_as_MySQLdb()
#         self.file = codecs.open('info.json', 'w', encoding='utf-8')#保存为json文件
#     def process_item(self, item, spider):
#         line = json.dumps(dict(item)) + "\n"#转为json的
#         self.file.write(line)#写入文件中
#         return item
#     def spider_closed(self, spider):#爬虫结束时关闭文件
#         self.file.close()

#存储数据到MYSQL数据库中
class MySQLScrapyPipeline(object):

    # pipeline默认调用
    def process_item(self, item, spider):
        con = db().connectMysql()
        cursor = con.cursor()
        sql = 'insert into qbao_stuff.test_stuff(id,name) values (%s,%s)'
        try:
            cursor.execute(sql, (item['id'], item['name']))
            con.commit()
        except Exception as err:
            print('error',err)
            con.rollback()


        return item



