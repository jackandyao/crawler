# this is use python script!
# -*- coding: UTF-8 -*-
#爬虫模拟京东登录且京东抓取商品
from datetime import datetime
from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector
import scrapy
from scrapy.http import Request
from aisr_crawler.util.dwlimage import DwlImage
from aisr_crawler.util.codeidentify import CodeIdentHttp
from aisr_crawler.item.crawelr_item import JDSpiderItem
from aisr_crawler.util.handlestr import HandleStr as hs
from aisr_crawler.util.jingdong import JDUtil as jd
import random,urllib,time,re,os,logging,json
from aisr_crawler.util.phone import PhoneMessage as pm
from aisr_crawler.util.filerw import FileHandle as fh
#模拟京东登录并自动抓取商品
class JingDongIDSpider(CrawlSpider):

    FILE = os.getcwd()
    #请求header
    post_headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36",
        "Referer": ".media.jd.com",
    }

    httpurl = 'https://media.jd.com/gotoadv/goods'

    name = "jdIDSpiders"

    keyword = '热销'
    # 通过模拟表单自动登录
    def start_requests(self):
        loginUrl = "https://passport.jd.com/common/loginPage?from=media&ReturnUrl=http://media.jd.com/index/overview"
        return [Request(loginUrl,meta={'cookiejar' : 1}, callback = self.post_login)]

    #模拟自动登录
    def post_login(self,response):
        selector = Selector(response)
        loginForm = selector.xpath('//*[@id="formloginframe"]')
        sa_token = loginForm.xpath('./input[1]/@value').extract()[0].strip()
        uuid = loginForm.xpath('./input[2]/@value').extract()[0].strip()
        pubkey = selector.xpath('//*[@id="pubKey"]/@value').extract()[0].strip()
        token = selector.xpath('//*[@id="token"]/@value').extract()[0].strip()
        eid = selector.xpath('//*[@id="eid"]/@value').extract()[0].strip()
        verification = selector.xpath('//*[@id="JD_Verification1"]/@src').extract()

        if len(verification) > 0:
            print('登录系统出现验证码,请先获取验证码:')

            #自动识别验证码
            authcode = self.getVeryicationCode(verification)
            param = {
                'loginname': '13661825384',
                'nloginpwd': 'willamjie723',
                'authcode': authcode,
                'pubKey': pubkey,
                'sa_token': sa_token,
                'uuid': uuid,
                'eid': eid,
                '_t': token,
                'from': 'media',
                'nr': '1'
            }
        else:
           print('登录系统没有验证码,请直接输入用户名和密码:')
           param={
               'loginname': '13661825384',
               'nloginpwd': 'willamjie723',
               'pubKey': pubkey,
               'sa_token': sa_token,
               'uuid':uuid,
               'eid':eid,
               '_t':token,
               'from':'media',
               'nr':'1'
           }
        print('正在登录系统中......')
        #RormRequest基于表单请求
        yield scrapy.FormRequest.from_response(response,
                 url ='https://passport.jd.com/uc/loginService',
                 formdata=param,
                 headers=self.post_headers,
                 meta={'cookiejar': response.meta['cookiejar']},
                 callback=self.after_login,
                 dont_filter=True
                )


    #登录成功之后再请求要抓取的URL
    def after_login(self,response):
         req_cookie = response.request.headers.getlist('Cookie')
         resp_cookie = response.headers.getlist('Set-Cookie')
         body = response.body.decode(response.encoding)
         if 'success' in body:
             print("亲,恭喜您已经成功登录到京东联盟！")

             #抓取这类关键字:手机_手机配件_手机贴膜
             keyword= self.keyword
             param_list = fh().getIDListByFile(keyword)
             #print('list',param_list)
             param ={}
             for obj in param_list:
                 fs = obj['file'].split("_")
                 dir_name = fs[2]
                 dir_path = fs[0]+"_"+ fs[1]+"_"+fs[2]
                 param['keyword'] = obj['id']
                 data = urllib.parse.urlencode(param)
                 #REDIS
                 pageUrl = self.httpurl + "?" + data
                 #print('pageurl',pageUrl)
                 yield scrapy.Request(url=pageUrl, meta={'cookiejar': response.meta['cookiejar'], 'dir_name':dir_name,'dir_path':dir_path},callback=self.parse_item)
         else:
             print("抱歉,登录失败,请重新登录!")


    #获取验证码 人工输入/自动处理
    def getVeryicationCode(image_url):
        filename =  datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        codeimg = DwlImage(image_url,filename)
        code = CodeIdentHttp.identifyCodeResult(codeimg,'3004')
        return code


    #解析具体的ITEM
    def parse_item(self, response):
        #print('url',response.url)
        dir_name = response.meta['dir_name']
        dir_path = response.meta['dir_path']
        print('status', response.status)
        body = response.body.decode(response.encoding)
        # print("body", body)
        if '请登录' in body or '请使用京东商城账号登录' in body:
            print("对不起cookie已经失效,请重新登录系统!")
        elif '400 Bad Request' in body:
            print("对不起爬虫请求被京东反爬虫系统屏蔽了")
            print('keyword',dir_path)
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
                    # 封装item
                    jdItem = JDSpiderItem();
                    # 实际商品id
                    jdItem['real_stuff_id'] = spu_id
                    # 商品名称
                    title = title
                    jdItem['name'] = hs.patternHanZi(title)
                    # 原价
                    jdItem['reserve_price'] = 0
                    print(spu_id,price)
                    # 商品最终价格
                    jdItem['final_price'] = float(price.replace('￥','').replace(',',''))
                    # jdItem
                    jdItem['rebate_id'] = 0
                    # 推广佣金比
                    jdItem['promotion_rate'] = int(float(money_ratio.replace('%',''))*100)
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

                    #账号
                    jdItem['operator_source'] = "xushaobin"
                    jdItem['start_date'] = start_date
                    jdItem['end_date'] = end_date
                    jdItem['dir_name'] = dir_name
                    jdItem['dir_path'] = dir_path
                    #订单
                    yield jdItem
            else:
                print('本次没有查询到任何数据,请重新查询数据!,正准备重新查询数据...')
                time.sleep(random.randint(1, 3))


