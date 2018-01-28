# this is use python script!
# -*- coding: UTF-8 -*-
import urllib.request as req
import json
from urllib import error
import re
from spiders.dict import DictMapUtil as dmu
#封装请求淘宝相关的功能,获取到要抓取商品的总页数
class TaoBaoUtil():

    # 获取当前要抓取结果的总页数
    def getTaoBaoPageByKeyword(type,keyWord,file):
        page_result={}
        # shopTag = yxjh
        # 这个参数不带 返回的商品会少很多
        httpUrl = dmu.getHttpUrlByType(type)
        data = dmu.createTaoBaoHttpParam(type,keyWord,file)
        reqs = req.Request(httpUrl + "?" + data)
        print("page_url",httpUrl + "?" + data)
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
            else:
                # 被拦截
                print("result_deconde", dres)
                obj = json.loads(dres)
                sumpage = obj['data']['paginator']['pages']
                page = sumpage
                if (page >= 1000):
                    page = 500
                elif (page >= 2000):
                    page = 600
                elif (page > 3000):
                    page = 700
                else:
                    page = page
                print("查询页数是:" + str(sumpage))
                page_result['sumpage']=page
                page_result['success'] = "true"
            return page_result
        except error.HTTPError as e:
            print(e.code())
            print(e.read().decode('utf-8'))




    #读取抓取文件类目
    def getKeyWord(file):
        keyword_list=[]
        f = open(file, "r",encoding='UTF-8')
        lines = f.readlines()  # 读取全部内容
        for line in lines:
            keywords = line.split("  ")
            for key in keywords:
                keyword_list.append(key.strip())
        return keyword_list;

    #匹配中文
    def patternHanZi(str):
        phanzi = re.compile(u'[\u4e00-\u9fa5]');
        res=phanzi.findall(str)
        a=""
        for r in res:
            a+=r
        return a


if __name__ == "__main__":
#     print(getCatId("女装"))
    #res=TaoBaoUtil.getTaoBaoPageByKeyword("all","内衣")
    res=TaoBaoUtil.getKeyWord("keyword.txt");
    print(res)