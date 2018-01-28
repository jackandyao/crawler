# # this is use python script!
# # -*- coding: UTF-8 -*-
# import json
# from scrapy.spiders import CrawlSpider
# from aisr_crawler.item.crawelr_item import TaoBaoSpiderItem
# from aisr_crawler.util.taobao import TaoBaoUtil as tu
# from aisr_crawler.util.handlestr import HandleStr as hs
# from aisr_crawler.util.dict import DictMapUtil as dmu
# from aisr_crawler.util.filerw import FileHandle as fh
# import sys
# import platform
# from aisr_crawler.util.phone import PhoneMessage as pm
# import time
# import datetime
# import scrapy
# #sadd myspider:start_urls http://www.example.com
#
# class  TaobaoSpider(CrawlSpider):
#     name = "taobaospider"
#
#     start_urls = [
#         "茶_白茶(新)_白茶",
#         "茶_白茶(新)_白毫银针",
#         "茶_白茶(新)_白牡丹",
#         "茶_白茶(新)_贡眉",
#         "茶_白茶(新)_寿眉",
#         "茶_白茶(新)_福鼎高山寿眉",
#         "茶_白茶(新)_正宗福鼎白茶"
#     ]
#     startTime =  datetime.datetime.now()
#     param_file = "aisr_crawler/config/taobao_param.txt"
#     key_file = "aisr_crawler/config/tb_keyword.txt"
#     phone_file ="aisr_crawler/config/phone.txt"
#     type = "all"
#
#
#
#     page_result={}
#     key_len = len(start_urls)
#
#     def make_request_from_data(self, data):
#         return self.make_requests_from_url(data)
#
#     def make_requests_from_url(self, url):
#         return scrapy.Request(url, callback=self.parse_url, dont_filter=True)
#
#     #解析每个关键字的URL 且放到缓存队列
#     def parse_url(self,response):
#         ks = response.url
#         print('ks',ks)
#         obj=self.getSearchKeyWord(ks)
#         page_result = tu.getTaoBaoPageByKeyword(type, obj["key"], param_file)
#         print('page_reuslt', page_result)
#         falg = page_result['success']
#         if (falg == 'true'):
#             sumpage = page_result['sumpage']
#             print('实际返回页数是:' + str(sumpage) + ",key:" + key)
#             httpUrl = dmu.getHttpUrlByType(type)
#             data = dmu.createTaoBaoHttpParam(type, key, param_file)
#             fullurl = httpUrl + "?" + data;
#             page = 1;
#             while page <= sumpage:
#                 reqUrl = fullurl + "&" + "toPage=" + str(page)
#                 yield scrapy.Request(reqUrl,callback=self.parse_item,meta={'ks': ks})
#                 page += 1;
#                 endTime = datetime.datetime.now()
#             key_len = key_len - 1
#         else:
#             key_len = key_len - 1
#             time.sleep(0.1)
#             no_file = open("E:/pycharm/crawler/aisr_crawler/aisr_crawler/config/no_keyword.txt", 'a', encoding='utf8')
#             no_file.writelines(key + "\n")
#             no_file.close()
#         print("key_len", key_len)
#         return
#
#     #进行关键字切割
#     def getSearchKeyWord(self,ks):
#         list = ks.split("_")
#         obj={}
#         obj['key']=list[2]
#         obj['catName'] =ks
#         return obj
#
#     #解析具体需要获取的商品内容
#     def parse_item(self,response):
#         print('url',response.url)
#         ks =response.meta['ks']
#         jsonobject = json.loads(response.body_as_unicode())
#         objlist = jsonobject['data']['pageList'];
#         for obj in objlist:
#             taoBaoItem = TaoBaoSpiderItem();
#             # 实际商品id
#             taoBaoItem['real_stuff_id'] = obj['auctionId']
#             # 商品名称
#             title=obj['title']
#             taoBaoItem['name'] = hs.patternHanZi(title)
#             # 原价
#             taoBaoItem['reserve_price'] = obj['reservePrice']
#             # 商品最终价格
#             taoBaoItem['final_price'] = obj['zkPrice']
#             # 返利类型rebate表id
#             taoBaoItem['rebate_id'] = 0
#             # 推广佣金比
#             taoBaoItem['promotion_rate'] = obj['tkRate']
#             # android推广链接
#             taoBaoItem['android_promotion_url'] = "#"
#             # ios推广链接
#             taoBaoItem['ios_promotion_url'] = "#"
#             # 商品链接
#             taoBaoItem['url'] = obj['auctionUrl']
#             # 商品图片链接
#             img_url = obj['pictUrl']
#             if "http" in img_url:
#                 taoBaoItem['img_url'] = img_url
#             else:
#                 taoBaoItem['img_url'] = "http:"+img_url
#
#             # 商品类目cat_id
#             #taoBaoItem['cat_id'] = self.obj['catId']
#             taoBaoItem['cat_id'] = ''
#             taoBaoItem['cat_name'] = ks["catName"]
#             # 商品状态
#             taoBaoItem['status'] = 0
#             # 商品来源
#             use_type = obj['userType']
#             source = self.getSourceName(use_type)
#             taoBaoItem['source'] = source
#             # 商品统一ID
#             id = str(obj['auctionId']) + str(self.getSourceCode(source))
#             taoBaoItem['id'] = id
#             # 店铺id
#             taoBaoItem['shop_id'] = obj['sellerId']
#             # 商家名称
#             taoBaoItem['shop_name'] = obj['shopTitle']
#             # 推广销量
#             taoBaoItem['order_num'] = obj['biz30day']
#             # 推广销量
#             taoBaoItem['click_num'] = 0
#             # 创建时间
#             taoBaoItem['create_time'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
#             # 更新时间
#             taoBaoItem['update_time'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
#             taoBaoItem['operator_source']=""
#             yield taoBaoItem
#
#     #根据变换转换对应的商品来源
#     @staticmethod
#     def getSourceName(user_type):
#         if user_type==0:
#             return "taobao";
#         elif user_type==1:
#             return "tmall";
#         return "null";
#
#
#     #根据商品来源转换对应的商品来源编码
#     @staticmethod
#     def getSourceCode(sourceName):
#         if sourceName=="taobao":
#             return 111;
#         elif sourceName=="tmall":
#             return 222;
#         else:
#             return 333;
