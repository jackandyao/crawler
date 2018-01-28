# this is use python script!
# -*- coding: UTF-8 -*-
import requests
from aisr_crawler.middleware.cookie.cookiejar import CookieJar as cj
import json
import pymysql
class JDOrderUtil:
    #ck ='ipLoc-djd=1-72-4137-0; areaId=1; user-key=03f71ca8-a994-4305-9ebb-b5ec13f4e029; cn=0; unpl=V2_YDNtbUcEFkd3X09Vc0kPBmIAGwgRAhRFIQtHUHJJCFEzAUdbclRCFXMUR1NnGVUUZwUZWEVcQR1FCHZXfBpaAmEBFl5yBBNNIEwEACtaDlwJAxJYQVFAFnAIQlFLKV8FVwMTbUJSSxJyDUZRfBtaB28DEllFX0sTcwhOZEsebDVXBxNUSl5BJXQ4R2Q5TQADbwIbWEEaQxB9D0FRexxbB2EBGl1CU0QdfQ5AVHMpXTVk; __jdv=122270672|baidu-search|t_262767352_baidusearch|cpc|11427224154_0_4bdc3f809ab2428dbdfae2058aeee3d7|1497779244244; ssid="2wY/t3HBQSim7GaEJOrC7A=="; 3AB9D23F7A4B3C9B=PD7QC76TTQHMQ5PHP2FDISPSDZVAUTSP4I447EYS3EUY4RRLGWHSUFLVQJ4Y2NJJQ2SHNFL2QXM5276R64SJQLVDEM; TrackID=1dO3pVy-MxXWuFzS5Tih-aXeoORG5O9EBHvCTdRY2Q9V1QXPMwXuhaDQThg8oP_bIDqnSVMCwE7rrCY6RZnq2XV--BAF83Dt4dq26NSp9Rxo; pinId=t8rv_49NTAXiId-dUhO1MA; _tp=%2B2IO5ajDcIBy09A8jW%2BKjA%3D%3D; logining=1; _pst=youhaohuo888; ceshi3.com=000; thor=1D5CF117EB45F941F6331DA371BB3CF1598DAE810CA126E6D920EC11441238504AEE0F70DA065BB3F96D67B6AE173386F68C265FFA220C2ED20DC8593127AEEFF81F9AC162F70B1B7958888846364908A037884F9EBF501C2DB371B5D398101A783756D921592C5F32E93DF2BE219A03E55D82B6183BBDAE7A4606C0262CD7EB6E0341D4130562478E311EAA8B85694B; pin=youhaohuo888; unick=youhaohuo888; showNoticeWindow=false; __jda=108460702.14966414637391156997719.1496641464.1498310307.1498456125.74; __jdc=108460702; __jdu=14966414637391156997719'
    #ck = 'ipLoc-djd=1-72-4137-0; areaId=1; user-key=03f71ca8-a994-4305-9ebb-b5ec13f4e029; cn=0; unpl=V2_YDNtbUcEFkd3X09Vc0kPBmIAGwgRAhRFIQtHUHJJCFEzAUdbclRCFXMUR1NnGVUUZwUZWEVcQR1FCHZXfBpaAmEBFl5yBBNNIEwEACtaDlwJAxJYQVFAFnAIQlFLKV8FVwMTbUJSSxJyDUZRfBtaB28DEllFX0sTcwhOZEsebDVXBxNUSl5BJXQ4R2Q5TQADbwIbWEEaQxB9D0FRexxbB2EBGl1CU0QdfQ5AVHMpXTVk; __jdv=122270672|baidu-search|t_262767352_baidusearch|cpc|11427224154_0_4bdc3f809ab2428dbdfae2058aeee3d7|1497779244244; ssid="2wY/t3HBQSim7GaEJOrC7A=="; showNoticeWindow=false; 3AB9D23F7A4B3C9B=PD7QC76TTQHMQ5PHP2FDISPSDZVAUTSP4I447EYS3EUY4RRLGWHSUFLVQJ4Y2NJJQ2SHNFL2QXM5276R64SJQLVDEM; TrackID=1MByzrsDtNbvDjvU9ZYGWhYsvR-Z1a8gYOKm12mSgCFot54s5CY0OPb2NNovJOmfaL_iGHh4rEhEQqYn9Go_gjqBGTr2zJJPEuPNJn2e55P4; pinId=t8rv_49NTAXiId-dUhO1MA; _tp=%2B2IO5ajDcIBy09A8jW%2BKjA%3D%3D; logining=1; _pst=youhaohuo888; ceshi3.com=000; thor=8E8D9FD75DC860C7B48950236EA53E492550BEAE37A9C35FE0F2C9610C9688952D6B298A3EDE603605B43B3E74E5AC17C9ED57C16BEBF9740300E8DBC0E502FDDD0E0368A223DA2670A12F56F307D3B465239284B604E2741DB4FDC4C118131F5697594F2E517AAD593085C608DEC5E422D5AB99B0E28B53F8762E05709C8741614662E6B8347A80A7C4FC2600859100; pin=youhaohuo888; unick=youhaohuo888; __jda=108460702.14966414637391156997719.1496641464.1498462914.1498524993.76; __jdb=108460702.7.14966414637391156997719|76.1498524993; __jdc=108460702; __jdu=14966414637391156997719'
    #ck ='ipLoc-djd=1-72-4137-0; areaId=1; user-key=03f71ca8-a994-4305-9ebb-b5ec13f4e029; cn=0; unpl=V2_YDNtbUcEFkd3X09Vc0kPBmIAGwgRAhRFIQtHUHJJCFEzAUdbclRCFXMUR1NnGVUUZwUZWEVcQR1FCHZXfBpaAmEBFl5yBBNNIEwEACtaDlwJAxJYQVFAFnAIQlFLKV8FVwMTbUJSSxJyDUZRfBtaB28DEllFX0sTcwhOZEsebDVXBxNUSl5BJXQ4R2Q5TQADbwIbWEEaQxB9D0FRexxbB2EBGl1CU0QdfQ5AVHMpXTVk; __jdv=122270672|baidu-search|t_262767352_baidusearch|cpc|11427224154_0_4bdc3f809ab2428dbdfae2058aeee3d7|1497779244244; ssid="2wY/t3HBQSim7GaEJOrC7A=="; showNoticeWindow=false; 3AB9D23F7A4B3C9B=PD7QC76TTQHMQ5PHP2FDISPSDZVAUTSP4I447EYS3EUY4RRLGWHSUFLVQJ4Y2NJJQ2SHNFL2QXM5276R64SJQLVDEM; TrackID=1RjajIzPQMY2va6kh9D0xiL4m03mgSayD2kf31h1tkSP8aoyqDt0sbPfDPrYh2dztg9PbQ6N89NOQ-Q4ZCJx6a47IUhIusQ3w3pVfhnwam-Y; pinId=t8rv_49NTAXiId-dUhO1MA; _tp=%2B2IO5ajDcIBy09A8jW%2BKjA%3D%3D; logining=1; _pst=youhaohuo888; ceshi3.com=000; thor=66343ECC407324D1C15760F0AF607D8421169662414AB04C09DEBA5BAD58D6AAA795C86BFB2D2515BE73E86CC1C9FD2514A593802BF310B1FD8B92974D62935FF1764588E96122C89F5178A99F059EBFB95BEBE55F131B43D3320AEA852CAA183A8B2E32839DB33F541475E2955A72CC8DC5F3C7E05EC073E677BB6DB2AC5D94C057996F70DB0E7C35A62F4DD02090D5; pin=youhaohuo888; unick=youhaohuo888; __jda=108460702.14966414637391156997719.1496641464.1498563499.1498613971.79; __jdb=108460702.5.14966414637391156997719|79.1498613971; __jdc=108460702; __jdu=14966414637391156997719'

    #ck ='ipLoc-djd=1-72-4137-0; areaId=1; user-key=03f71ca8-a994-4305-9ebb-b5ec13f4e029; cn=0; unpl=V2_YDNtbUcEFkd3X09Vc0kPBmIAGwgRAhRFIQtHUHJJCFEzAUdbclRCFXMUR1NnGVUUZwUZWEVcQR1FCHZXfBpaAmEBFl5yBBNNIEwEACtaDlwJAxJYQVFAFnAIQlFLKV8FVwMTbUJSSxJyDUZRfBtaB28DEllFX0sTcwhOZEsebDVXBxNUSl5BJXQ4R2Q5TQADbwIbWEEaQxB9D0FRexxbB2EBGl1CU0QdfQ5AVHMpXTVk; __jdv=122270672|baidu-search|t_262767352_baidusearch|cpc|11427224154_0_4bdc3f809ab2428dbdfae2058aeee3d7|1497779244244; ssid="2wY/t3HBQSim7GaEJOrC7A=="; showNoticeWindow=false; 3AB9D23F7A4B3C9B=PD7QC76TTQHMQ5PHP2FDISPSDZVAUTSP4I447EYS3EUY4RRLGWHSUFLVQJ4Y2NJJQ2SHNFL2QXM5276R64SJQLVDEM; TrackID=1RjajIzPQMY2va6kh9D0xiL4m03mgSayD2kf31h1tkSP8aoyqDt0sbPfDPrYh2dztg9PbQ6N89NOQ-Q4ZCJx6a47IUhIusQ3w3pVfhnwam-Y; pinId=t8rv_49NTAXiId-dUhO1MA; _tp=%2B2IO5ajDcIBy09A8jW%2BKjA%3D%3D; logining=1; _pst=youhaohuo888; ceshi3.com=000; thor=66343ECC407324D1C15760F0AF607D8421169662414AB04C09DEBA5BAD58D6AAA795C86BFB2D2515BE73E86CC1C9FD2514A593802BF310B1FD8B92974D62935FF1764588E96122C89F5178A99F059EBFB95BEBE55F131B43D3320AEA852CAA183A8B2E32839DB33F541475E2955A72CC8DC5F3C7E05EC073E677BB6DB2AC5D94C057996F70DB0E7C35A62F4DD02090D5; pin=youhaohuo888; unick=youhaohuo888; __jda=108460702.14966414637391156997719.1496641464.1498613971.1498618931.80; __jdc=108460702; __jdu=14966414637391156997719'
    ck = 'ipLoc-djd=1-72-4137-0; areaId=1; user-key=03f71ca8-a994-4305-9ebb-b5ec13f4e029; cn=0; unpl=V2_YDNtbUcEFkd3X09Vc0kPBmIAGwgRAhRFIQtHUHJJCFEzAUdbclRCFXMUR1NnGVUUZwUZWEVcQR1FCHZXfBpaAmEBFl5yBBNNIEwEACtaDlwJAxJYQVFAFnAIQlFLKV8FVwMTbUJSSxJyDUZRfBtaB28DEllFX0sTcwhOZEsebDVXBxNUSl5BJXQ4R2Q5TQADbwIbWEEaQxB9D0FRexxbB2EBGl1CU0QdfQ5AVHMpXTVk; __jdv=122270672|baidu-search|t_262767352_baidusearch|cpc|11427224154_0_4bdc3f809ab2428dbdfae2058aeee3d7|1497779244244; ssid="W6woLYyFRu6QOrSQ9ADqKQ=="; 3AB9D23F7A4B3C9B=PD7QC76TTQHMQ5PHP2FDISPSDZVAUTSP4I447EYS3EUY4RRLGWHSUFLVQJ4Y2NJJQ2SHNFL2QXM5276R64SJQLVDEM; TrackID=193gEaeG-4i6m-xaVLaStVkdcB36sS5Tie7JSlOX-zCiBg14p5lBnqPe6xNh17EV8yx_qnYEmGum578SwEZaDHTJjV2fnspvEnRwPz_cD0qs; pinId=t8rv_49NTAXiId-dUhO1MA; _tp=%2B2IO5ajDcIBy09A8jW%2BKjA%3D%3D; logining=1; _pst=youhaohuo888; ceshi3.com=000; thor=C6C46471370B244EDF4E3AECC6CC228E7CC66D08D3788BB9BED759A943519BE36C84A578AFCD4B45C181F1810513C1A7C06B42C484F9207224A09D9C294259C9BDC0FABBF7AB1A6ED124FB9EE834D98499818A3D724298112EB39AF658AB60E01198F0BAF619A3FDF8378F1C08FF25A4E7DEBF8BF57795BA084D13B4C9FE1097C9B399E548DEFFCCE3D43533D248B279; pin=youhaohuo888; unick=youhaohuo888; showNoticeWindow=false; __jda=108460702.14966414637391156997719.1496641464.1498643849.1498704538.82; __jdc=108460702; __jdu=14966414637391156997719'
    ck = 'ipLoc-djd=1-72-4137-0; areaId=1; user-key=03f71ca8-a994-4305-9ebb-b5ec13f4e029; cn=0; ssid="H39+U1niQCi292FRXE4tog=="; __jdv=95931165|direct|-|none|-|1499140247963; 3AB9D23F7A4B3C9B=PD7QC76TTQHMQ5PHP2FDISPSDZVAUTSP4I447EYS3EUY4RRLGWHSUFLVQJ4Y2NJJQ2SHNFL2QXM5276R64SJQLVDEM; TrackID=1ExRVCcTa8I4_461iaaRGLwWgNgX6_KLxjBNX1Emp4FcuPN4aH5DiusVOovwBUlsBX3KPF_Q47tQ1-lzleLQj0AjgCk0t0USaf6R2muE8Yyo; pinId=t8rv_49NTAXiId-dUhO1MA; _tp=%2B2IO5ajDcIBy09A8jW%2BKjA%3D%3D; logining=1; _pst=youhaohuo888; ceshi3.com=000; thor=7DAFFDFA789C49CCC1E1BF46827C02C38E3F1E04F26DBB8BACCC6F21D333114C32255EFDBA8440C528020BAAF077CC89812E25CA821959B7F8FA4ABCCE519EEA18852E08A23FAFB970095209A3D695421F606B93386ABB2CEE4860D98DD2747B5CCF39C3919241BFBD921345762527FDF0DC530F2C674C2A304AA3773C2F875F3DF6D60572DC5022617684E5400611EA; pin=youhaohuo888; unick=youhaohuo888; showNoticeWindow=false; __jda=108460702.14966414637391156997719.1496641464.1499154435.1499156643.91; __jdb=108460702.1.14966414637391156997719|91.1499156643; __jdc=108460702; __jdu=14966414637391156997719'
    cookies = cj.getCookie(ck)
    orderUrl = 'https://media.jd.com/rest/report/detail/final/page'
    downOrderUrl ='https://media.jd.com/rest/report/detail/final/export'

    headers = {
        "Content-Type": "application/json; charset=UTF-8"
    }

    startDate ="2017-06-17"
    endDate ="2017-06-24"

    #初始化数据库连接信息
    def __init__(self):
        self.db = pymysql.connect("192.168.14.107", "wangping", "sadas3432$#%ret@!", "qbao_stuff", charset="utf8")
        self.cursor =self.db.cursor()

    #下载订单
    def searchOrderIds(self):
        order_ids = open("../config/jd_order_id.txt")
        #遍历每个订单原始ID
        for orderId in order_ids:
           orderItemList = self.searchOrderInfo(orderId.strip())
           self.saveOrderInfo(orderItemList)
        self.db.close()

    #查询订单信息信息
    def searchOrderInfo(self,orderId):
        obj = self.getOrderInfo(orderId)
        datalist = obj['data']
        orderItemList = []
        # 遍历每个订单的详细产品信息
        for data in datalist:
            # print('data', data)
            # 遍历订单号
            parentid = data['parentId']
            if (int(parentid) == 0):
                print('未拆单', orderId)
                self.noChaiDan(data,parentid,orderItemList,'no')
            else:
                print('已拆单', orderId)
                #获取父订单ID
                falg =False
                while (falg==False):
                    res = self.getOrderParentId(parentid)
                    pid = parentid
                    parentid = res['parentid']
                    if(parentid==0):
                        falg =True
                        print('拆单结束',pid)
                        ds = res['data']
                        orderList=[]
                        print(ds)
                        for d in ds:
                            self.noChaiDan(data,pid,orderList,'yes')
                            self.saveOrderInfo(orderList)
        return orderItemList


    #解决未拆单
    def noChaiDan(self,data,parentid,orderItemList,falg):
        orderId = data['orderId']
        orderDate = data['orderDate']
        finishdate = data['finishDate']
        state =data['orderStatusName']
        skus = data['skus']
        for sku in skus:
            orderItem ={}
            skuId = sku["skuId"]
            if(falg=='no'):
                orderItem['parentId'] = orderId
            if(falg=='yes'):
                orderItem['parentId'] = parentid
            orderItem['orderId'] = orderId
            orderItem['orderDate'] = orderDate
            orderItem['skuId'] = skuId
            orderItem['balance'] = sku['balance']
            orderItem['balanceName'] = sku['balanceName']
            orderItem['rate'] = sku['commissionRate']
            orderItem['rateMoney'] = sku['commission']
            orderItem['skuPrice'] = sku['skuPrice']
            orderItem['finishDate'] = finishdate
            orderItem['skuNum'] = sku['skuNum']
            orderItem['skuName'] = sku['skuName']
            orderItem['orderStatusName']=state
            orderItemList.append(orderItem)

    #获取每个订单的父ID
    def getOrderParentId(self,parentid):
        res ={}
        obj = self.getOrderInfo(parentid)
        res['parentid'] = obj['data'][0]['parentId']
        res['data'] = obj['data']
        return res

    #查询订单信息
    def getOrderInfo(self,orderId):
        data = self.createSearchParam(self.startDate, self.endDate, orderId)
        result = requests.post(self.orderUrl, data=json.dumps(data), cookies=self.cookies, headers=self.headers)
        res = result.text
        if '请使用京东商城账号登录' in res or '你好，请登录' in res:
            print("你没有登录系统,请先登录")
        elif '400 Bad Request' in res:
            print("对不起爬虫请求被京东反爬虫系统屏蔽了")
            with open('../config/jd_turn_failed_id.txt', 'a') as f:
                f.write(id + '\n')
        else:
            #print(res)
            obj = json.loads(res)
            return obj

    #下载每日业绩订单
    def downLoadOrderXls(self):
        data = self.createSearchParam(self.startDate, self.endDate,'')
        resp = requests.post(self.downOrderUrl, data=json.dumps(data), cookies=self.cookies, headers=self.headers)
        with open("f.csv", 'wb') as f:
            for chunk in resp.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
                    f.flush()
        #print(resp.content)

    #保存订单数据到数据库中
    def saveOrderInfo(self,orderItemList):
           if (orderItemList!=None):
               for order in orderItemList:
                   # 遍历订单最终信息并保存到数据库
                   orderid = order['orderId']
                   parentid = order['parentId']
                   orderdate = order['orderDate']
                   finshdate =order['finishDate']
                   skuid = order['skuId']
                   balance = order['balance']
                   balancename = order['balanceName']
                   rate =int(order['rate'])*100
                   money =order['rateMoney']
                   price =order['skuPrice']
                   skunum=order['skuNum']
                   skuname =order['skuName']
                   state = order['orderStatusName']
                   print('skuname',skuname)
                   #print('price',price,'money',money,'rate',rate,'skunum',skunum)
                   sql = "INSERT INTO jd_order(orderid,parentid,orderdate,skuid,skuname,balance,balancename,finishdate,skuprice,skunum,commissionrate,commission,orderstate)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                   params = [orderid,parentid,orderdate,skuid,skuname,balance,balancename,finshdate,price,skunum,rate,money,state]
                   try:
                       # 执行sql语句
                       self.cursor.execute(sql,params)
                       # 提交到数据库执行
                       self.db.commit()
                       print('成功保存数据到数据库中')
                   except Exception as e:
                       # 如果发生错误则回滚
                       print('保存数据失败',e)
                       self.db.rollback()
                   # 关闭数据库连接
               #self.db.close()
           else:
               print('查询订单数据异常无任何数据返回!')

    #创建查询条件
    def createSearchParam(self,startDate,endDate,orderId):
        params= {
                 "pagination":{"total":0,"pageNum":1,"size":"20"},
                 "order":[],
                 "data":[],
                 "search":[
                     {"name":"orderId","value":orderId},
                     {"name":"accountDateStr","value":startDate+"#"+endDate},
                     {"name":"shortcutDate","value":""},
                     {"name":"orderStatus","value":""}]
                 }

        return params


if __name__ == '__main__':
    res = JDOrderUtil().searchOrderIds()
    #res = JDOrderUtil().downLoadOrderXls()