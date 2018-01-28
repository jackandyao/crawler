from scrapy.spiders import CrawlSpider
from scrapy.conf import settings
from scrapy.selector import Selector
from component.util.param_util import ConditionFactory as cf
import scrapy,sys
from component.util.system_util import SystemUtil as syst

#通过关键字抓取对应的产品id
class JdIdSpider(CrawlSpider):

    plat_form = syst().getPlatform()
    if (plat_form == "linux"):
        dir_name = sys.argv[0]
    else:
        dir_name = settings['SEARCH_DIR_KW']

    name = "jdid"

    #重写请求的方法
    def start_requests(self):
        jdInstance = cf().getCondtionInstance("JD")()
        keywords = jdInstance.getSearchKeyWordList(self.dir_name)
        for key in keywords:
            obj = jdInstance.getSearchKeyWord(key)
            cat_name = obj['cat_name']
            cat_path = obj['cat_path']
            http_url = "https://search.jd.com/Search?keyword=" + cat_name + "&enc=utf-8"
            yield scrapy.Request(url=http_url,meta={'keyword':cat_name,'cat_path':cat_path})

    def parse(self, response):
        sel = Selector(response)
        pagestr = sel.response.xpath('//*[@id="J_topPage"]/span/i/text()').extract()
        page = int(pagestr[0])
        if (page >= 2):
            if (page >= 15):
                num = 15
            else:
                num = page
            i = 1
            while i <= num:
                reqlink = response.url + "&page=" + str(i)
                i += 1
                yield scrapy.Request(reqlink,meta={'keyword':response.meta['keyword'],'cat_path':response.meta['cat_path']}, callback=self.parse_id)

    def parse_id(self, response):
        keyword =response.meta['keyword']
        cat_path = response.meta['cat_path']
        body = response.body.decode(response.encoding)
        if "抱歉，没有找到与" in body:
            print("对不起根据关键字:" + keyword + "没有查询到任何结果！")
        else:
            brand_file = self.dir_name + ".txt"
            full_path = settings['JD_ID_PATH'] + "/" + brand_file
            sel = Selector(response)
            ids = sel.response.xpath('//*[@id="J_goodsList"]/ul/li/@data-sku').extract()
            for id in ids:
                with open(full_path, 'a') as f:
                    content =cat_path+":" + keyword + ":" + str(id).strip()
                    print(content)
                    f.write(content + '\n')
            print("[" + keyword + "]" + "相关关键字id抓取完毕")
