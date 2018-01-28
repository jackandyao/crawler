import scrapy
from scrapy.selector import Selector
from jdmulu.items import JdproductItem

class jdtestSpider(scrapy.Spider):
    name = "jdtest"
    allowed_domains = ["jd.com"]
    start_urls = ["https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&suggest=3.his.0.0&cid2=653&cid3=655&page=3&s=58&click=0"]

    def parse(self, response):
        print('body',response.xpath('//*[@id="brand-36404"]/a'))
        pass