# this is use python script!
# -*- coding: UTF-8 -*-
#爬虫模拟京东登录且京东抓取商品
from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector
import urllib
import scrapy
from scrapy.http import Request, FormRequest
from aisr_crawler.util.handlestr import HandleStr as hs
from aisr_crawler.item.crawelr_item import JDSpiderItem
from aisr_crawler.middleware.cookie.cookiejar import CookieJar as cj
from aisr_crawler.util.jingdong import JDUtil as jd
import time

#抓取京东的商品
class JingDongSpider(CrawlSpider):

    post_headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36",
        "Referer": "http://media.jd.com",
    }

    name = "jdCookeiSpiders"

    start_urls = [

    ]

    #构造参数
    param ={}
    param['pageSize']='50'
    #param['keyword'] ='笔记本'

    httpurl ='https://media.jd.com/gotoadv/goods'

    keywords=["笔记本","空调","电视机","洗衣机"]

    # param_list = jd.createSearchParam("aisr_crawler/config/jd_key.txt")
    # param_list=[]
    cat_name =""
    for p in keywords:
        param['keyword'] = p
        param['fromPrice'] ='100'
        param['toPrice'] = '10000'
        cat_name = p
        data =urllib.parse.urlencode(param)
        page =1
        while page <= 4:
              start_urls.append(httpurl+"?" +data+"&pageIndex="+str(page))
              page+=1

    #通过直接使用COOKIE进行登录
    def start_requests(self):
        #ck = 'unpl=V2_ZzNtbUVVRhZ0CRQEcxoLBWJWFg0RB0RGIQpAVSlOX1E0V0FdclRCFXMUR1BnG10UZwQZXEdcQBFFCEdkexhdBGYKF1hGXnMRJwtPAHJKCAIyBhZZFlRBJUULRmR7GGwFZQsTX0pRRBV3OHZTSykaXDxGVABKVEslcABAVHoZXQRjMxNtQ2cIe3RFRlZzGF4NYQQSX3JWcxY%3d; mobilev=html5; mba_muid=1496131508405678339613; __jdv=122270672|baidu|-|organic|not set|1496226156058; ssid="SGDDNESuTF+ATb5b+IUJVQ=="; masterClose=yes; 3AB9D23F7A4B3C9B=PD7QC76TTQHMQ5PHP2FDISPSDZVAUTSP4I447EYS3EUY4RRLGWHSUFLVQJ4Y2NJJQ2SHNFL2QXM5276R64SJQLVDEM; TrackID=1vnJxzgRJhqVN4E4s7zuLzAB0oIxnNB1VWJyYUmJIzyTGMdBtUgT-qMx94gDCymhvlVBfRev7F0SVYXz4Efq0fw; pinId=_4Vc37lERPk; _tp=1p445VhAqKBizAUsKQ93lg%3D%3D; logining=1; _pst=520bsj; ceshi3.com=000; thor=3E5861AF1D99F9183C5A3C2EB78D3BB7179C2DBD62B64C85A84FCB8ED3B6B7F46F9FD6920E4E246639BC147414B648F248EFBA30896AE05B3D04C14380966F68F94C3B500AAE6070CD5E75369CB42439203937E7D2D7EE348D99938803326F7580D1183094DCA14D68F3C2FCF8098293ED30AF2FCAB14A259686196231E12210; pin=520bsj; unick=520bsj; __jda=108460702.14961324377181286274750.1496132437.1496381400.1496413010.18; __jdb=108460702.4.14961324377181286274750|18.1496413010; __jdc=108460702; __jdu=14961324377181286274750'
        ck ='ipLoc-djd=1-72-4137-0; areaId=1; unpl=V2_ZzNtbRVSShR8CRYBKR9ZUmIBQl5LUEsTIFgUVX8aCAcyUEJbclRCFXMUR1NnGFUUZwEZWUtcRxFFCEdkeR5VAWEzEm03VkERPFMaXX5BGUZlVEdeGQMdYkULRmRzKVwAbwQVWEJSRBdzCk5Uex1bDW8FFF1KZ3MSRTgdARUdDwE1B0ZUFlAQF3Zcdld4GFgGZAMWWHJWcxRFQyhVNhlZDWAEF11HUEETdwBGVH8eVA1hBRJVclZzFg%3d%3d; __jdv=122270672|fun.fanli.com|t_36857_1|tuiguang|f48080adc74f43a28697dac052e3dba7|1496901579456; ssid="G2z2/2AMTYqADKoKV/cQAA=="; 3AB9D23F7A4B3C9B=PD7QC76TTQHMQ5PHP2FDISPSDZVAUTSP4I447EYS3EUY4RRLGWHSUFLVQJ4Y2NJJQ2SHNFL2QXM5276R64SJQLVDEM; TrackID=1wG7CcTnoViFr4X8f-nwW-hcJF0xUkHn310x8UtkeBNj750sb0P7MnKcK823mwMhn-AlPY_LNn5baf_5ZCcE5eRcAPNWwaoDk2S0joCLfI08; pinId=t8rv_49NTAXiId-dUhO1MA; _tp=%2B2IO5ajDcIBy09A8jW%2BKjA%3D%3D; logining=1; _pst=youhaohuo888; ceshi3.com=000; thor=51B618A6EBBC081F05F440B10BD3E8CEF198E5136E6C9F1B142FDA273F8D1CF763A65E0CAD6B56E0CA2266DC1BBEBEBCE3741DBDD93326DA5D5AA160423870B280756298632F77C3D62F5E71714E28C93B8A84D4BB088324146CB38EF9EC43C324A232C8E7107652641847B4B65541F40DB5D7A4A4C29CCA193830D70A90F3BB776A769BFDF67A6128148FFCF19E2C7E; pin=youhaohuo888; unick=youhaohuo888; __jda=108460702.14966414637391156997719.1496641464.1496999166.1497070785.15; __jdb=108460702.3.14966414637391156997719|15.1497070785; __jdc=108460702; __jdu=14966414637391156997719'
        cookies =cj.getCookie(ck)
        for url in self.start_urls:
            print('page_url',url)
            #return [Request(url=url,headers=self.post_headers, cookies=cookies, callback=self.parse)]
            yield  scrapy.Request(url=url,headers=self.post_headers,cookies=cookies,callback=self.parse)

    #解析具体的ITEM
    def parse(self, response):
        print('status', response.status)
        body = response.body.decode(response.encoding)
        # print("body", body)
        if '请登录' in body or '请使用京东商城账号登录' in body:
            print("对不起cookie已经失效,请重新登录系统!")
        elif '400 Bad Request' in body:
            print("对不起爬虫请求被京东反爬虫系统屏蔽了")
        else:
            selector = Selector(response)
            first_id = selector.xpath('//*[@id="goodsQueryForm"]/div[2]/div/div/div/div[2]/ul/li/@skuid').extract()
            if len(first_id) > 0:
                print('已经成功获取到数据,准备解析数据...')
                li_list = selector.xpath('//*[@id="goodsQueryForm"]/div[2]/div/div/div/div[2]/ul/li')
                for sel in li_list:
                    spu_id = sel.xpath('./@skuid').extract()[0]
                    real_stuff_id = spu_id + "333"
                    source = "jd"
                    url = sel.xpath('./div/div[1]/a/@href').extract()[0]
                    img_url = sel.xpath('./div/div[1]/a/img/@src').extract()[0]
                    title = sel.xpath('./div/div[2]/a/text()').extract()[0]
                    price = sel.xpath('./div/div[2]/div[1]/span[2]/span/text()').extract()[0].strip()
                    money_ratio = sel.xpath("./div/div[2]/div[2]/div[2]/em/text()").extract()[0]
                    order_num = sel.xpath("./div/div[2]/div[2]/div[5]/em/text()").extract()[0]
                    shop_name = ""
                    start_date = sel.xpath('./div[2]/a/@data-startdate').extract()[0]
                    end_date = sel.xpath('./div[2]/a/@data-enddate').extract()[0]

                    print('title', title)
                    # 封装item
                    jdItem = JDSpiderItem();
                    # 实际商品id
                    jdItem['real_stuff_id'] = spu_id
                    # 商品名称
                    title = title
                    jdItem['name'] = hs.patternHanZi(title)
                    # 原价
                    jdItem['reserve_price'] = 0
                    # 商品最终价格
                    jdItem['final_price'] = float(price.replace('￥',''))
                    # jdItem
                    jdItem['rebate_id'] = 0
                    # 推广佣金比
                    jdItem['promotion_rate'] = money_ratio
                    # android推广链接
                    jdItem['android_promotion_url'] = "#"
                    # ios推广链接
                    jdItem['ios_promotion_url'] = "#"
                    # 商品链接
                    jdItem['url'] = url
                    # 商品图片链接
                    img_url = img_url
                    if "http" in img_url:
                        jdItem['img_url'] = img_url
                    else:
                        jdItem['img_url'] = "http:" + img_url
                    # 商品类目cat_id
                    jdItem['cat_id'] = 0
                    #商品类目简称
                    jdItem['cat_name'] = self.cat_name
                    # 商品状态
                    jdItem['status'] = 0
                    # 商品来源
                    jdItem['source'] = source
                    # 商品统一ID
                    jdItem['id'] = real_stuff_id
                    # 商家名称
                    jdItem['shop_name'] = shop_name
                    # 推广销量
                    jdItem['order_num'] = order_num
                    # 创建时间
                    jdItem['create_time'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                    # 更新时间
                    jdItem['update_time'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                    jdItem['operator_source'] = "xushaobin"
                    jdItem['start_date'] = start_date
                    jdItem['end_date'] = end_date
                    yield jdItem
            else:
             print('本次没有查询到任何数据,请重新查询数据!')