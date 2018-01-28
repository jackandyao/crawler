# this is use python script!
# -*- coding: UTF-8 -*-
from scrapy.spiders import CrawlSpider
import scrapy,json,time,sys
from component.item.stuff_item import StuffItem
from component.util.param_util import ConditionFactory as cf
from scrapy.conf import settings
import logging
from component.util.system_util import SystemUtil as syst
#淘宝商品抓取爬虫
class  TaobaoSpider(CrawlSpider):
    logging.basicConfig(level=logging.WARNING,format='%(message)s',filename='taobao.log',filemode='w')
    # logging.basicConfig(level=logging.INFO, format='%(message)s')


    plat_form = syst().getPlatform()
    if (plat_form =="linux"):
        dir_name = sys.argv[0]
    else:
        dir_name  =settings['SEARCH_DIR_KW']
    name = "taobao"

    #重写获取URL的方法
    def start_requests(self):
        taobaoInstance = cf().getCondtionInstance("TB")()
        keywords = taobaoInstance.getSearchKeyWordList(self.dir_name,settings['STUFF_DIR_PATH'])
        for key in keywords:
            obj = taobaoInstance.initSearchCondtion(key)
            search_url = obj['search_url']
            cat_name = obj['cat_name']
            cat_path = obj['cat_path']
            real_page = obj['real_page']

            yield scrapy.Request(url=search_url, meta={'cat_path': cat_path, 'cat_name': cat_name,'real_page':real_page,'dir_key':key})

    #获取满足条件的真实页数
    def __getRealPage(self,real_page,sumpage,key):
        #查询条件配置文件为空 说明不需要区分每个关键字具体要抓取多少页 有统一标准
        # print('__getRealPage',real_page,sumpage)
        if ("&" not in key):
            return self.__splitRealPage(sumpage)
        else:
            if (int(real_page) > 0):
                return real_page
            if (int(real_page < 0)):
                return sumpage

    #对于单个关键字最多获取600个商品
    def __splitRealPage(self,sumpage):
        max_page = int(settings['SEARCH_MAX_PAGE'])
        # print('__splitRealPage',sumpage)
        if (sumpage >max_page):
            sum_page = max_page
        else:
            sum_page= sumpage
        # print('return page info',sumpage,sum_page)
        return sum_page

    #把每个关键字的总页数 转化成对应的url,比如总页数Wie50 就模拟分页请求50次
    def parse(self, response):
        url = response.url
        #print('parse_search_url',url)
        body = response.body.decode(response.encoding)
        if "亲，访问受限了" in body:
            print('你被阿里妈妈反爬虫拦截了!')
            self.writeFailUrlToText(url)

        else:
            page_url = response.url
            cat_name = response.meta['cat_name']
            cat_path = response.meta['cat_path']
            real_page = response.meta['real_page']
            obj = json.loads(response.body_as_unicode())
            data = obj['data']
        if 'paginator' in data:
            paginator = data['paginator']
            if (paginator != None):
                if 'pages' in paginator:
                    pages = paginator['pages']
                    print('pages from taobao',pages)

                    sumpage = self.__getRealPage(real_page,pages,response.meta['dir_key'])
                    print('sumapge',cat_name,int(sumpage))
                    logging.warning('sumpage'+":"+cat_name+":"+cat_path+":"+str(sumpage))
                    page = 1
                    pages =int(sumpage)
                    while page <= pages:
                        full_page_url = page_url + "&" + "toPage=" + str(page)
                        page += 1
                        yield scrapy.Request(url=full_page_url, meta={'cat_path': cat_path, 'cat_name': cat_name},callback=self.parse_stuff_item)
                else:
                    print('对不起根据您输入的关键字没有检索到任何结果!')

            else:
                print('对不起根据您输入的关键字没有检索到任何结果!')
        else:
            print('对不起根据您输入的关键字没有检索到任何结果!')


    #把抓取失败的关键字或者失败的URL写入到txt中...
    def writeFailUrlToText(self,url):
        fail_url_file = settings['STUFF_FAIL_URL']
        with open(fail_url_file, 'a') as f:
            f.write(url + '\n')

    #解析抓取到的每一页数据
    def parse_stuff_item(self, response):
        #print('page_url',response.url)
        cat_name = response.meta['cat_name']
        cat_path = response.meta['cat_path']
        jsonobject = json.loads(response.body_as_unicode())
        objlist = jsonobject['data']['pageList']
        if (objlist ==None):
            print('对不起没有可以解析的产品数据,请核实查询条件',response.url)

        else:
            for obj in objlist:
                taoBaoItem = StuffItem();
                stuff_id = obj['auctionId']
                # 实际商品id
                taoBaoItem['stuff_real_id'] = stuff_id
                # 商品名称
                taoBaoItem['stuff_name'] = obj['title']
                # 原价
                taoBaoItem['stuff_reserve_price'] = obj['reservePrice']
                # 商品最终价格
                taoBaoItem['stuff_final_price'] = obj['zkPrice']
                # 返利类型rebate表id
                taoBaoItem['stuff_rebate_id'] = 0
                # 推广佣金比
                taoBaoItem['stuff_promotion_rate'] = str(obj['tkRate'])
                # android推广链接
                taoBaoItem['stuff_android_promotion_url'] = "#"
                # ios推广链接
                taoBaoItem['stuff_ios_promotion_url'] = "#"
                # 商品链接
                taoBaoItem['stuff_url'] = obj['auctionUrl']
                # 商品图片链接
                taoBaoItem['stuff_img_url'] = obj['pictUrl']

                # 商品类目cat_id
                taoBaoItem['stuff_cat_id'] = ''
                # 类目名称
                taoBaoItem['stuff_cat_name'] = cat_name
                # 类目路径
                taoBaoItem['stuff_cat_path'] = cat_path
                # 商品状态
                taoBaoItem['stuff_status'] = 0
                # 商品来源
                use_type = obj['userType']
                source = self.getSourceName(use_type)
                taoBaoItem['stuff_source'] = source

                # 加上平台之后的商品ID
                id = str(stuff_id) + str(self.getSourceCode(source))
                taoBaoItem['stuff_id'] = id
                # 推广销量
                taoBaoItem['stuff_order_num'] = obj['biz30day']
                # 创建时间
                taoBaoItem['stuff_create_time'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                # 更新时间
                taoBaoItem['stuff_update_time'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                # 当前转链接使用的阿里妈妈账号名称
                taoBaoItem['stuff_operator_name'] = "#"
                taoBaoItem['stuff_two_one_promotion_url'] = "#"
                #商品推广的开始日期
                taoBaoItem['stuff_start_date'] =""
                #商品推广的结束日期
                taoBaoItem['stuff_end_date'] =""
                #print(cat_name, obj['title'])
                yield taoBaoItem


    # 根据变换转换对应的商品来源
    @staticmethod
    def getSourceName(user_type):
        if user_type == 0:
            return "taobao";
        elif user_type == 1:
            return "tmall";
        return "null";

    # 根据商品来源转换对应的商品来源编码
    @staticmethod
    def getSourceCode(sourceName):
        if sourceName == "taobao":
            return 111;
        elif sourceName == "tmall":
            return 222;
        else:
            return 333;

    # 获取商品目录ID
    @staticmethod
    def getCategoryId(file):
        return;