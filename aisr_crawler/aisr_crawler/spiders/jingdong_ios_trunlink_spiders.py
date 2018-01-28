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
from aisr_crawler.util.handlestr import HandleStr as hs
from aisr_crawler.util.jingdong import JDUtil as jd
import random
import urllib
import time
import re
from aisr_crawler.util.phone import PhoneMessage as pm
import os
import logging
import json
from aisr_crawler.item.crawelr_item import JDTurnLinkItem
#模拟京东登录并自动抓取商品
class JingDongTurnLinkSpider(CrawlSpider):

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

    httpurl = 'https://media.jd.com/gotoadv/getCustomCode/1'

    name = "jdIosTrunLinkSpider"

    type = "ios"
    idfile = 'jd_id_'+type+".txt"
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
         #print('req_cookie',req_cookie)
         resp_cookie = response.headers.getlist('Set-Cookie')
         body = response.body.decode(response.encoding)
         if 'success' in body:
             print("亲,恭喜您已经成功登录到京东联盟！")

             #抓取这类关键字:手机_手机配件_手机贴膜
             id_list = open("aisr_crawler/config/"+self.idfile)
             file = "aisr_crawler/config/link.txt"
             for id in id_list:
                 param = jd.createLinkParam(file, self.type, id)
                 data = urllib.parse.urlencode(param)
                 linkUrl = self.httpurl + "?" + data
                 print('linkurl',linkUrl)
                 # 去创建一个请求
                 yield scrapy.Request(url=linkUrl, meta={'cookiejar': response.meta['cookiejar']
                                                         ,'id':id},callback=self.parse_link)
                 #time.sleep(random.randint(1, 3))
         else:
             print("抱歉,登录失败,请重新登录!")



    #获取验证码 人工输入/自动处理
    def getVeryicationCode(image_url):
        filename =  datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        codeimg = DwlImage(image_url,filename)
        code = CodeIdentHttp.identifyCodeResult(codeimg,'3004')
        return code


    #先获取每个关键字能查询到的总页数
    def parse_link(self,response):
        jdTurnLinkItem =JDTurnLinkItem()
        id = response.meta['id']
        res = response.body.decode(response.encoding)
        #print('res',res)
        if '请使用京东商城账号登录' in res or '你好，请登录' in res:
            print("转链接返回信息:你没有登录系统,请先登录")
        elif '400 Bad Request' in res:
            print("转链接返回信息:对不起爬虫请求被京东反爬虫系统屏蔽了")
            with open('aisr_crawler/config/jd_turn_failed_id.txt', 'a') as f:
                f.write(id + '\n')
            time.sleep(random.randint(1,3))
            yield scrapy.Request(url=response.url, meta={'cookiejar': response.meta['cookiejar']
                , 'id': id}, callback=self.parse_link)
        else:
            p_res = json.loads(res)
            falg = p_res['success']
            # print('post', p_res)
            if (falg == True):
                if 'urlAdvCode' in p_res:
                    urlAdvCode = str(p_res['urlAdvCode'])
                    print('code',urlAdvCode)
                    jdTurnLinkItem['id'] = id
                    jdTurnLinkItem['ios_link'] = urlAdvCode
                    print(id,urlAdvCode)
                    # yield jdTurnLinkItem

            else:
                with open('aisr_crawler/config/jd_nobuy_id.txt', 'a') as f:
                    f.write(id + '\n')



