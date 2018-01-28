# this is use python script!
# -*- coding: UTF-8 -*-
import re
class HandleUtil:

    #去除产品名称的HTML标签
    def patternHanZi(str):
        re_h = re.compile('</?\w+[^>]*>')  # HTML标签
        str = re_h.sub('', str)  # 去掉HTML 标签
        return str

    #把推广佣金比例转换为数值类型
    def changeRate(rate):
        return int(float(rate.replace('%', '')) * 100)

    #把价格改成数字类型
    def changePrice(price):
        if "￥" in str(price):
            return int(float(price.replace('￥', '').replace(',', '')))
        else:
            return price

    #提取非括号之内的字
    def regexChinese(val):
        return re.sub('（[^）]+）','',val)

#HTC U Ultra蓝宝石版（U-1w-128G）远望（蓝） 移动联通电信六模全网通 双卡双待双屏
if __name__ == '__main__':
    str = HandleUtil.regexChinese('<span size =4>HTC U Ultra蓝宝石版（U-1w-128G）</span>远望（蓝） 移动联通电信六模全网通 双卡双待双屏')
    #ratio = HandleUtil.changeRate('2.8')
    print(str)