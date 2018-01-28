#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib.request as req
from urllib import error
import urllib
import json
class PhoneMessage():
     def sendPhoneMsg(phonefile,msg):
        phonelist =[]
        for phone in open(phonefile):
            phonelist.append(phone.strip())
        print("phones",phonelist)
        params={}
        for i in range(0, len(phonelist)):
            request_url = 'http://dw.qbao.com/send_massage/custom_info.do'
            params['phoneNumber']=phonelist[i]
            params['sendInfo']=msg
            param=urllib.parse.urlencode(params)
            reqs = req.Request(request_url+"?"+param)
            try:
                resp = req.urlopen(reqs)
                result = resp.read()
                js = json.loads(result.decode("utf-8"))
                falg = js["success"]
                print("falg",falg)
                if(falg==True):
                    print("手机短消息发送成功")
                else:
                    print("手机短消息发送失败")
            except error.HTTPError as e:
                print(e.code())
                print(e.read().decode('utf-8'))
if __name__ == "__main__":
    PhoneMessage.sendPhoneMsg("E:/pycharm/crawler/taobao_spider/taobao_spider/spiders/phone.txt","有好货最厉害!")