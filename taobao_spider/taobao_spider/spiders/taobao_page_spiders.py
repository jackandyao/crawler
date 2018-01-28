# this is use python script!
# -*- coding: UTF-8 -*-
import json
import time
from scrapy.spiders import CrawlSpider
from items import TaobaoSpiderItem
from spiders.page import TaoBaoUtil as tu
from spiders.dict import DictMapUtil as dmu
import sys
import platform
from phone import PhoneMessage as pm
import time
import datetime

#sadd myspider:start_urls http://www.example.com

class  TaobaoSpider(CrawlSpider):
    name = "taobaospider"
    startTime =  datetime.datetime.now()
    if(platform.system()=="Windows"):
        print("进入windows系统")
        param_file = "E:/pycharm/crawler/taobao_spider/taobao_spider/spiders/param.txt"
        key_file = "E:/pycharm/crawler/taobao_spider/taobao_spider/spiders/keyword.txt"
        phone_file ="E:/pycharm/crawler/taobao_spider/taobao_spider/spiders/phone.txt"
        type = "all"
    else:
        print("进入linux系统")
        key_file = sys.argv[1]
        param_file = sys.argv[2]
        phone_file = sys.argv[3]
        search_type = sys.argv[4]

    #获取带爬取所有商品的目录关键字
    keywords = tu.getKeyWord(key_file)
    #print("ks",keywords)
    #keywords = ["扇子", "凉席","蚊帐","窗帘","电蚊拍"]
    #keywords = [ "凉席"]
    #print("keywords_list",keywords)
    page_result={}
    key_len = len(keywords)
    for key in keywords:
        page_result =tu.getTaoBaoPageByKeyword(type,key,param_file)
        falg = page_result['success']
        if(falg=='true'):
            sumpage=page_result['sumpage']
            print('实际返回页数是:'+str(sumpage)+",key:"+key)
            start_urls = []
            httpUrl = dmu.getHttpUrlByType(type)
            data = dmu.createTaoBaoHttpParam(type,key,param_file)
            fullurl = httpUrl+"?"+data;
            page = 1;
            while page <= 10:
                start_urls.append(fullurl+"&"+"toPage="+str(page))
                page += 1;
                endTime = datetime.datetime.now()
            key_len=key_len-1
            #msg ="恭喜你,爬虫系统已经成功爬取关键字为:"+"["+key+"]"+"的所有商品,抓取页数为:"+str(sumpage)+",抓取数据记录条数是:"+str(sumpage*40)+"条"+",爬取数据耗时为:"+str((endTime-startTime).seconds)+"s"
            #pm.sendPhoneMsg(phone_file,msg)
        else:
            key_len = key_len - 1
            time.sleep(0.1)
            no_file=open("E:/pycharm/crawler/taobao_spider/taobao_spider/spiders/no_keyword.txt",'w',encoding='utf8')
            no_file.writelines(key+"\n")
            no_file.close()
        print("key_len",key_len)
    #解析具体需要获取的商品内容
    def parse(self,response):
        print('url',response.url)
        jsonobject = json.loads(response.body_as_unicode())
        objlist = jsonobject['data']['pageList'];
        for obj in objlist:
            taoBaoItem = TaobaoSpiderItem();
            # 实际商品id
            taoBaoItem['real_stuff_id'] = obj['auctionId']
            # 商品名称
            title=obj['title']
            taoBaoItem['name'] = tu.patternHanZi(title)
            # 原价
            taoBaoItem['reserve_price'] = obj['reservePrice']
            # 商品最终价格
            taoBaoItem['final_price'] = obj['zkPrice']
            # 返利类型rebate表id
            taoBaoItem['rebate_id'] = 0
            # 推广佣金比
            taoBaoItem['promotion_rate'] = obj['tkRate']
            # android推广链接
            taoBaoItem['android_promotion_url'] = "#"
            # ios推广链接
            taoBaoItem['ios_promotion_url'] = "#"
            # 商品链接
            taoBaoItem['url'] = obj['auctionUrl']
            # 商品图片链接
            img_url = obj['pictUrl']
            if "http" in img_url:
                taoBaoItem['img_url'] = img_url
            else:
                taoBaoItem['img_url'] = "http:"+img_url

            # 商品类目cat_id
            taoBaoItem['cat_id'] = ""
            # 商品状态
            taoBaoItem['status'] = 0
            # 商品来源
            use_type = obj['userType']
            source = self.getSourceName(use_type)
            taoBaoItem['source'] = source
            # 商品统一ID
            id = str(obj['auctionId']) + str(self.getSourceCode(source))
            taoBaoItem['id'] = id
            # 店铺id
            taoBaoItem['shop_id'] = obj['sellerId']
            # 商家名称
            taoBaoItem['shop_name'] = obj['shopTitle']
            # 推广销量
            taoBaoItem['order_num'] = obj['biz30day']
            # 推广销量
            taoBaoItem['click_num'] = 0
            # 创建时间
            taoBaoItem['create_time'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            # 更新时间
            taoBaoItem['update_time'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            taoBaoItem['operator_source']=""
            yield taoBaoItem

    #根据变换转换对应的商品来源
    @staticmethod
    def getSourceName(user_type):
        if user_type==0:
            return "taobao";
        elif user_type==1:
            return "tmall";
        return "null";


    #根据商品来源转换对应的商品来源编码
    @staticmethod
    def getSourceCode(sourceName):
        if sourceName=="taobao":
            return 111;
        elif sourceName=="tmall":
            return 222;
        else:
            return 333;
    #获取商品目录ID
    @staticmethod
    def getCategoryId(file):
        return;