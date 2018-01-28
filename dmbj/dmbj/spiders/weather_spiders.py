# this is use python script!
# -*- coding: UTF-8 -*-
from scrapy import Request
from scrapy.spiders import CrawlSpider
from dmbj.items import WeatherItem
#按照一定规则进行数据抓取并解析
class dmbjSpider(CrawlSpider):
    name="dmbjspider"
    allowed_domains = ['weather.com.cn']
    start_urls=["http://www.weather.com.cn/weather/101280101.shtml"]

    #抓取内容解析
    def parse(self, response):
        for sel in response.xpath('//*[@id="7d"]/ul/li'):
            item = WeatherItem()
            item['weatherDate'] = sel.xpath('h1/text()').extract()
            item['weatherDate2'] = sel.xpath('h2/text()').extract()
            item['weatherWea'] = sel.xpath('p[@class="wea"]/text()').extract()
            item['weatherTem1'] = sel.xpath('p[@class="tem tem1"]/span/text()').extract() + sel.xpath(
                'p[@class="tem tem1"]/i/text()').extract()
            item['weatherTem2'] = sel.xpath('p[@class="tem tem2"]/span/text()').extract() + sel.xpath(
                'p[@class="tem tem2"]/i/text()').extract()
            item['weatherWin'] = sel.xpath('p[@class="win"]/i/text()').extract()
            print('item',item)
            yield item