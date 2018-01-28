# this is use python script!
# -*- coding: UTF-8 -*-

from scrapy import Field,Item


#定义其它的Item
class TaoBaoSpiderItem(Item):
    # 实际商品id
    real_stuff_id = Field()
    # 商品名称
    name = Field()
    # 原价
    reserve_price = Field()
    # 商品最终价格
    final_price = Field()
    # 推广佣金比
    promotion_rate = Field()
    # 商品链接
    url = Field()
    # 商品图片链接
    img_url = Field()
    # 商品来源
    use_type = Field()
    # 店铺id
    shop_id = Field()
    # 商家名称
    shop_name = Field()
    # 推广销量
    order_num = Field()
    # 常量字段
    rebate_id = Field()
    android_promotion_url = Field()
    ios_promotion_url = Field()
    cat_id = Field()
    cat_name = Field()
    status = Field()
    source = Field()
    id = Field()
    create_time = Field()
    update_time = Field()
    click_num = Field()
    operator_source = Field()


class JDSpiderItem(Item):
    # 实际商品id
    real_stuff_id = Field()
    # 商品名称
    name = Field()
    # 原价
    reserve_price = Field()
    # 商品最终价格
    final_price = Field()
    # 推广佣金比
    promotion_rate = Field()
    # 商品链接
    url = Field()
    # 商品图片链接
    img_url = Field()
    # 商品来源
    use_type = Field()
    # 商家名称
    shop_name = Field()
    # 推广销量
    order_num = Field()
    # 常量字段
    rebate_id = Field()
    android_promotion_url = Field()
    ios_promotion_url = Field()
    cat_id = Field()
    #cat_name = Field()
    status = Field()
    source = Field()
    id = Field()
    create_time = Field()
    update_time = Field()
    operator_source = Field()
    start_date = Field()
    end_date = Field()
    dir_name = Field()
    dir_path = Field()

    #
class JDTurnLinkItem(Item):
    id = Field()
    android_link =Field()
    ios_link =Field()

class JDMySQLItem(Item):
    id = Field()
    name =Field()
