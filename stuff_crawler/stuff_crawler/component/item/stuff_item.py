# this is use python script!
# -*- coding: UTF-8 -*-
from scrapy import Field,Item

#保存产品实体信息
class StuffItem(Item):

    #原始商品ID加上对应的平台标识组成新的商品标识
    stuff_real_id = Field()
    #商品名称
    stuff_name = Field()
    #原价
    stuff_reserve_price = Field()
    #商品最终价格
    stuff_final_price = Field()
    #推广佣金比
    stuff_promotion_rate = Field()
    #商品链接
    stuff_url = Field()
    #商品图片链接
    stuff_img_url = Field()
    #月销量
    stuff_order_num = Field()
    #商品返利配置系数标识
    stuff_rebate_id = Field()
    #AND平台对应的转链接
    stuff_android_promotion_url = Field()
    #IOS平台对应的转链接
    stuff_ios_promotion_url = Field()
    #针对有优惠券的商品 直接调用二合一转链接接口即可
    stuff_two_one_promotion_url = Field()
    #目录编码
    stuff_cat_id = Field()
    #目录名称
    stuff_cat_name = Field()
    #目录路径
    stuff_cat_path = Field()
    #产品状态 审核 上架 下架
    stuff_status = Field()
    #产品来源 天猫 淘宝 京东 唯品会..
    stuff_source = Field()
    #产品原始ID
    stuff_id = Field()
    #创建时间 索引全量标识
    stuff_create_time = Field()
    #更新时间 索引更新标识
    stuff_update_time = Field()
    #当前转链接使用的阿里妈妈账号
    stuff_operator_name = Field()
    #商品推荐链接有效的开始日期
    #商品推荐链接有效的结束日期
    stuff_start_date = Field()
    stuff_end_date = Field()