# this is use python script!
# -*- coding: UTF-8 -*-
import redis
from aisr_crawler.util.taobao import TaoBaoUtil as tu
from aisr_crawler.util.handlestr import HandleStr as hs
from aisr_crawler.util.dict import DictMapUtil as dmu
from aisr_crawler.util.filerw import FileHandle as fh
import urllib
import json
import time
import random

#把淘宝待抓取的关键字转换对应的URL 存放到队列中 https://yq.aliyun.com/ziliao/102415 反爬虫
class TBUrlPush:

    #推送url到redis中
    def pushuTBUrl(self,key_file,param_file,type):
        r = redis.Redis(host='192.168.14.245', port=6379)
        ks = fh.getTBKeyWordJson(key_file)
        for k in ks:
            keyword = k['key']
            catname = k['catName']
            page_result = tu.getTaoBaoPageByKeyword(type, keyword, param_file)
            #print('page_reuslt', page_result)
            falg = page_result['success']
            fullurl =''
            if (falg == 'true'):
                sumpage = page_result['sumpage']
                #print('实际返回页数是:' + str(sumpage) + ",key:" + keyword)
                httpUrl = dmu.getHttpUrlByType(type)
                data = dmu.createTaoBaoHttpParam(type, keyword, param_file)
                fullurl = httpUrl + "?" + data;
                page = 1;
                while page <= sumpage:
                    reqUrl = fullurl + "&" + "toPage=" + str(page)
                    print(keyword,sumpage,reqUrl)
                    r.lpush('tabaoSpider:start_urls', reqUrl)
                    page+=1
                time.sleep(random.randint(1,3))
            else:
                print("对不起根据关键字:"+keyword+",没有查询到结果!")
                httpUrl = dmu.getHttpUrlByType(type)
                data = dmu.createTaoBaoHttpParam(type, keyword, param_file)
                fullurl = httpUrl + "?" + data;
                with open('../config/tb_nourl.txt', 'a',encoding="utf-8") as f:
                     f.write(catname +":" +fullurl+ '\n')
                #等待几分钟重新爬取阿里妈妈关键字

if __name__ == '__main__':
     key_file ='../config/tb_keyword.txt'
     param_file ='../config/taobao_param.txt'
     type = 'all'
     tb = TBUrlPush().pushuTBUrl(key_file,param_file,type)
     print('推送关键字完毕!')