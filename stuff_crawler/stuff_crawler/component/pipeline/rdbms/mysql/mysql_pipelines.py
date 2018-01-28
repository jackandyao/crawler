# this is use python script!
# -*- coding: UTF-8 -*-
from twisted.enterprise import adbapi
from component.pipeline.rdbms.mysql.dbhelper import DBHelper as dbh
from scrapy.conf import settings
#存储数据到MYSQL数据库中
class MySQLScrapyPipeline(object):
    #默认会调用的方法
    def process_item(self, item, spider):
        con = dbh().connectMysql()
        cursor = con.cursor()
        execSql = settings['MYSQL_EXECUTION_SQL']
        try:
            cursor.execute(execSql, (
                item['stuff_real_id'], item['stuff_name'],
                item['stuff_reserve_price'], item['stuff_final_price'],
                item['stuff_promotion_rate'], item['stuff_url'],
                item['stuff_img_url'], item['stuff_order_num'],
                item['stuff_rebate_id'], item['stuff_android_promotion_url'],
                item['stuff_ios_promotion_url'], item['stuff_two_one_promotion_url'],
                item['stuff_cat_id'], item['stuff_cat_name'],
                item['stuff_cat_path'], item['stuff_status'],
                item['stuff_source'], item['stuff_source'],
                item['stuff_create_time'], item['stuff_update_time'],
                item['stuff_operator_name']
                                     ))
            con.commit()
        except Exception as err:
            print('error',err)
            con.rollback()
        return item



