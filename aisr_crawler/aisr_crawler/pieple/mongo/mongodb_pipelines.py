# -*- coding: utf-8 -*-
import pymongo
from scrapy.conf import  settings
#把爬虫最终解析的数据进行持久化
class MongoPipeline(object):

    #定义一个初始化方法来初始化MONGO的连接信息
    def __init__(self):
        # 链接数据库
        self.client = pymongo.MongoClient(host=settings['MONGODB_HOST'],
                                          port=settings['MONGODB_PORT'])
        # 数据库登录需要帐号密码的话
        #self.client.admin.authenticate(settings['MONGODB_USERNAME'], settings['MONGODB_PASSWORD'])
        self.db = self.client[settings['MONGODB_DB']]  # 获得数据库的句柄
        self.postItem = self.db[settings['MONGODB_COLL']]  # 获得collection的句柄

    #持久数据到mongo中
    def process_item(self, item, spider):
        #item转换为对应的字典
        postItem = dict(item)  # 把item转化成字典形式
        #print('postItem', postItem)
        self.postItem.insert_one(postItem)  # 向数据库插入一条记录
        #return item  # 会在控制台输出原item数据，可以选择不写


