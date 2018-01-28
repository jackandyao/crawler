# this is use python script!
# -*- coding: UTF-8 -*-
# 转链接功能
import requests
from aisr_crawler.middleware.cookie.cookiejar import CookieJar as cj
from aisr_crawler.util.jingdong import JDUtil as jd
#from aisr_crawler.util.jdmongo import JDMongodUtil as jmu
from aisr_crawler.util.jd_mong import JDLinkMongodUtil as jmu
import json
import datetime
import sys
import platform
#执行转链接功能
class TurnLinkUtil():
    ck = 'ipLoc-djd=1-72-4137-0; areaId=1; user-key=03f71ca8-a994-4305-9ebb-b5ec13f4e029; cn=0; unpl=V2_YDNtbUcEFkd3X09Vc0kPBmIAGwgRAhRFIQtHUHJJCFEzAUdbclRCFXMUR1NnGVUUZwUZWEVcQR1FCHZXfBpaAmEBFl5yBBNNIEwEACtaDlwJAxJYQVFAFnAIQlFLKV8FVwMTbUJSSxJyDUZRfBtaB28DEllFX0sTcwhOZEsebDVXBxNUSl5BJXQ4R2Q5TQADbwIbWEEaQxB9D0FRexxbB2EBGl1CU0QdfQ5AVHMpXTVk; __jdv=122270672|baidu-search|t_262767352_baidusearch|cpc|11427224154_0_4bdc3f809ab2428dbdfae2058aeee3d7|1497779244244; ssid="w+BJvPCrR1Kq/rkzrpGT9Q=="; 3AB9D23F7A4B3C9B=PD7QC76TTQHMQ5PHP2FDISPSDZVAUTSP4I447EYS3EUY4RRLGWHSUFLVQJ4Y2NJJQ2SHNFL2QXM5276R64SJQLVDEM; TrackID=1O-qlunPoEY7b8MV-uAOjy0BP7A_kGB237txS3ERH78GG5bz2K1S0xM2ZaFUHUFZxM6CR4SLrsEAIjSEfteI0avRaqrECpU8MZVP-HwepaK8; pinId=t8rv_49NTAXiId-dUhO1MA; _tp=%2B2IO5ajDcIBy09A8jW%2BKjA%3D%3D; logining=1; _pst=youhaohuo888; ceshi3.com=000; thor=43CC34A5C16EEB2C8BA2AB2780FA442B039D8A59E22E658488EA21627C7226490EF5415045603737C06E55CEB8FDA8C84997DF5ADB091DAC5FC3BF3B00361798EFE9B2357F6A34B9EC7302528DCFE6A05BE25C67592E1237DBEBDC07D0078A672A5C5BE123A2C5AB090BC435DBB81E8C4239DA4C0073E4F7A6E43CE408885AFA6B237D4E8B1360833815F9920891BE47; pin=youhaohuo888; unick=youhaohuo888; __jda=108460702.14966414637391156997719.1496641464.1498791214.1498987447.85; __jdb=108460702.4.14966414637391156997719|85.1498987447; __jdc=108460702; showNoticeWindow=false; __jdu=14966414637391156997719'
    cookies = cj.getCookie(ck)
    #执行转链接功能
    def jdTurnLink(self,type):
        file = "../config/link.txt"
        jd_ids = open("../config/jd_id_android.txt")
        for id in jd_ids:
            data = jd.createLinkParam(file, type, id)
            post = requests.post("https://media.jd.com/gotoadv/getCustomCode/1", data=data, cookies=self.cookies)
            res = post.text
            if '请使用京东商城账号登录' in res or '你好，请登录' in res:
                print("你没有登录系统,请先登录")
            elif '400 Bad Request' in res:
                print("对不起爬虫请求被京东反爬虫系统屏蔽了")
                with open('../config/jd_turn_failed_id.txt', 'a') as f:
                   f.write(id + '\n')
            else:
                p_res = json.loads(post.text)
                falg = p_res['success']
                print('post',p_res)
                if (falg == True):
                    if 'urlAdvCode' in p_res:
                        urlAdvCode = str(p_res['urlAdvCode'])
                        jmu().updateLinkById(id.strip(), type, urlAdvCode)
                        print("success_id:", id.strip())
                else:
                    #print('商品不在推广中')
                    with open('../config/jd_nobuy_id.txt', 'a') as f:
                        f.write(id + '\n')
if __name__ == '__main__':
    startTime = datetime.datetime.now()
    tl = TurnLinkUtil().jdTurnLink("android")
    endTime = datetime.datetime.now()
    hour=str((endTime - startTime).seconds)
    print("Andorid转链接完毕，耗时时间:",hour)