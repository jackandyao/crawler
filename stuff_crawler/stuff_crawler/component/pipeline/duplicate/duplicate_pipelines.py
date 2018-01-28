# this is use python script!
# -*- coding: UTF-8 -*-
from scrapy.exceptions import DropItem

#去除重复的item
class DuplicateScrapyPipeline(object):

    def __init__(self):
        self.ids_seen = set()

    def process_item(self, item, spider):

        if item['stuff_real_id'] in self.ids_seen:
            raise DropItem('DuplicateScrapyPipeline-发现重复',item['stuff_real_id'])
        else:
            self.ids_seen.add(item['stuff_real_id'])
            return item