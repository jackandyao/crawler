# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy import signals
import json
import codecs
import sys

class TaobaomuluPipeline(object):
    def __init__(self):
        #self.file = codecs.open('data.json', 'wb', encoding='utf-8')
        self.file = "data"
        self.file += ".txt"
        self.fp = open(self.file, 'w',encoding='utf-8')
    def process_item(self, item, spider):
        # file_name = "data"
        # file_name += ".txt"
        # fp = open(file_name, 'wb')
        # fp.write(item['mulu_content'])
        # fp.close()
        # line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        # self.file.write(line)

        mulu_level1 = str(item['mulu_level1']).replace('[\'','')
        mulu_level1 = mulu_level1.replace('\']','')
        mulu_level2 = str(item['mulu_level2']).replace('[\'','')
        mulu_level2 = mulu_level2.replace('\']', '')
        mulu_level3 = str(item['mulu_level3']).replace('[\'','')
        mulu_level3 = mulu_level3.replace('\']', '')
        mulu_level3 = mulu_level3.replace('\'', '')

        for value in item['mulu_level3']:
            #print('x',value)
            mulu_level = mulu_level1 + "_" + mulu_level2 + "_" + value + "\n"
            self.fp.write(mulu_level)
        return item
    def spider_closed(self, spider):
        # self.file.close()
        self.fp.close()
        pass
