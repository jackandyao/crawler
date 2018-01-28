# this is use python script!
# -*- coding: UTF-8 -*-
# 转链接功能
import requests
from aisr_crawler.middleware.cookie.cookiejar import CookieJar as cj
from aisr_crawler.util.taobao import TaoBaoUtil as tb
import json,datetime,sys,platform
#执行转链接功能
class TurnLinkUtil():

    #ck ='ipLoc-djd=1-72-4137-0; areaId=1; unpl=V2_ZzNtbRVSShR8CRYBKR9ZUmIBQl5LUEsTIFgUVX8aCAcyUEJbclRCFXMUR1NnGFUUZwEZWUtcRxFFCEdkeR5VAWEzEm03VkERPFMaXX5BGUZlVEdeGQMdYkULRmRzKVwAbwQVWEJSRBdzCk5Uex1bDW8FFF1KZ3MSRTgdARUdDwE1B0ZUFlAQF3Zcdld4GFgGZAMWWHJWcxRFQyhVNhlZDWAEF11HUEETdwBGVH8eVA1hBRJVclZzFg%3d%3d; __jdv=122270672|fun.fanli.com|t_36857_1|tuiguang|f48080adc74f43a28697dac052e3dba7|1496901579456; ssid="G2z2/2AMTYqADKoKV/cQAA=="; 3AB9D23F7A4B3C9B=PD7QC76TTQHMQ5PHP2FDISPSDZVAUTSP4I447EYS3EUY4RRLGWHSUFLVQJ4Y2NJJQ2SHNFL2QXM5276R64SJQLVDEM; TrackID=16RJBOBXoUaqvAI6rvHGalysQeqVjBZ7pzGOFGyzSGmvBXlPCKbdVkewdP5DAsfJIKIu9VPwXBFnhUJDCyAplEp3-TlGyQafFgbo2H4ufxqM; pinId=t8rv_49NTAXiId-dUhO1MA; _tp=%2B2IO5ajDcIBy09A8jW%2BKjA%3D%3D; logining=1; _pst=youhaohuo888; ceshi3.com=000; thor=31E0EED2144BEF508A4C1549CEA1073B7E1C1E95824A6650C5DA0CB3BF5B9223023AD8CE7F92C809386ACA2E789BD0B9B7A6CD101DBC5177FEE1F328BAAF9C092B1DED9D9105E088EE30F1C287968B8F999B07E239B5EC98AC245DCEFAF7ED819E8E42DAB0C00865A83FEA7444F790468287FFF3BA8DC5B58A0B2A0D771E71592A873954FDB9ED85D0E1397B7497BD78; pin=youhaohuo888; unick=youhaohuo888; showNoticeWindow=false; __jda=108460702.14966414637391156997719.1496641464.1497268526.1497316212.31; __jdb=108460702.4.14966414637391156997719|31.1497316212; __jdc=108460702; __jdu=14966414637391156997719'
    #ck = 'ipLoc-djd=1-72-4137-0; areaId=1; unpl=V2_ZzNtbRVSShR8CRYBKR9ZUmIBQl5LUEsTIFgUVX8aCAcyUEJbclRCFXMUR1NnGFUUZwEZWUtcRxFFCEdkeR5VAWEzEm03VkERPFMaXX5BGUZlVEdeGQMdYkULRmRzKVwAbwQVWEJSRBdzCk5Uex1bDW8FFF1KZ3MSRTgdARUdDwE1B0ZUFlAQF3Zcdld4GFgGZAMWWHJWcxRFQyhVNhlZDWAEF11HUEETdwBGVH8eVA1hBRJVclZzFg%3d%3d; __jdv=122270672|fun.fanli.com|t_36857_1|tuiguang|f48080adc74f43a28697dac052e3dba7|1496901579456; ssid="G2z2/2AMTYqADKoKV/cQAA=="; showNoticeWindow=false; wlfstk_smdl=64mpy4j31u8w105rtyg1c5y1rqxqtjy0; _jrda=1; TrackID=1KH6B-CPAylxIdJX5Eyi_QteZeexjZN2KZMGVdjZqa57rMWsBHT2Jn50GE5URyR3t7iW5QFYWChH0xBQ0AwMy-1dZSwvJrNEVd7PkpPOqVXE; pinId=t8rv_49NTAXiId-dUhO1MA; _tp=%2B2IO5ajDcIBy09A8jW%2BKjA%3D%3D; _pst=youhaohuo888; ceshi3.com=000; pin=youhaohuo888; unick=youhaohuo888; thor=3B03A8EF266971935BB11D2F28D282CA9982237BD1FA529F0A4D8097B69E46B4DD03454CD9E4B06A35311098D3B6AA53C3C14F09B218FE4E07784CB9F235DCCD6CB906E5934B20BD3023BF539AA23D2FF7A1FBB3915724AB665C66A046D6256CBE8F1A8E68FA15A60014923789FBB6C39C8CF3BCC9E23E7700DD0E0CFB720C08475EBCABC88A9AA937F8282A9812B937; 3AB9D23F7A4B3C9B=PD7QC76TTQHMQ5PHP2FDISPSDZVAUTSP4I447EYS3EUY4RRLGWHSUFLVQJ4Y2NJJQ2SHNFL2QXM5276R64SJQLVDEM; __jda=108460702.14966414637391156997719.1496641464.1497500087.1497502631.38; __jdc=108460702; masterClose=yes; __jdu=14966414637391156997719'
    ck ='t=18a5c4915d62104669b70bf363493dcd; account-path-guide-s1=true; undefined_yxjh-filter-1=true; 106306839_yxjh-filter-1=true; 120482131_yxjh-filter-1=true; 120828063_yxjh-filter-1=true; 123398343_yxjh-filter-1=true; 42146858_yxjh-filter-1=true; cookie2=978862d906b0967b64b57fab11e6bcae; v=0; _tb_token_=QNn3xWIMSiq; cookie32=81b561b6a0fb8066f009f61b2d113974; cookie31=MTA2MzA2ODM5LHRiOTkzMzU3ODAsNzg2NjQ4NjQzQHFxLmNvbSxUQg%3D%3D; alimamapwag=TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgNi4zOyBXT1c2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzQ3LjAuMjUyNi4xMDYgU2FmYXJpLzUzNy4zNg%3D%3D; login=VFC%2FuZ9ayeYq2g%3D%3D; alimamapw=R1EAXwdVDQAJVmoBU1YNUlJTBANbUwNfClRXVgACUQEKBgJTAlUNV1ADWg%3D%3D; rurl=aHR0cDovL3B1Yi5hbGltYW1hLmNvbS8%2Fc3BtPWEyMzIwLjczODg3ODEuYTIxNHRyOC4xNS5IaEpROU8%3D; cna=D967EU69cWYCAWVR7Cq+kh5I; apushf4f28b675ff5e94dc07d6a8cd29d040c=%7B%22ts%22%3A1497527668549%2C%22heir%22%3A1497527613826%2C%22parentId%22%3A1497527606740%7D; isg=Ar-_VRJG2rRoXN7cOngQsxO2TpOJDGdHiT7BElGI1G6yYNfiSXbKl0Y21gdk'
    cookies = cj.getCookie(ck)
    #执行转链接功能
    def tbTurnLink(self,id):
        data = tb.getTaoBaoTurnLink(id)
        post = requests.post("http://pub.alimama.com/common/code/getAuctionCode.json", data=data, cookies=self.cookies)
        res = post.text
        print(res)
        # jd_ids = open("../config/jd_id_android.txt")
        # for id in jd_ids:
        #     data = jd.createLinkParam(file, type, id)
        #     post = requests.post("https://media.jd.com/gotoadv/getCustomCode/1", data=data, cookies=self.cookies)
        #     res = post.text
        #     if '请使用京东商城账号登录' in res or '你好，请登录' in res:
        #         print("你没有登录系统,请先登录")
        #     elif '400 Bad Request' in res:
        #         print("对不起爬虫请求被京东反爬虫系统屏蔽了")
        #         with open('../config/jd_turn_failed_id.txt', 'a') as f:
        #            f.write(id + '\n')
        #     else:
        #         p_res = json.loads(post.text)
        #         falg = p_res['success']
        #         print('post',p_res)
        #         if (falg == True):
        #             if 'urlAdvCode' in p_res:
        #                 urlAdvCode = str(p_res['urlAdvCode'])
        #                 jmu().updateLinkById(id.strip(), type, urlAdvCode)
        #                 print("success_id:", id.strip())
        #         else:
        #             #print('商品不在推广中')
        #             with open('../config/jd_nobuy_id.txt', 'a') as f:
        #                 f.write(id + '\n')
if __name__ == '__main__':
    startTime = datetime.datetime.now()
    tl = TurnLinkUtil().tbTurnLink("45071324263")
    endTime = datetime.datetime.now()
    hour=str((endTime - startTime).seconds)
    print("Andorid转链接完毕，耗时时间:",hour)