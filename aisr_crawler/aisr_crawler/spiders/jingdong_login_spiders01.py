# this is use python script!
# -*- coding: UTF-8 -*-
#爬虫模拟京东登录且京东抓取商品
import datetime
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
import jieba
#模拟京东登录并自动抓取商品
class JingDongSpider(CrawlSpider):

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

    name = "jdLoginSpiders"

    def start_requests(self):
        # f = open(self.test_file, 'r', encoding='UTF-8')
        # lines = f.readlines()
        lines =["苹果手机","三星手机"]
        for line in lines:
            # ks = line.split("_")
            # keywrod = ks[2]
            http_url = "https://search.jd.com/Search?keyword=" + line + "&enc=utf-8"
            self.start_urls.append(http_url)

        for url in self.start_urls:
            yield self.make_requests_from_url(url)

    # def parse(self, response):
    #     sel = Selector(response)
    #     pagestr = sel.response.xpath('//*[@id="J_topPage"]/span/i/text()').extract()
    #     page = int(pagestr[0])
    #     # print('url_link', response.url)
    #     if (page >= 2):
    #         if (page >= 15):
    #             num = 15
    #         else:
    #             num = page
    #         i = 1
    #         while i <= 2:
    #             reqlink = response.url + "&page=" + str(i)
    #             i += 1
    #             yield scrapy.Request(reqlink, callback=self.parse_id)

    # def parse_id(self, response):
    #     sel = Selector(response)
    #     # brand = sel.response.xpath('//*[@id="J_selector"]/div[1]/div/div[2]/div[2]/ul/li/a/text()').extract()
    #     ids = sel.response.xpath('//*[@id="J_goodsList"]/ul/li/@data-sku').extract()
    #     for id in ids:
    #         #print('id', id)
    #         loginUrl = "https://passport.jd.com/common/loginPage?from=media&ReturnUrl=http://media.jd.com/index/overview"
    #         yield scrapy.Request(loginUrl, meta={'cookiejar': 1, 'id': id}, callback=self.post_login)

    # 通过模拟表单自动登录
    def start_requests(self):
        loginUrl = "https://passport.jd.com/common/loginPage?from=media&ReturnUrl=http://media.jd.com/index/overview"
        return [Request(loginUrl,meta={'cookiejar' : 1}, callback = self.post_login)]

    #模拟自动登录
    def post_login(self,response):
        print('post_login')
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
                'loginname': '18602507935',
                'nloginpwd': 'aa11ss33',
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
               'loginname': '18602507935',
               'nloginpwd': 'aa11ss33',
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




    def after_login(self, response):
        body = response.body.decode(response.encoding)
        if 'success' in body:
            lines = ["苹果手机", "三星手机"]
            for line in lines:
                http_url = "https://search.jd.com/Search?keyword=" + line + "&enc=utf-8"
            print("亲,恭喜您已经成功登录到京东联盟！")
            yield scrapy.Request(url=http_url, meta={'cookiejar': response.meta['cookiejar']}, callback=self.parse_link)
        else:
            print('body', body)
            print("抱歉,登录失败,请重新登录!")

    def parse_link(self, response):
        sel = Selector(response)
        pagestr = sel.response.xpath('//*[@id="J_topPage"]/span/i/text()').extract()
        page = int(pagestr[0])
        # print('url_link', response.url)
        if (page >= 2):
            if (page >= 15):
                num = 15
            else:
                num = page
            i = 1
            while i <= 2:
                reqlink = response.url + "&page=" + str(i)
                i += 1
                yield scrapy.Request(reqlink, callback=self.parse_id)

    def parse_id(self, response):
        sel = Selector(response)
        ids = sel.response.xpath('//*[@id="J_goodsList"]/ul/li/@data-sku').extract()
        for id in ids:
            #print('id', id)
            param ={}
            param['keyword'] =id
            data = urllib.parse.urlencode(param)
            pageUrl = self.httpurl + "?" + data
            yield scrapy.Request(pageUrl, meta={'cookiejar': 1, 'id': id}, callback=self.parse_item)





    #获取验证码 人工输入/自动处理
    def getVeryicationCode(image_url):
        filename =  datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        codeimg = DwlImage(image_url,filename)
        code = CodeIdentHttp.identifyCodeResult(codeimg,'3004')
        return code



    #解析具体的ITEM
    def parse_item(self, response):
        # dir_name =response.meta['dir_name']
        # dir_path = response.meta['dir_path']
        dir_name =""
        dir_path =""
        print('status', response.status)
        body = response.body.decode(response.encoding)
        # print("body", body)
        if '请登录' in body or '请使用京东商城账号登录' in body:
            print("对不起cookie已经失效,请重新登录系统!")
        elif '400 Bad Request' in body:
            print("对不起爬虫请求被京东反爬虫系统屏蔽了")
            print('keyword', dir_path)
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
                    #print(spu_id, price)
                    # 商品最终价格
                    jdItem['final_price'] = float(price.replace('￥', '').replace(',', ''))
                    # jdItem
                    jdItem['rebate_id'] = 0
                    # 推广佣金比
                    jdItem['promotion_rate'] = int(float(money_ratio.replace('%', '')) * 100)
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
                    jdItem['operator_source'] = "xushaobin"
                    jdItem['start_date'] = start_date
                    jdItem['end_date'] = end_date
                    jdItem['dir_name'] = dir_name
                    jdItem['dir_path'] = dir_path
                    falg = self.isSave(end_date,order_num)
                    variable = self.isVariable(dir_name,title)
                    if(falg==True):
                        print('保存数据',title,dir_name,dir_path)
                        yield jdItem
                    else:
                        print('不满足保存条件',real_stuff_id,end_date,order_num)
            else:
                print('本次没有查询到任何数据,请重新查询数据!,正准备重新查询数据...')
                time.sleep(random.randint(1, 3))

    #计算当前记录是否要持久化到数据库
    @staticmethod
    def isSave(end_date,order_num):
        #计算是否是有效推广
        #计算销量是否满足
        end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d')
        now_date = datetime.datetime.strptime("2017-07-31", '%Y-%m-%d')
        day = (end_date - now_date).days
        if(day>0 and int(order_num)>30):
            return True
        else:
            return False

    #判断搜索的记录是否匹配对应的关键字
    @staticmethod
    def isVariable(word,name):
        seg_list = jieba.cut(word, cut_all=False)
        str = ": ".join(seg_list)
        strs = str.split(":")
        falg = []
        for s in strs:
            falg.append(s.strip() in name)
        if (False in falg):
           return False
        else:
           return True
