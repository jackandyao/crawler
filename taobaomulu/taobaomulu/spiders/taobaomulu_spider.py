import scrapy
from scrapy.selector import Selector
from taobaomulu.items import TaobaomuluItem

class taobaomuluSpider(scrapy.Spider):
    name = "taobaomulu"
    allowed_domains = ["taobao.com"]
    start_urls = ["https://www.taobao.com/oshtml/categorylist.html?qq-pf-to=pcqq.c2c"]

    def parse(self, response):
        sel = Selector(response)
        #for link in sel.xpath('//div[@class=" page-layout page-main-content"]/div/div/div/div/div/div/a/@href').extract():
        for link in [#'//www.taobao.com/oshtml/categorylist-35.html?spm=a21m2.8462669.0.0.mpt8gU'#,
            # '//www.taobao.com/oshtml/categorylist-1801.html',
            # '//www.taobao.com/oshtml/categorylist-50002766.html',
            # '//www.taobao.com/oshtml/categorylist-50010788.html',
            #'//www.taobao.com/oshtml/categorylist-50012029.html',
            # '//www.taobao.com/oshtml/categorylist-50023282.html',
            # '//www.taobao.com/oshtml/categorylist-124458005.html',
            # '//www.taobao.com/oshtml/categorylist-50006843.html',
             '//www.taobao.com/oshtml/categorylist-1625.html'

        ]:
            link_page = "http:" + link
            #print('link_page',link_page)
            request = scrapy.Request(link_page, callback=self.parse_item)
            yield request

    def parse_item(self, response):
        sel = Selector(response)
        item = TaobaomuluItem()
        sites = sel.xpath('//ul[@class="category-list"and @style]/li')
        item['mulu_level1'] = sel.xpath('/html/body/div[2]/div[2]/div/div/div/div/div/a/h1/text()').extract()
        print('yijimulu',item['mulu_level1'])
        for site in sites:
            #print('site',site)
            item['mulu_level2'] = site.xpath('./a/text()').extract()
            item['mulu_level3'] = site.xpath('./div/a/text()').extract()
            #print('item1',item['mulu_level2'])
            yield item