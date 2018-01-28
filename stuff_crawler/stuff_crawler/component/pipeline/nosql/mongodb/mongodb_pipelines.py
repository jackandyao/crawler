# -*- coding: utf-8 -*-
import pymongo
from scrapy.conf import settings
from component.util.config_util import ConfigUtil as conf
#使用mongodb持久化爬虫解析之后的数据
class MongoDBScrapyPipeline(object):

    #定义一个初始化方法来初始化MONGO的连接信息
    def __init__(self):
        file = settings['MONGODB_CONF_FILE']
        selection ="mongodb_"+settings['PROJECT_MODE_TYPE']
        host = conf(file).getValue(selection,'MONGODB_HOST')
        port = conf(file).getIntValue(selection,'MONGODB_PORT')
        db = conf(file).getValue(selection,'MONGODB_DB')
        coll = conf(file).getValue(selection,'MONGODB_COLL')

        # 链接数据库
        self.client = pymongo.MongoClient(host=host, port=port)
        # 数据库登录需要帐号密码的话
        # self.client.admin.authenticate(settings['MONGODB_USERNAME'], settings['MONGODB_PASSWORD'])
        self.db = self.client[db]  # 获得数据库的句柄
        self.coll = self.db[coll]  # 获得collection的句柄

    #持久数据到mongo中
    def process_item(self, item, spider):
        #判断销量 如果销量不满足需要的最低销量 需要把这个item给删除掉 满足的话 就持久化下来
        #item转换为对应的字典
        postItem = dict(item)
        operator_type = settings['MONGODB_OPERATOR_TYPE']
        #print('操作类型',operator_type)
        #执行增加操作
        if (operator_type =='insert'):
            self.coll.insert_one(postItem)
        #执行更新操作
        elif(operator_type =='update'):
            #需要通过item构造类似于 update_one({'x': 1}, {'$inc': {'x': 3}}) 这种结构
            self.coll.update_one(postItem)
        else:
            print('目前没有可以操作的类型')



