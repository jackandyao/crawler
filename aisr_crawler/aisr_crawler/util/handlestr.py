# this is use python script!
# -*- coding: UTF-8 -*-
import re
class HandleStr():

    # 匹配中文
    def patternHanZi(str):
        re_h = re.compile('</?\w+[^>]*>')  # HTML标签
        str = re_h.sub('', str)  # 去掉HTML 标签
        return str






#HTC U Ultra蓝宝石版（U-1w-128G）远望（蓝） 移动联通电信六模全网通 双卡双待双屏
if __name__ == '__main__':
    str = HandleStr.patternHanZi('<span size =4>HTC U Ultra蓝宝石版（U-1w-128G）</span>远望（蓝） 移动联通电信六模全网通 双卡双待双屏')
    print(str)