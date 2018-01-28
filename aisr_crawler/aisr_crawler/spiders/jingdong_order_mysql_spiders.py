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
import sys,pymysql,requests
import random,urllib,time,re,os,logging,json
from aisr_crawler.util.phone import PhoneMessage as pm
#模拟京东登录并自动抓取商品
class JingDongSpider(CrawlSpider):

    #系统输入参数
    # startDate=sys.argv[0]
    # endDate=sys.argv[1]

    startDate = "2017-06-17"
    endDate = "2017-06-24"
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
    #请求URL
    orderUrl = 'https://media.jd.com/rest/report/detail/final/page'
    downOrderUrl = 'https://media.jd.com/rest/report/detail/final/export'

    name = "jdOrderSpider"

    # 创建查询条件
    def createSearchParam(self, startDate, endDate, orderId):
        params = {
            "pagination": {"total": 0, "pageNum": 1, "size": "20"},
            "order": [],
            "data": [],
            "search": [
                {"name": "orderId", "value": orderId},
                {"name": "accountDateStr", "value": startDate + "#" + endDate},
                {"name": "shortcutDate", "value": ""},
                {"name": "orderStatus", "value": ""}]}

        return params

    # 获取验证码 人工输入/自动处理
    def getVeryicationCode(image_url):
        filename = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        codeimg = DwlImage(image_url, filename)
        code = CodeIdentHttp.identifyCodeResult(codeimg, '3004')
        return code

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
                'loginname': 'youhaohuo888',
                'nloginpwd': 'Abc123456',
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
               'loginname': 'youhaohuo888',
               'nloginpwd': 'Abc123456',
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
             yield scrapy.Request(url=self.downOrderUrl, meta={'cookiejar': response.meta['cookiejar']},callback=self.downLoaderOrder)
         else:
             print("抱歉,登录失败,请重新登录!")

    #下载订单数据并保存为xls
    def downLoaderOrder(self,response):
        # data = self.createSearchParam(self.startDate, self.endDate, '')
        # resp = requests.post(self.downOrderUrl, data=json.dumps(data), cookies=self.cookies, headers=self.headers)
        #response
        xlsName = self.startDate+"_"+self.endDate+"_"+"京东业绩订单明细"+".csv"
        basePath ='aisr_crawler/config/xls/'+xlsName
        #resp = response.iter_content
        if os.path.exists(basePath):
            print('今天的业绩订单已经下载,请不要重复下载,谢谢')
            return
        else:
            print('准备下载今天业绩订单')
            print(response)
            with open(basePath, 'wb') as f:
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
                        f.flush()




