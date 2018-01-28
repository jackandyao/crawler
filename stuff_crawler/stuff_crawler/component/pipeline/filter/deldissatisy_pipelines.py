# this is use python script!
# -*- coding: UTF-8 -*-
from scrapy.exceptions import DropItem
from scrapy.conf import settings
import datetime

#删除不满足条件的item
class DelDissatisyScrapyPipeline(object):

    def process_item(self, item, spider):
        print('del',item)
        if (item !=None):
            filter_type = settings['FILTER_TYPE']
            types = filter_type.split(",")
            for type in types:
                self.filterByType(type, item)

    #根据过滤类型选择对应的过滤方法
    def filterByType(self,type,item):
        if (type =='sell_number'):
            self.filterSellerNumber(item)
        elif (type =='ratio'):
            self.filterPromotionRatio(item)
        elif (type =='end_date'):
            self.filterEndDate(item)
        else:
            return item

    #过滤销量不满足的item
    def filterSellerNumber(self,item):
        # 获取销量
        sell_number = settings['SELL_MIN_NUMBER']
        item_number = item['stuff_order_num']
        if (item_number<int(sell_number)):
            raise DropItem('删除销量不满足条件的item',item['stuff_real_id'])
        else:
            return item

    #过滤佣金比例不满足的item
    def filterPromotionRatio(self,item):
        #获取佣金比例
        ratio = settings['PROMTION_RATE']
        item_ratio = item['stuff_promotion_rate']
        if (item_ratio < ratio):
            raise DropItem('删除佣金比例不满足条件的item',item['stuff_real_id'])
        else:
            return item

    #比较推广日期
    def filterEndDate(self,item):
        end_date = item['stuff_end_date']
        if (end_date!=""):
            variable_date = settings['VARIABLE_END_DATE']
            end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d')
            now_date = datetime.datetime.strptime(variable_date, '%Y-%m-%d')
            day = (end_date - now_date).days
            if (day <0):
                raise DropItem('删除产品推广日期不满足条件的item', item['stuff_real_id'])
            else:
                return item
        else:
            return item
