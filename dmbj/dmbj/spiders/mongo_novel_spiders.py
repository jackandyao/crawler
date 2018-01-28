# # this is use python script!
# # -*- coding: UTF-8 -*-
# from scrapy import Request
# from scrapy.spiders import CrawlSpider,Rule
# from scrapy.selector import Selector,HtmlXPathSelector
# from dmbj.items import DmbjItem
# from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
# #按照一定规则进行数据抓取并解析
# class dmbjSpider(CrawlSpider):
#     name="dmbjspider"
#     #redis_key="novelspider:start_urls"
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
#         print('desc',desc)
#         sites = sell.xpath('/html/body/section/div[2]/div/article/a')
#         print('sites', sites)
#         item={}
#         for site in sites:
#             print(site)
#             item['title'] = title
#             item['desc'] = desc
#             item['zhangjieurl']=site.xpath('@href').extract()[0]
#             item['zhangjie'] = site.xpath('text()').extract()[0]
#             #print('字典item[zhangjieurl]',item['zhangjieurl'])
#             yield Request(item['zhangjieurl'], meta={'item': item}, callback=self.parse_item_content)
#

    # rules = (
    #     # 提取匹配 huhuuu/default.html\?page\=([\w]+) 的链接并跟进链接(没有callback意味着follow默认为True)
    #     Rule(SgmlLinkExtractor(allow=('huhuuu/default.html\?page\=([\w]+)', ),)),
    #
    #     # 提取匹配 'huhuuu/p/' 的链接并使用spider的parse_item方法进行分析
    #     Rule(SgmlLinkExtractor(allow=('huhuuu/p/', )), callback='parse_item'),
    # )
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
#         print(items)
#         for item in items:
#
#             yield Request(item, callback=self.parse_item)
