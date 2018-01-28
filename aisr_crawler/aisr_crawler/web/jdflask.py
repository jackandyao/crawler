# this is use python script!
# -*- coding: UTF-8 -*-
import urllib

import requests
#根据条件抓取京东商品
#商品关键字+商品价格范围+佣金排序+销量排序
class JDFlaskService:

    def getSpuList(self,keyWord,fromPrice,toPrice,pageIndex,cookieValue):
        # param ={}
        # param['keyword'] = keyWord
        # param['fromPrice'] = fromPrice
        # param['toPrice'] = toPrice
        # data = urllib.parse.urlencode(param)
        # ck = 'unpl=V2_ZzNtbUVVRhZ0CRQEcxoLBWJWFg0RB0RGIQpAVSlOX1E0V0FdclRCFXMUR1BnG10UZwQZXEdcQBFFCEdkexhdBGYKF1hGXnMRJwtPAHJKCAIyBhZZFlRBJUULRmR7GGwFZQsTX0pRRBV3OHZTSykaXDxGVABKVEslcABAVHoZXQRjMxNtQ2cIe3RFRlZzGF4NYQQSX3JWcxY%3d; mobilev=html5; mba_muid=1496131508405678339613; __jdv=122270672|baidu|-|organic|not set|1496226156058; ssid="SGDDNESuTF+ATb5b+IUJVQ=="; masterClose=yes; 3AB9D23F7A4B3C9B=PD7QC76TTQHMQ5PHP2FDISPSDZVAUTSP4I447EYS3EUY4RRLGWHSUFLVQJ4Y2NJJQ2SHNFL2QXM5276R64SJQLVDEM; TrackID=1vnJxzgRJhqVN4E4s7zuLzAB0oIxnNB1VWJyYUmJIzyTGMdBtUgT-qMx94gDCymhvlVBfRev7F0SVYXz4Efq0fw; pinId=_4Vc37lERPk; _tp=1p445VhAqKBizAUsKQ93lg%3D%3D; logining=1; _pst=520bsj; ceshi3.com=000; thor=3E5861AF1D99F9183C5A3C2EB78D3BB7179C2DBD62B64C85A84FCB8ED3B6B7F46F9FD6920E4E246639BC147414B648F248EFBA30896AE05B3D04C14380966F68F94C3B500AAE6070CD5E75369CB42439203937E7D2D7EE348D99938803326F7580D1183094DCA14D68F3C2FCF8098293ED30AF2FCAB14A259686196231E12210; pin=520bsj; unick=520bsj; __jda=108460702.14961324377181286274750.1496132437.1496381400.1496413010.18; __jdb=108460702.4.14961324377181286274750|18.1496413010; __jdc=108460702; __jdu=14961324377181286274750'
        # cookies = cj.getCookie(cookieValue)
        # httpurl = r'https://media.jd.com/gotoadv/goods'
        # full_url = httpurl + "?" + data + "&pageIndex=" + str(pageIndex)
        # get_result = requests.get(full_url,data=data,cookies=cookies)
        return