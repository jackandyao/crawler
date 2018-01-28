import scrapy
from scrapy.selector import Selector
# from jdmulu.items import JdproductItem
import os
class jdproductSpider(scrapy.Spider):
    name = "jdproduct"
    allowed_domains = ["jd.com"]
    start_urls = ["https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8"]

    #url = "https://search.jd.com/Search?keyword=电子书&enc=utf-8"

    def parse(self, response):
        keyword_list = []
        f = open('data_jd.txt', 'r', encoding='UTF-8')
        lines = f.readlines()  # 读取全部内容
        #print('lines',lines)
        # for line in lines:
        #     ls = line.split("_")
        #     filename = line
        #     keyword = ls[2]
        #     keyword_list.append(keyword.strip())

        #print('line',keyword_list)
        for line in lines:
            #print(keyword[0])
            ks = line.split("_")
            url_link = "https://search.jd.com/Search?keyword=" + ks[2] + "&enc=utf-8"
            #print('url_link',url_link)
            yield scrapy.Request(url_link,callback=self.parse_link,meta={'filename':line})
            print('name',line)


    def parse_link(self, response):
        item= {}
        #print('url',response.url)
        filename = str(response.meta['filename'])
        #realname = filename+"_ID.txt"
        sel = Selector(response)
        pagestr = sel.response.xpath('//*[@id="J_topPage"]/span/i/text()').extract()
        #print('page',pagestr)
        page = int(pagestr[0])
        #print('page', page)
        print('url_link',response.url)
        if(page >= 2):
            if(page >= 15):
                num = 15
            else:
                num = page
            i = 1
            while i <= 2:
                reqlink = response.url + "&page=" + str(i)
                i += 1
                yield scrapy.Request(reqlink,callback=self.parse_item,meta={'item':item})
        # print(filename)
        # os.mkdir(filename.strip()+"_ID.txt")
        file = open(filename.strip()+"_ID.txt",'w',encoding='utf-8')
        file.write(filename)
        print(file)

    def parse_item(self, response):
        # data = "手机"
        # pageurl = self.start_urls + '?'
        # print('url',pageurl)
        #print('body',response.body)
        sel = Selector(response)
        item = {}
        item['keyword'] = sel.response.xpath('//*[@id="J_crumbsBar"]/div/div/div[2]/strong/text()').extract()
        item['brand'] = sel.response.xpath('//*[@id="J_selector"]/div[1]/div/div[2]/div[2]/ul/li/a/text()').extract()

        for li in sel.xpath('//*[@id="J_selector"]/div[1]/div/div[2]/div[2]/ul/li'):
            brand = li.xpath('./a/text()').extract()[1]
            print('brand',str(brand).strip())
        # item['brand'] = sel.response.xpath('//*[@id="J_selector"]/div[1]/div/div[2]/div[2]/ul/li[1]/a/text()').extract()[1]
        #item['id'] = sel.response.xpath('//*[@id="J_goodsList"]/ul/li/@data-sku').extract()

        # id_item =response.meta['item']
        # id_item['id'] = item['id']
        #print('id',sel.response.xpath('//*[@id="J_goodsList"]/ul/li/@data-sku').extract())

        # for ul in sel.xpath('//*[@id="J_goodsList"]/ul/li'):
        #     item['id'] = ul.xpath('./@data-sku').extract()
        #     yield item
        #print('ul', item['id'])
        # print('brand',item['brand'])
        yield item



