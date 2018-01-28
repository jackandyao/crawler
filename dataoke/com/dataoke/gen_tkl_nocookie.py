# coding = utf-8
from bs4 import BeautifulSoup
import time
import re
import requests
import urllib.request
import urllib.parse
import json
import logging
import traceback
import collections
import hashlib
import base64
import datetime
import random
from pymongo import MongoClient
# from bson.objectid import ObjectId

#v5m
# high_key_secret = '23302613|37b2dfd56e41055e17e9a4d6416153f2'

high_app_session = '700001015476275a3a852f45b610ed833c950adb26653f4c5827fd0a99918d70debcc723317808183' # wyhw20170601     
                    
           
# pid = "mm_47816987_18966021_66434120"  # wyhw20170601

apps = [
    '23944059|ea4b5486f88abe5778371ea338ada68b',
    '23943516|212531aa8ff2e7fac1b5de820f815e0b',
    '23944251|0da0e27cb0247d2121b9f28dc8da9684',
    '23943731|9999efae449f3a7e9a8c99e1d12876d3',
    '23944626|c07a2b733a435c42073b6fa4a62c3d2d',
    '23944627|6d971d2e58819f76ea8f20fca70da0ec',
    '23944628|2b09e5f82b58ed4260b50ee2c40b06f9',
    '23945014|c6fc1182649a1deee28ca9821a98a9da',
    '23943881|9ad82d5e4bdcf199515bcdbe7236fbcb',
    '23949607|90827445187ab78e182338472c40040e',
    '24300109|fb11ab86beb151c5c31d9c91694f4f3e',
    '24300809|b3b48adf2cf1a83bdc3fcc4f8244be5e',
    '24299398|e72e8d0e1af715ea8802ca8788e3961e',
    '24299721|4c611d6b04ab1755b8e6a6173ad08bc1',
    '24299561|c4f1c477c1c65e83b9dc7d713f28b32b',
    '24299722|5ec2a8d75dca47553cf5e83cc6b2368a',
    '24300110|8b08ae128575c6df422c8ae4c35bc0c0',
    '24299564|a1056ad13b12b5658d5c5af11cf71362',
    '24300450|e8ffe2a1a1f868dadf7a820d99ffb146',
    '24300112|8d62479ab64769dffff9cf6862e05097',
    '24300813|fd72c51054b3fd373e2eea560be38245',
    '24300451|1980e69d9fad22022421f01c03c4e0a9',
    '24300262|0e7c21a54a8468bd5e5185be75138f3a',
    '24300113|a171e61d4af836fff1a324f018c2691a',
    '24299728|10205a4ea0a20fbb02db3dc595ae142e',
    '24301002|28624f2fef849446f1d5ce846e15bff1',
    '24301003|6f10148bc3b70a2390ba3df76c493907',
    '24300265|d9554e0e7473ed91a856cf67048248db',
    '24299906|2d0637a402b7cc0eee4e5d687c75e19b',
    '24408860|eb5f8f9e213856f50a04a575a772b4ac'
    ]


session = requests.Session()
session.trust_env = False

pc_html_header = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate, sdch",
    "Accept-Language": "en-US,en;q=0.8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.101 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
}

def get_tkl_params(key_secret,logo,url):
    appkey = key_secret.split('|')[0]
    u_logo = 'http://www.taobao.com/logo.jpg'
    if logo:
        u_logo = logo

    tpwd_param_dict = collections.OrderedDict([   
        ("logo",u_logo),
        ("url",url),
        ("text","我有好物-智能导购")
    ])
    tpwd_param = json.dumps(tpwd_param_dict, ensure_ascii=False,separators=(',',':'))

    tkl_sign_data = collections.OrderedDict([   
        ("app_key",appkey),
        ("format","json"),
        ("method","taobao.wireless.share.tpwd.create"),
        ("sign_method","md5"),
        ("timestamp",datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')),
        ("tpwd_param",tpwd_param),
        ("v","2.0")
    ])



    return tkl_sign_data

def get_high_params(pid,key_secret,session,item_id):
    app_key = key_secret.split('|')[0]
    pid_array = pid.split('_')
    site_id = pid_array[2]
    adzone_id = pid_array[3]
    high_sign_data = collections.OrderedDict([   
        ("adzone_id",adzone_id),
        ("app_key",app_key),
        ("format","json"),
        ("item_id",item_id),
        ("method","taobao.tbk.privilege.get"),
        ("platform", "1") ,
        ("session",session),
        ("sign_method","md5"),
        ("site_id",site_id),
        ("timestamp",datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')),
        ("v","2.0")
    ])
    return high_sign_data

def md5(data):
    m = hashlib.md5()
    m.update(data.encode())
    sign = m.hexdigest().upper()
    return sign

def get_tb_api_result(t_params_dict,key_secret):
    secret = key_secret.split('|')[1]
    final_str = ''
    params_str = ''
    for key,value in t_params_dict.items():
        final_str = final_str + key + value 
        params_str += '&' + key + '=' + urllib.parse.quote(value)
    sign = md5(secret+final_str+secret)
    apiurl = "http://gw.api.taobao.com/router/rest?sign="+sign + params_str
    return apiurl

# conn = MongoClient('192.168.132.172', 27017)
conn = MongoClient('mongodb://10.2.32.133:27017,10.2.32.134:27017,10.2.32.135:27017')
db = conn.wyhw  # 没有则自动创建
tab_dataoke_coupon = db.product_coupon  #使没有则自动创建
pid = "mm_123874690_29382961_109462297"
coupon_alimama_dict = {}
coupon_taobao_dict = {}

while True:
    s = tab_dataoke_coupon.find({'is_high':None,'valid':1},['_id','product_coupon_id','product_coupon_price','product_id','product_img','product_commission_type','product_price']).limit(20)
    for item in list(s):
        print(str(item['_id']))
        # 高佣接口
        # high_params = get_high_params(pid,high_key_secret,high_app_session,item['product_id'])
        # high_api = get_tb_api_result(high_params,high_key_secret)
        pid_array = pid.split('_')
        site_id = pid_array[2]
        adzone_id = pid_array[3]
        high_api = 'http://maomi.hz.taeapp.com/topapi_gaoxiao.php?get?&item_id=%s&adzone_id=%s&platform=1&site_id=%s&me=&session=%s' % (item['product_id'],adzone_id,site_id,high_app_session)
        print('v5m_api %s' % high_api)

        resp = requests.get(high_api,headers=pc_html_header)
        print(resp.text)
        resp_json = json.loads(resp.text)
        twoinone = ''

        if "App Call Limited" in resp.text:
            print("App Call Limited")
            time.sleep(30)
            continue
        elif "Remote service error" in resp.text:
            print("Remote service error")
            if "isv.item-not-exist" in resp.text:
                tab_dataoke_coupon.update({"_id":item['_id']},{"$set":{"valid":0}})
            time.sleep(5)
            continue

        return_points = 0
        final_coupon_price = 0
        coupon_data = resp_json['tbk_privilege_get_response']['result']['data']
        if 'coupon_remain_count' not in coupon_data:
            twoinone = "https://uland.taobao.com/coupon/edetail?activityId=%s&itemId=%s&pid=%s&af=1" % (item['product_coupon_id'],item['product_id'],pid)
        else:
            coupon_info = re.findall(r"满(\d*)元减(\d*)元",resp_json['tbk_privilege_get_response']['result']['data']['coupon_info'])
            product_coupon_condition = coupon_info[0][0]
            product_coupon_price = coupon_info[0][1]

            product_coupon_surplus = resp_json['tbk_privilege_get_response']['result']['data']['coupon_remain_count']
            product_coupon_receive = resp_json['tbk_privilege_get_response']['result']['data']['coupon_total_count'] - resp_json['tbk_privilege_get_response']['result']['data']['coupon_remain_count']
            

            if float(product_coupon_price) < float(item['product_coupon_price']):
                print('auto api is not highest, use the original coupon')
                twoinone = "https://uland.taobao.com/coupon/edetail?activityId=%s&itemId=%s&pid=%s&af=1" % (item['product_coupon_id'],item['product_id'],pid)
                final_coupon_price = float(item['product_coupon_price'])
            else:
                twoinone = resp_json['tbk_privilege_get_response']['result']['data']['coupon_click_url']
                final_coupon_price = float(product_coupon_price)
        return_points = int(float(resp_json['tbk_privilege_get_response']['result']['data']['max_commission_rate']) * (item['product_price'] - final_coupon_price) * 0.85 * 0.1)
        # print('return points: %s' % return_points )
        print(twoinone)
        # TKL
        i = random.randint(0,29)
        tkl_params = get_tkl_params(apps[i],item['product_img'],twoinone)
        tkl_api = get_tb_api_result(tkl_params,apps[i])
        resp = requests.get(tkl_api,headers=pc_html_header)
        resp_json = json.loads(resp.text)

        print(resp.text)
        if "App Call Limited" in resp.text:
            print("App Call Limited")
            time.sleep(30)
            continue


        
        tkl = resp_json['wireless_share_tpwd_create_response']['model']
        final_promo_info = {'qrCodeUrl':'','sclick':'','taoToken':'','shortLinkUrl':''}
        
        if tkl != None :
            final_promo_info['taoToken'] = tkl
            final_promo_info['sclick'] = twoinone
            # tab_dataoke_coupon.update({"_id":ObjectId(str(item['_id']))},{"$set":{"promo_info":promo_info}})
            tab_dataoke_coupon.update({"_id":item['_id']},{"$set":{"product_promo_info":final_promo_info,"return_points":return_points,"is_high":True}})
        else:
            print(resp.text)
        time.sleep(1)

