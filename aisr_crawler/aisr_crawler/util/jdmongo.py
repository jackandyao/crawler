# this is use python script!
# -*- coding: UTF-8 -*-
# python 操作mongodb
import pymongo
from pymongo import MongoClient
import datetime
#Python读取京东爬取到的数据
class JDMongodUtil:

    hostip ="192.168.14.107"
    hostport =27017
    collection=""
    database="jd_spiders"
    #collection ="jd_ios_link"
    collection="jd_all"
    #实例对象的时候就会执行该方法
    def __init__(self):
         client = MongoClient(host=self.hostip,port=self.hostport)
         db=client.get_database(self.database)
         self.coll = db.get_collection(self.collection)

    #查询所有的ID
    def getIDListFromMongod(self,type):
        id_list = self.coll.find({})
        if (id_list !=None):
            for item in id_list:
                with open("../config/"+type+"_idlink.txt", 'a') as f:
                   if(type == 'android'):
                       #print(item['id'].strip()+":"+item['android_link'].strip())
                       if("android_link" in item):

                           f.write(item['id'].strip() + "&&" + item['android_link'].strip() + '\n')
                       else:
                           print('不包含key',item['id'])
                   if(type == 'ios'):
                       if('ios_link' in item):
                            f.write(item['id'].strip()+"&&"+item['ios_link'].strip() + '\n')
                       else:
                           print('不包含key', item['id'])

    #查询所有产品的ID
    def getIDFromMongod(self,type,idfile):
        if(type == "android"):
            item_list = self.coll.find({"android_promotion_url":"#"},{"real_stuff_id":1})
            print('android',item_list)
            self.writeIDToFile(idfile,item_list)
        if(type == "ios"):
            item_list = self.coll.find({"ios_promotion_url":"#"}, {"real_stuff_id": 1})
            self.writeIDToFile(idfile, item_list)

    #查询所有推广快要过期的产品
    def getNoVaiableIDFromMongo(self,id):
        item = self.coll.find_one({"real_stuff_id": id})
        if(item !=None):
            end_str = item['end_date']
            end_date = datetime.datetime.strptime(end_str, '%Y-%m-%d')
            now_date = datetime.datetime.strptime("2017-07-10", '%Y-%m-%d')
            day = (end_date - now_date).days
            if (day<0):
                self.coll.delete_one({"real_stuff_id": id})
                print('删除过期ID',id,day,end_str)
        else:
            print('产品ID已经被删除了',id)

    #批量删除推广过期的商品
    def batchDeleteID(self):
        for id in open('../config/jd_id_ios.txt'):
            self.getNoVaiableIDFromMongo(id.strip())

    #删除已经不再推广的商品
    def batchIDDeleteNoTuiGuang(self):
        for id in open('../config/jd_id_notuguang.txt'):
            self.coll.delete_one({"real_stuff_id": id})
            print('删除过期ID', id)

    
    #根据ID查询所有字段值
    def getOneSpuFromMongo(self,id):
        item = self.coll.find_one({"real_stuff_id": id})
        return item

    #把要待转链接的ID存入到文件里面
    def writeIDToFile(self,idfile,item_list):
        if item_list.count()>0:
            for item in item_list:
                if 'real_stuff_id' in item:
                    with open(idfile, 'a') as f:
                       f.write(item['real_stuff_id'] + '\n')
                else:
                    print('不存在对应的KEY',item_list)
            print('jd_id_count', item_list.count())
        else:
            print("对不起,本次没有查询到任何数据!")

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

    #批量更新链接
    def batchUpdateLink(self,type):
        for obj in open('../config/'+type+"_idlink.txt"):
            item = obj.split("&&")
            id = item[0]
            code = item[1]
            self.updateLinkById(id,type,code)
            print('更新链接',type,id,code)

    #测试插入数据
    def insertData(self):
        user_profiles = [
            {'user_id': 211, 'name': 'Luke'},
            {'user_id': 212, 'name': 'Ziltoid'}]
        self.coll.insert_many(user_profiles)
    #测试更新数据
    def updateData(self):
        self.coll.update({"user_id":"211"},{"$set:{age:32}"},'true')




if __name__ == '__main__':
    #jd = JDMongodUtil().getIDFromMongod("ios","../config/jd_id_ios.txt")
    #jd = JDMongodUtil().getIDFromMongod("android", "../config/jd_id_android.txt")
    #jd = JDMongodUtil().getIDListFromMongod("ios")
    #jd = JDMongodUtil().batchIDDeleteNoTuiGuang()
    jd = JDMongodUtil().batchUpdateLink("ios")
    #print('删除结束')
    print('操作完成')