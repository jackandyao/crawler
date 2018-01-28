# # this is use python script!
# # -*- coding: UTF-8 -*-
# from scrapy import Request
# from scrapy_redis.spiders import RedisSpider
# from scrapy.selector import Selector
#
# class DmbjRedisSpider(RedisSpider):
#     name="dmbjspider"
#     redis_key="dmbj:start_urls"
#     start_urls=['http://www.daomubiji.com']
#
#     #转换内容
#     def parse_item_content(self, response):
#         sell = Selector(response)
#         item = response.meta['item']
#         data=sell.xpath('//article[@class="article-content"]')
#         item['content'] = data.xpath('string(.)').extract()[0]
#         yield item
#
#
#     def parse_item(self, response):
#         sell = Selector(response)
#         title=sell.xpath('/html/body/div[1]/div/h1/text()').extract()[0]
#         print('title',title)
#         desc = sell.xpath('/html/body/div[1]/div/div/text()').extract()[0]
#         #print('desc',desc)
#         sites = sell.xpath('/html/body/section/div[2]/div/article/a')
#         #print('sites', sites)
#         item={}
#         for site in sites:
#             #print(site)
#             item['title'] = title
#             item['desc'] = desc
#             item['zhangjieurl']=site.xpath('@href').extract()[0]
#             item['zhangjie'] = site.xpath('text()').extract()[0]
#             #print('字典item[zhangjieurl]',item['zhangjieurl'])
#             yield Request(item['zhangjieurl'], meta={'item': item}, callback=self.parse_item_content)
#
#
#     #抓取内容解析
#     def parse(self, response):
#         selector = Selector(response)
#         article = selector.xpath('//article/p/a')
#         items = []
#         for each in article:
#
#             url = each.xpath('@href').extract()[0]
#             items.append(url)
#         #print(items)
#         for item in items:
#
#             yield Request(item, callback=self.parse_item)
