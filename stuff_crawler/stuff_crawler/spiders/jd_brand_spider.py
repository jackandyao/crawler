from scrapy.spiders import CrawlSpider
from scrapy.conf import settings
from scrapy.selector import Selector
from component.util.param_util import ConditionFactory as cf
import scrapy,json,time,sys
from component.util.system_util import SystemUtil as syst
from component.util.handle_util import HandleUtil as hd
import re
#抓取某个关键字对应可能包含的品牌
class JdBrandSpider(CrawlSpider):
    plat_form = syst().getPlatform()
    if (plat_form == "linux"):
        dir_name = sys.argv[0]
    else:
        dir_name = settings['SEARCH_DIR_KW']


    name = "jdbrand"
    start_urls = []

    # 通过get请求 只能获取到前40个品牌
    def start_requests(self):
        jdInstance = cf().getCondtionInstance("JD")()
        keywords = jdInstance.getSearchKeyWordList(self.dir_name,settings['STUFF_DIR_PATH'])
        for key in keywords:
            obj = jdInstance.getSearchKeyWord(key)
            cat_name = obj['cat_name']
            # cat_name = "食品"
            cat_path = obj['cat_path']
            http_url = "https://search.jd.com/Search?keyword=" + cat_name + "&enc=utf-8qrst=1&rt=1&stop=1&vt=2"
            yield scrapy.Request(url=http_url,meta={'keyword':cat_name,'cat_path':cat_path})

    # 使用post请求 获取全部品牌
    # def start_requests(self):
    #     jdInstance = cf().getCondtionInstance("JD")()
    #     keywords = jdInstance.getSearchKeyWordList(self.dir_name,settings['STUFF_DIR_PATH'])
    #     for key in keywords:
    #         obj = jdInstance.getSearchKeyWord(key)
    #         cat_name = obj['cat_name']
    #         # cat_name = "食品"
    #         cat_path = obj['cat_path']
    #         http_url = "https://search.jd.com/brand.php"
    #         data ={"keyword":cat_name,"enc":"utf-8","qrst":"1","rt":"1","vt":"2"}
    #         # yield scrapy.Request(url=http_url,meta={'keyword':cat_name,'cat_path':cat_path})
    #         yield scrapy.FormRequest(
    #             url=http_url,
    #             formdata=data,
    #             meta={'keyword': cat_name, 'cat_path': cat_path},
    #             callback=self.parse
    #         )


    def parse(self, response):
        keyword =response.meta['keyword']
        # print('keyword',keyword)
        body = response.body.decode(response.encoding)
        print('body',response.body)
        if "抱歉，没有找到与" in body:
            print("对不起根据关键字:"+keyword +"没有查询到任何结果！")
        else:
            brand_file = self.dir_name+".txt"
            full_path = settings['JD_BRAND_PATH']+"/" + brand_file
            sel = Selector(response)
            # brand_xpath='//*[@id="J_selector"]/div[1]/div/div[2]/div[2]/ul'
            brand_xpath ='//*[@id="J_selector"]/div[1]/div/div[2]/div[2]/ul/li'
            li_list = sel.xpath(brand_xpath)
            print('len',len(li_list))
            brand_list = []
            for l in li_list:
                brand = l.xpath('./a/@title').extract()[0]
                brand_list.append(hd.regexChinese(str(brand).strip()))
            str_list = ",".join(brand_list)
            with open(full_path, 'a') as f:
                content = keyword + ":"+str_list
                f.write(content + '\n')
            print("["+keyword+"]"+"对应的品牌名称抓取完毕")