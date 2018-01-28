# this is use python script!
# -*- coding: UTF-8 -*-
from scrapy.spiders import CrawlSpider
import scrapy,json,time,sys,datetime
from component.item.stuff_item import StuffItem
from scrapy.conf import settings
from component.util.system_util import SystemUtil as syst
import urllib,jieba,random
from scrapy.selector import Selector

#通过京东联盟抓取京东的商品
class JdStuffSpider(CrawlSpider):

    plat_form = syst().getPlatform()
    if (plat_form == "linux"):
        dir_name = sys.argv[0]
    else:
        dir_name = settings['SEARCH_DIR_KW']

    name = "jdstuff"

    httpurl = 'https://media.jd.com/gotoadv/goods'

    username = settings['JD_USER_NAME']
    password = settings['JD_PASS_WORD']
    # 请求header
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



    # 通过模拟表单自动登录
    def start_requests(self):
        loginUrl = "https://passport.jd.com/common/loginPage?from=media&ReturnUrl=http://media.jd.com/index/overview"
        return [scrapy.Request(loginUrl, meta={'cookiejar': 1}, callback=self.post_login)]

    # 模拟自动登录
    def post_login(self, response):
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
            # 自动识别验证码
            authcode = self.getVeryicationCode(verification)
            param = {
                'loginname': self.username,
                'nloginpwd': self.password,
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
            param = {
                'loginname': self.username,
                'nloginpwd': self.password,
                'pubKey': pubkey,
                'sa_token': sa_token,
                'uuid': uuid,
                'eid': eid,
                '_t': token,
                'from': 'media',
                'nr': '1'
            }
        print('正在登录系统中......')
        # RormRequest基于表单请求
        yield scrapy.FormRequest.from_response(response,
                                               url='https://passport.jd.com/uc/loginService',
                                               formdata=param,
                                               headers=self.post_headers,
                                               meta={'cookiejar': response.meta['cookiejar']},
                                               callback=self.after_login,
                                               dont_filter=True
                                               )
    # 登录成功之后再请求要抓取的URL
    def after_login(self, response):
        body = response.body.decode(response.encoding)
        if 'success' in body:
            print("亲,恭喜您已经成功登录到京东联盟！")
            jd_id_file = settings['JD_ID_PATH'] +"/" + self.dir_name+".txt"
            f = open(jd_id_file, "r", encoding='UTF-8')
            lines = f.readlines()  # 读取全部内容
            for line in lines:
                ls = line.split(":")
                pageUrl = self.httpurl + "?" + ls[2]
                yield scrapy.Request(url=pageUrl, meta={'cookiejar': response.meta['cookiejar'], 'cat_name': ls[1],
                                                        'cat_path': ls[0],'spu_id':ls[2]}, callback=self.parse_item)
        else:
            print("抱歉,登录失败,请重新登录!")

    # 获取验证码 人工输入/自动处理
    def getVeryicationCode(self,image_url):
       return

    def parse_item(self, response):
       cat_name = response.meta['cat_name']
       cat_path = response.meta['cat_path']
       spu_id = response.meta['spu_id']
       print('status', response.status)
       body = response.body.decode(response.encoding)
       # print("body", body)
       if '请登录' in body or '请使用京东商城账号登录' in body:
           print("对不起cookie已经失效,请重新登录系统!")
       elif '400 Bad Request' in body:
           print("对不起爬虫请求被京东反爬虫系统屏蔽了")
           print('keyword', cat_name)
       else:
           selector = Selector(response)
           first_id = selector.xpath('//*[@id="goodsQueryForm"]/div[2]/div/div/div/div[2]/ul/li/@skuid').extract()
           if len(first_id) > 0:
               print('已经成功获取到数据,准备解析数据...')
               li_list = selector.xpath('//*[@id="goodsQueryForm"]/div[2]/div/div/div/div[2]/ul/li')
               for sel in li_list:
                   spu_id = sel.xpath('./@skuid').extract()[0]
                   real_stuff_id = spu_id + "333"
                   url = sel.xpath('./div/div[1]/a/@href').extract()[0]
                   img_url = sel.xpath('./div/div[1]/a/img/@src').extract()[0]
                   title = sel.xpath('./div/div[2]/a/text()').extract()[0]
                   price = sel.xpath('./div/div[2]/div[1]/span[2]/span/text()').extract()[0].strip()
                   money_ratio = sel.xpath("./div/div[2]/div[2]/div[2]/em/text()").extract()[0]
                   order_num = sel.xpath("./div/div[2]/div[2]/div[5]/em/text()").extract()[0]
                   start_date = sel.xpath('./div[2]/a/@data-startdate').extract()[0]
                   end_date = sel.xpath('./div[2]/a/@data-enddate').extract()[0]
                   # 封装item
                   jdItem = StuffItem()
                   # 实际商品id
                   jdItem['stuff_real_id'] = spu_id
                   # 商品名称
                   jdItem['stuff_name'] = title
                   # 原价
                   jdItem['stuff_reserve_price'] =price
                   # 商品最终价格
                   jdItem['stuff_final_price'] =price
                   # 返利类型rebate表id
                   jdItem['stuff_rebate_id'] = 0
                   # 推广佣金比
                   jdItem['stuff_url'] =url
                   # 商品图片链接
                   jdItem['stuff_img_url'] = img_url
                   # 商品类目cat_id
                   jdItem['stuff_cat_id'] = ''
                   # 类目名称
                   jdItem['stuff_promotion_rate'] = str(money_ratio)
                   # android推广链接
                   jdItem['stuff_android_promotion_url'] = "#"
                   # ios推广链接
                   jdItem['stuff_ios_promotion_url'] = "#"
                   # 商品链接
                   jdItem['stuff_cat_name'] = cat_name
                   # 类目路径
                   jdItem['stuff_cat_path'] = cat_path
                   # 商品状态
                   jdItem['stuff_status'] = 0
                   # 商品来源
                   jdItem['stuff_source'] = "jd"
                   # 加上平台之后的商品ID
                   jdItem['stuff_id'] = real_stuff_id
                   # 推广销量
                   jdItem['stuff_order_num'] = order_num
                   # 创建时间
                   jdItem['stuff_create_time'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                   # 更新时间
                   jdItem['stuff_update_time'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                   # 当前转链接使用的阿里妈妈账号名称
                   jdItem['stuff_operator_name'] = "#"
                   jdItem['stuff_two_one_promotion_url'] = "#"
                   # 商品推广的开始日期
                   jdItem['stuff_start_date'] = start_date
                   # 商品推广的结束日期
                   jdItem['stuff_end_date'] = end_date
                   print('start_date',start_date,spu_id,title)
                   yield jdItem
           else:
               print('本次没有查询到任何数据,请重新查询数据!,正准备重新查询数据...',spu_id)




