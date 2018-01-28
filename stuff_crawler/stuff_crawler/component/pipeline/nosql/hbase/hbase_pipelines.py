# this is use python script!
# -*- coding: UTF-8 -*-
from scrapy.conf import settings
from component.util.config_util import ConfigUtil as conf
import happybase
import _md5
#使用hbase保存爬虫清洗之后的数据
class HBaseScrapyPipeline(object):
    def __init__(self):
        file = settings['HBASE_CONF_FILE']
        selection =  "hbase_" + settings['PROJECT_MODE_TYPE']
        host = conf(file).getValue(selection,'HBASE_HOST')
        table_name = conf(file).getValue(selection,'HBASE_TABLE')
        connection = happybase.Connection(host)
        table = connection.table(table_name)
        self.table = table

    def process_item(self, item, spider):
        stuff_id = item['stuff_id']
        stuff_detail = item['stuff_detail']
        # rowkey,data
        rowKey =""
        #data = {'cf1:stuff_id': stuff_id, 'cf1:stuff_detail': stuff_detail}
        rowData=""
        self.table.put(rowKey,rowData)
        return item