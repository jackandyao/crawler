import scrapy
from scrapy.selector import Selector
from jdmulu.items import JdmuluItem

class jdmuluSpider(scrapy.Spider):
    name = "jdmulu"
    allowed_domains = ["jd.com"]
    start_urls = ["https://www.jd.com/allSort.aspx"]

    def parse(self, response):
        sel = Selector(response)
        item = JdmuluItem()
        sites = sel.xpath('//div[@class="category-item m"]')
        for site in sites:
            item['mulu_level1'] = site.xpath('./div/h2/span/text()').extract()
            #print('yijimulu', item['mulu_level1'])
            site2 = site.xpath('./div[@class="mc"]/div[@class="items"]/dl')
            for site_in in site2:
                item['mulu_level2'] = site_in.xpath('./dt/a/text()').extract()
                #print('yijimulu', item['mulu_level2'])
                item['mulu_level3'] = site_in.xpath('./dd/a/text()').extract()
                yield item
#        yield item