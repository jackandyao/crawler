# # -*- coding: utf-8 -*-
#
#
# from scrapy import Field,Item
#
# #定义一个对象 用来接收爬虫要抓取的关键字段,便于后续继续处理
# class DmbjItem(Item):
#     #获取爬取的字段信息
#     bookName = Field()
#     bookTile = Field()
#     chapterNum = Field()
#     chapterName = Field()
#     chapterURL = Field()
#
# #定义一个对象来存储天启预报相信信息
# class WeatherItem(Item):
# 	weatherDate = Field()
# 	weatherDate2 = Field()
# 	weatherWea = Field()
# 	weatherTem1 = Field()
# 	weatherTem2 = Field()
# 	weatherWin = Field()
#
# #定义爬取知乎内容
# class ZhihuItem(Item):
#     url = Field()
#     name =Field()