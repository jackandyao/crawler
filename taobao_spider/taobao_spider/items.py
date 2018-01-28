# -*- coding: utf-8 -*-

from scrapy import Field,Item

class TaobaoSpiderItem(Item):
    # 实际商品id
    real_stuff_id = Field()
    # 商品名称
    name = Field()
    # 原价
    reserve_price = Field()
    # 商品最终价格
    final_price = Field()
    # 返利类型rebate表id
    rebate_id = Field()
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
    status = Field()
    source = Field()
    id = Field()
    create_time = Field()
    update_time = Field()
    click_num = Field()
    operator_source = Field()

#保存古诗文内容
class PoemlSpiderItem(Item):
    link = Field()
    name = Field()
    dynasty = Field()
    author = Field()
    content = Field()

#博客内容
class BotcnblogsItem(Item):
    # define the fields for your item here like:
    title = Field()        #标题
    publishDate = Field()  #发布日期
    readCount = Field()    #阅读量
    commentCount = Field() #评论数<br><br>