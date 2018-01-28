# this is use python script!
# -*- coding: UTF-8 -*-
import urllib.request as req
import json
from urllib import error
import urllib
from aisr_crawler.util.condition import CreateCondition as cc
class JDUtil:
    #创建请求参数
    def createLinkParam(file,type,id):
        #创造查询条件
        param =cc.createSearchCondition(file)
        if(type=='android'):
            param['unionAppId'] ='778075041' #android
        else:
            param['unionAppId'] = '778066019' #ios
        param['materialId']=id #产品id
        param['wareUrl'] ="http://item.jd.com/"+id+".html"
        return param;

    #获取所有待转连接的ID
    def getLinkIDList(file):
        keywords = []
        for key in open(file):
            keywords.append(key.strip())
        return keywords

    #获取要爬取的商品关键字
    def createSearchParam(file):
        key_list = []
        for line in open(file,encoding='UTF-8'):
            key_param = {}
            lines =line.split(":")
            key_param['cat_name']=lines[0]
            key_param['key_word']=lines[1]
            key_param['from_price']=lines[2]
            key_param['to_price']=lines[3].strip()
            key_list.append(key_param)
        return key_list;


    #从配置文件里面获取京东带爬取商品的关键字
    def getJDKeyWordJson(file):
        keyword_list = []
        f = open(file, "r", encoding='UTF-8')
        lines = f.readlines()  # 读取全部内容

        for line in lines:
            obj = {}
            keywords = line.split("_")
            obj['key'] = keywords[2].strip()
            obj['catName'] = line.split("_")[0]+"_"+line.split("_")[1]+"_"+line.split("_")[2]
            obj['fromPrice']= keywords[3].strip()
            obj['toPrice'] = keywords[4].strip()
            keyword_list.append(obj)
        return keyword_list;






if __name__ == '__main__':
    ks = JDUtil.getJDKeyWordJson("../config/jd_all_keyword.txt")
    for k in ks:
        print(k)
