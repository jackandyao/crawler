# coding = utf-8
import requests
import json
import time
import datetime
import urllib.parse
from pymongo import MongoClient


class ProductCouponInfo:
    def __init__(self):
        self.product_source = ''
        self.product_platform = ''
        self.product_id = ''
        self.product_cat_id = ''
        self.product_seller_id = ''
        self.product_img = ''
        self.product_title = ''
        self.product_price = ''
        self.product_price_deduct_coupon = ''
        self.product_sales = ''
        self.product_coupon_id = ''
        self.product_coupon_price = ''
        self.product_coupon_etime = ''
        self.product_coupon_etimestamp = ''
        self.product_coupon_surplus = ''
        self.product_coupon_receive = ''
        self.product_coupon_condition = ''
        self.product_commission_type = ''
        self.product_commission_rate = ''
        # self.product_promo_info = ''
        self.product_promo_reason = ''
        self.valid = 1
        self.update_time = ''

session = requests.Session()
session.trust_env = False

pc_html_header = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate, sdch",
    "Accept-Language": "en-US,en;q=0.8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.101 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
}

def convert_to_dict(obj):
    '''把Object对象转换成Dict对象'''
    dict = {}
    dict.update(obj.__dict__)
    return dict

def convert_to_dicts(objs):
    '''把对象列表转换为字典列表'''
    obj_arr = []
    for o in objs:
        #把Object对象转换成Dict对象
        dict = {}
        dict.update(o.__dict__)
        obj_arr.append(dict)
    return obj_arr

def class_to_dict(obj):
    '''把对象(支持单个对象、list、set)转换成字典'''
    is_list = obj.__class__ == [].__class__
    is_set = obj.__class__ == set().__class__
    if is_list or is_set:
        obj_arr = []
        for o in obj:
            #把Object对象转换成Dict对象
            dict = {}
            dict.update(o.__dict__)
            obj_arr.append(dict)
        return obj_arr
    else:
        dict = {}
        dict.update(obj.__dict__)
        return dict



i = 1

# conn = MongoClient('192.168.132.172', 27017)
# db = conn.wyhw  # 没有则自动创建
# tab_dataoke_coupon = db.dataoke_coupon  #使没有则自动创建

# while i < 2:
#     dataoke_coupon_api = 'http://api.dataoke.com/index.php?r=Port/index&type=total&appkey=j40ne9pui5&v=2&page=%s' % i
#     print(dataoke_coupon_api)
#     rep = session.get(dataoke_coupon_api,headers=pc_html_header)
#     if len(rep.text) > 500 :
#         rep_json = json.loads(rep.text)
#         for j in range(0, len(rep_json['result'])):
#             date_string = rep_json['result'][j]['Quan_time']
#             data_string_array = date_string.split(' ')
#             rep_json['result'][j]['Quan_timestamp'] = time.mktime(datetime.datetime.strptime(rep_json['result'][j]['Quan_time'],'%Y-%m-%d %H:%M:%S').timetuple())
#             rep_json['result'][j]['Dx'] = 0 if rep_json['result'][j]['Commission_queqiao'] > rep_json['result'][j]['Commission_jihua'] else 1

#             # print(rep_json['result'][j]['Quan_time'])
#         tab_dataoke_coupon.insert(rep_json['result'])
#         time.sleep(5)
#     else:
#         break
#     i = i + 1

        # print(rep_json['result'])
    # print(rep.content.decode('unicode_escape'))

conn = MongoClient('192.168.132.172', 27017)
db = conn.wyhw  # 没有则自动创建
tab_dataoke_coupon = db.product_coupon  #使没有则自动创建
print('start to count')
tab_dataoke_coupon_count = tab_dataoke_coupon.count()



while True:
    dataoke_coupon_api = 'http://api.dataoke.com/index.php?r=Port/index&type=total&appkey=j40ne9pui5&v=2&page=%s' % i
    print(dataoke_coupon_api)
    rep = session.get(dataoke_coupon_api,headers=pc_html_header)
    if len(rep.text) > 500 :
        rep_json = json.loads(rep.text)
        # print(rep_json)
        if rep_json['data']['total_num'] >= 1:
            
            coupons =  []
            for j in range(0, len(rep_json['result'])):
                tmp_coupon = ProductCouponInfo()
                tmp_coupon.product_source = 'dataoke'
                tmp_coupon.product_platform = '天猫' if rep_json['result'][j]['IsTmall'] == 1 else '淘宝'
                tmp_coupon.product_id = rep_json['result'][j]['GoodsID']
                tmp_coupon.product_cat_id = rep_json['result'][j]['Cid']
                tmp_coupon.product_seller_id = rep_json['result'][j]['SellerID']
                tmp_coupon.product_img = rep_json['result'][j]['Pic']
                tmp_coupon.product_title = rep_json['result'][j]['Title']
                tmp_coupon.product_price = rep_json['result'][j]['Org_Price']
                tmp_coupon.product_price_deduct_coupon = rep_json['result'][j]['Price']
                tmp_coupon.product_sales = rep_json['result'][j]['Sales_num']
                tmp_coupon.product_coupon_id = rep_json['result'][j]['Quan_id']
                tmp_coupon.product_coupon_price = rep_json['result'][j]['Quan_price']
                date_string = rep_json['result'][j]['Quan_time']
                data_string_array = date_string.split(' ')
                tmp_coupon.product_coupon_etime = rep_json['result'][j]['Quan_time']
                tmp_coupon.product_coupon_etimestamp = time.mktime(datetime.datetime.strptime(rep_json['result'][j]['Quan_time'],'%Y-%m-%d %H:%M:%S').timetuple())
                tmp_coupon.product_coupon_surplus = rep_json['result'][j]['Quan_surplus']
                tmp_coupon.product_coupon_receive = rep_json['result'][j]['Quan_receive']
                tmp_coupon.product_coupon_condition = rep_json['result'][j]['Quan_condition']
                tmp_coupon.product_promo_reason = rep_json['result'][j]['Introduce']
                tmp_coupon.update_time = rep_json['data']['update_time']
                
                # print(rep_json['result'][j]['Jihua_link'] == '')
                if rep_json['result'][j]['Commission_jihua'] > rep_json['result'][j]['Commission_queqiao']:
                    if rep_json['result'][j]['Jihua_link'] == '':
                        tmp_coupon.product_commission_type = '通用'
                    else:
                        tmp_coupon.product_commission_type = '定向'
                    tmp_coupon.product_commission_rate = rep_json['result'][j]['Commission_jihua']

                else:
                    tmp_coupon.product_commission_type = '鹊桥'
                    tmp_coupon.product_commission_rate = rep_json['result'][j]['Commission_queqiao']

                # uland_api = "https://uland.taobao.com/coupon/edetail?activityId=%s&itemId=%s&pid=mm_123874690_29382961_109462297&af=1" %(tmp_coupon.product_coupon_id,tmp_coupon.product_id)

                # tkl_api = "http://localhost:29033/tbk/tkl?url=%s" % urllib.parse.quote(uland_api)
                # r = session.get(tkl_api ,headers=pc_html_header)
                # if r.text:
                #     tmp_coupon.product_promo_info = json.loads(r.text)
                # else:
                #     tmp_coupon.product_promo_info = ''
                
                if tab_dataoke_coupon_count <= 0:
                    coupons.append(tmp_coupon)
                else:
                    #更新模式
                    tab_dataoke_coupon.find_one_and_update(
                        {'product_id': tmp_coupon.product_id,'product_coupon_id':tmp_coupon.product_coupon_id},
                        {'$set': convert_to_dict(tmp_coupon)},
                        upsert = True
                    )

                # print(rep_json['result'][j]['Quan_time'])

            if tab_dataoke_coupon_count <= 0:
                tab_dataoke_coupon.insert(convert_to_dicts(coupons))
            
        if rep_json['data']['total_num'] < 50:
            break
            # print(convert_to_dicts(coupons))
        time.sleep(2)
    else:
        break
    i = i + 1