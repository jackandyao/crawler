# this is use python script!
# -*- coding: UTF-8 -*-
# python 操作mongodb
import pymongo
from pymongo import MongoClient
import datetime
#Python读取京东爬取到的数据
class JDLinkMongodUtil:

    hostip ="192.168.14.107"
    hostport =27017
    collection=""
    database="jd_spiders"
    #collection ="jd_android_link"
    collection="jd_hot"
    #实例对象的时候就会执行该方法
    def __init__(self):
         client = MongoClient(host=self.hostip,port=self.hostport)
         db=client.get_database(self.database)
         self.coll = db.get_collection(self.collection)


    #更新指定产品的IOS连接和ANDORID连接
    def updateLinkById(self,id,type,link):
        if(type == "android"):
            self.coll.update({"real_stuff_id":str(id)},{"$set":{"android_promotion_url":link}},multi=True)
            print(type+":"+link)

        elif(type == "ios"):
            self.coll.update({"real_stuff_id": str(id)}, {"$set":{"ios_promotion_url": link}},multi=True)
            print(type + ":" + link)
        else:
            print("对不起,目前不知道你需要转什么链接,请输入专链接类型")
