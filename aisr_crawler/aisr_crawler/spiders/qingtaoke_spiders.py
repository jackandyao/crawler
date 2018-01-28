# # this is use python script!
# # -*- coding: UTF-8 -*-
# # 爬取轻淘客网站数据
# # this is use python script!
# # -*- coding: UTF-8 -*-
# from scrapy import Request
# from scrapy.spiders import CrawlSpider
# from scrapy.selector import Selector,HtmlXPathSelector
# import re
# import scrapy
# #按照一定规则进行数据抓取并解析
# class dmbjSpider(CrawlSpider):
#     name="qtknzspider"
#     #redis_key="novelspider:start_urls"
#     #'http://www.qingtaoke.com/qingsou?cat=11&page=1'
#     start_urls=[];
#     for i in range(0, 57):
#         start_urls.append('http://www.qingtaoke.com/qingsou?cat=10&s_type=1&sort=1&page='+str(i+1))
#     for i in range(0, 23):
#         start_urls.append('http://www.qingtaoke.com/qingsou?cat=11&s_type=1&sort=1&page='+str(i+1))
#     for i in range(0, 26):
#         start_urls.append('http://www.qingtaoke.com/qingsou?cat=12&s_type=1&sort=1&page='+str(i+1))
#     for i in range(0, 55):
#         start_urls.append('http://www.qingtaoke.com/qingsou?cat=2&s_type=1&sort=1&page='+str(i+1))
#     for i in range(0, 22):
#         start_urls.append('http://www.qingtaoke.com/qingsou?cat=3&s_type=1&sort=1&page='+str(i+1))
#     for i in range(0, 66):
#         start_urls.append('http://www.qingtaoke.com/qingsou?cat=4&s_type=1&sort=1&page='+str(i+1))
#     for i in range(0, 55):
#         start_urls.append('http://www.qingtaoke.com/qingsou?cat=5&s_type=1&sort=1&page='+str(i+1))
#     for i in range(0, 34):
#         start_urls.append('http://www.qingtaoke.com/qingsou?cat=6&s_type=1&sort=1&page='+str(i+1))
#     for i in range(0, 29):
#         start_urls.append('http://www.qingtaoke.com/qingsou?cat=7&s_type=1&sort=1&page='+str(i+1))
#     for i in range(0, 23):
#         start_urls.append('http://www.qingtaoke.com/qingsou?cat=8&s_type=1&sort=1&page='+str(i+1))
#
#
#     #抓取内容解析
#     def parse_item(self,response):
#         url=str(response.url)
#         print('url', url)
#         catNum=url[url.index("cat=")+4:url.index("&")]
#         print("catNum",catNum)
#         selector=Selector(response)
#         article = response.xpath('//*[@id="createDom"]/div')
#         item = {}
#         for each in article:
#             imageUrl = each.xpath('./div/div/div/a/img/@data-img').extract()[0]
#             item['imageUrl']=imageUrl
#             imagehref = each.xpath('./div/div/div/a/@href').extract()[0]
#             item['imagehref']=imagehref
#             title = each.xpath('./div/div/div/a/img/@alt').extract()[0]
#             item['title']=title
#             price = each.xpath('./div/div/div[3]/div/span[2]/text()').extract()[0]
#             item['price']=price
#             yongjin1 = each.xpath('./div/div/div[4]/span[2]/i/text()').extract()[0]
#             yongjin2=each.xpath('./div/div/div[4]/span[2]/b/text()').extract()[0]
#             item['yongjin'] = yongjin1+yongjin2
#             fanquan = each.xpath('./div/div/div[5]/a/span/i/text()').extract()[0]
#             item['fanquan']=fanquan
#             if(catNum=='10'):
#                item['cat_cn'] = '女装'
#                item['cat_en'] ='nvzhuang'
#             if (catNum == '11'):
#                 item['cat_cn'] = '内衣'
#                 item['cat_en'] = 'neiyi'
#             if (catNum == '12'):
#                 item['cat_cn'] = '男装'
#                 item['cat_en'] = 'nanzhuang'
#             if (catNum == '2'):
#                 item['cat_cn'] = '母婴'
#                 item['cat_en'] = 'muying'
#             if (catNum == '3'):
#                 item['cat_cn'] = '美装'
#                 item['cat_en'] = 'meizhuang'
#             if (catNum == '4'):
#                 item['cat_cn'] = '居家'
#                 item['cat_en'] = 'jujia'
#             if (catNum == '5'):
#                 item['cat_cn'] = '鞋包配饰'
#                 item['cat_en'] = 'xiebaopeishi'
#             if (catNum == '6'):
#                 item['cat_cn'] = '美食'
#                 item['cat_en'] = 'meishi'
#             if (catNum == '7'):
#                 item['cat_cn'] = '文体'
#                 item['cat_en'] = 'wenti'
#             if (catNum == '8'):
#                 item['cat_cn'] = '家电数码'
#                 item['cat_en'] = 'jiadianshuma'
#             yield item
#
#
#     def parsUrl(xx):
#         m = re.search(r"window\.location\.href='([^']+)'",str(xx)).group(1)
#         return str(m)
#
#
#     def parse(self,response):
#         print("test=",response.body)
#         url=re.search(r"window\.location\.href='([^']+)'",str(response.body)).group(1)
#         return scrapy.Request(url,callback=self.parse_item)
