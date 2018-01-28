#!/usr/bin/python
#-*-coding:utf-8-*-

from pprint import pprint
from woaidu_crawler.utils import color

class FinalTestPipeline(object):

    
    def __init__(self):
        self.style = color.color_style()

    @classmethod
    def from_crawler(cls, crawler):
        pipe = cls()
        pipe.crawler = crawler
        return pipe
    
    def process_item(self, item, spider):
        print (self.style.NOTICE("SUCCESS(item):" + item['original_url']))
        #pprint(item)
        return item
