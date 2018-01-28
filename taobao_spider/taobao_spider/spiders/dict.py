# this is use python script!
# -*- coding: UTF-8 -*-
import urllib
from spiders.condition import CreateCondition as cc
#封装简单常用属性
class DictMapUtil():

    # 不同请求类型 获取不同的连接
    @staticmethod
    def getHttpUrlByType(type):

        urldic = {
            "all": "http://pub.alimama.com/items/search.json"
            , "nine": "http://pub.alimama.com/items/channel/9k9.json"
            , "twent": "http://pub.alimama.com/items/channel/20k.json"}
        return urldic[type];

    # 通过目录名称获取目录编码
    @staticmethod
    def getCatId(key):
        catIds = {
            "女装": "nvzhuang", "男装": "nanzhuang", "鞋包": "xiebao", "珠宝配饰": "zhubao", "运动户外": "huwai",
            "美妆": "meizhuang", "母婴": "muyin", "食品": "shiping", "内衣": "neiyi", "数码": "shuma", "家装": "jiazhuang"
            , "家具用品": "jiaju", "家电": "jiadian", "汽车": "qiche", "生活服务": "shenghuo", "图书音像": "tushu", "其它": "other"
        }
        return catIds[key];


    # 根据请求的参数类型不同,创建不同的http请求连接参数'
    @staticmethod
    def createTaoBaoHttpParam(type, keyWord,file):

        values = cc.createSearchCondition(file)
        print('values',values)
        values['perPageSize'] = "40"
        # 基于全站根据关键字查询
        if (type == 'all'):
            values['q'] = keyWord
            values['shopTag'] = "yxjh"
        # 基于全球购搜索
        if(type=='qqg'):
            values['typeTag']='qqg'
            values['q'] = keyWord
            values['shopTag'] = "yxjh"
        # 基于9.9根据关键字查询
        if (type == 'nine'):
            values['catIds'] =1
            values['channel'] = '9k9'
            values['level'] = "1"
        # 基于20根据关键字查询
        if (type == 'twent'):
            values['catIds'] = 1
            values['channel'] = '20k'
            values['level'] = "1"
        return urllib.parse.urlencode(values);



        return
if __name__ == "__main__":
    print(DictMapUtil.getHttpUrlByType("nine"))
