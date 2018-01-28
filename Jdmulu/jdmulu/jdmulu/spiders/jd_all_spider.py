import scrapy
from scrapy.selector import Selector
from jdmulu.items import JdproductItem

class jdproductSpider(scrapy.Spider):
    name = "jdall"
    allowed_domains = ["jd.com"]
    start_urls = ["https://search.jd.com/Search?keyword=AGM&enc=utf-8"]

    url = "https://search.jd.com/Search?keyword=AGM&enc=utf-8"

    def parse(self, response):
        keyword_list = []
        f = open('data_phone.txt', 'r', encoding='UTF-8')
        lines = f.readlines()  # 读取全部内容
        #print('lines',lines)
        for line in lines:
            keyword_list.append(line.split())
        #print('line',keyword_list)
        for keyword in keyword_list:
            #print(keyword[0])
            url_link = "https://search.jd.com/Search?keyword=" + keyword[0] + "&enc=utf-8"
            #print('url_link',url_link)
            yield scrapy.Request(url_link,callback=self.parse_link)


    def parse_link(self, response):
        sel = Selector(response)
        pagestr = sel.response.xpath('//*[@id="J_topPage"]/span/i/text()').extract()
        #print('page',pagestr)
        page = int(pagestr[0])
        print('page', page)
        print('url_link',response.url)
        if(page >= 1):
            if(page >= 15):
                num = 15
            else:
                num = page
            i = 1
            while i <= num:
                reqlink = response.url + "&page=" + str(i)
                i += 1
                yield scrapy.Request(reqlink,callback=self.parse_item)


    def parse_item(self, response):
        # data = "手机"
        # pageurl = self.start_urls + '?'
        # print('url',pageurl)
        #print('body',response.body)
        sel = Selector(response)
        item = JdproductItem()
        item['keyword'] = sel.response.xpath('//*[@id="J_crumbsBar"]/div/div/div[2]/strong/text()').extract()
        item['brand'] = sel.response.xpath('//*[@id="J_selector"]/div[1]/div/div[2]/div[2]/ul/li/a/text()').extract()
        #print('brand',sel.response.xpath('//*[@id="J_selector"]/div[1]/div/div[2]/div[2]/ul/li/a/text()').extract())
        # for li in sel.xpath('//*[@id="J_selector"]/div[1]/div/div[2]/div[2]/ul/li'):
        #     #print('li',li)
        #     item['brand'] = li.xpath('./a/text()').extract()[1]
        #     yield item
        #item['brand'] = sel.response.xpath('//*[@id="J_selector"]/div[1]/div/div[2]/div[2]/ul/li[1]/a/text()').extract()[1]
        item['id'] = sel.response.xpath('//*[@id="J_goodsList"]/ul/li/@data-sku').extract()
        #print('id',sel.response.xpath('//*[@id="J_goodsList"]/ul/li/@data-sku').extract())

        # for ul in sel.xpath('//*[@id="J_goodsList"]/ul/li'):
        #     item['id'] = ul.xpath('./@data-sku').extract()
        #     yield item
        #print('ul', item['id'])
        yield item



