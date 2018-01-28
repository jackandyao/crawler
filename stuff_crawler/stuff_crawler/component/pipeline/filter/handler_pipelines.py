# this is use python script!
# -*- coding: UTF-8 -*-
from component.util.handle_util import HandleUtil as hu

#去除字符串中包含HTML标签 以及把商品佣金返还比例转换为数字类型
class HandlerScrapyPipeline(object):

    #过滤HTML标签 stuff_name stuff_promotion_rate img_url
    def process_item(self, item, spider):
        # 去除产品名称中的HTML标签
        item['stuff_name'] = hu.patternHanZi(item['stuff_name'])

        # 产品返佣比例数值化
        item['stuff_promotion_rate'] = hu.changeRate(item['stuff_promotion_rate'])

        #产品价格转换成数字类型
        item['stuff_reserve_price'] = hu.changePrice(item['stuff_reserve_price'])
        item['stuff_final_price'] = hu.changePrice(item['stuff_final_price'])
        # 产品图片添加https
        if "http" in item['stuff_img_url']:
            item['stuff_img_url'] = item['stuff_img_url']
        else:
            item['stuff_img_url'] = "http:" + item['stuff_img_url']

        return item

