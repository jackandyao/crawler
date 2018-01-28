# this is use python script!
# -*- coding: UTF-8 -*-
import urllib.request as req
import json
import urllib
import re
from aisr_crawler.util.dict import DictMapUtil as dmu
#封装请求淘宝相关的功能,获取到要抓取商品的总页数
class TaoBaoUtil():

    #获取淘宝转链接的参数
    def getTaoBaoTurnLink(id):
        param={}
        param['adzoneid']='76574177'
        param['siteid']='23098705'
        param['auctionid']=id
        return param;

    # 获取当前要抓取结果的总页数
    def getTaoBaoPageByKeyword(type,keyWord,file):
        iplist=[
            '114.239.1.3:808','111.72.244.116:808','110.83.46.234:808',
            '183.153.23.86:808','115.203.66.141:808','115.215.70.225:808'

        ]
        proxy_support = urllib.request.ProxyHandler({'http': random.choice(iplist)})
        opener = urllib.request.build_opener(proxy_support)
        opener.addheaders = [('User-Agent',
                              'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36')]
        urllib.request.install_opener(opener)
        page_result={}
        # shopTag = yxjh
        # 这个参数不带 返回的商品会少很多
        httpUrl = dmu.getHttpUrlByType(type)
        data = dmu.createTaoBaoHttpParam(type,keyWord,file)
        reqs = req.Request(httpUrl + "?" + data)
        reqs.add_header('User-Agent', 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)')
        #print("page_url",httpUrl + "?" + data)
        try:
            resp = req.urlopen(reqs)
            #无结果
            result = resp.read()
            dres = result.decode("utf-8")
            if "亲，访问受限了" in dres:
                print("被阿里妈妈反爬虫进行拦截了..")
                page_result['msg']='被阿里妈妈反爬虫进行拦截了'
                page_result['success']="false"
                page=0
                return page_result
            else:
                # 被拦截
                #print("result_deconde", dres)
                obj = json.loads(dres)
                #print('obj',obj)
                data =obj['data']
                if 'paginator' in data:
                    paginator= data['paginator']
                    #print('paginator',paginator)
                    #print(keyWord)
                    if (paginator != None):
                        if 'pages' in paginator:
                            sumpage=paginator['pages']
                            page = sumpage
                            if (page >=51):
                                page =50
                            else:
                                page = page
                            #print("查询页数是:" + str(sumpage))
                            page_result['sumpage']=page
                            page_result['success'] = "true"
                            return page_result
                        else:
                            #print(keyWord,"没有查询到结果!")
                            page_result['msg'] = '对不起根据您输入的关键字没有检索到任何结果'
                            page_result['success'] = "false"
                            page = 0
                            return page_result
                    else:
                        #print(keyWord, "没有查询到结果!")
                        page_result['msg'] = '对不起根据您输入的关键字没有检索到任何结果'
                        page_result['success'] = "false"
                        page = 0
                        return page_result
                else:
                    #print(keyWord, "没有查询到结果!")
                    page_result['msg'] = '对不起根据您输入的关键字没有检索到任何结果'
                    page_result['success'] = "false"
                    page = 0
                    return page_result
        except error.HTTPError as e:
            print(e.code())
            print(e.read().decode('utf-8'))
