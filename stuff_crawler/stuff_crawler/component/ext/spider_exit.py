# this is use python script!
# -*- coding: UTF-8 -*-import logging
from scrapy import signals
from scrapy.exceptions import NotConfigured
import logging
logger = logging.getLogger(__name__)
from component.util.phone_util import PhoneMessageUtil as phone
from scrapy.conf import settings
class SpiderOpenCloseLogging(object):

    def __init__(self, item_count):
        self.item_count = item_count



    @classmethod
    def from_crawler(cls, crawler):

        if not crawler.settings.getbool('MYEXT_ENABLED'):
            raise NotConfigured
        item_count = crawler.settings.getint('MYEXT_ITEMCOUNT', 1000)
        ext = cls(item_count)

        crawler.signals.connect(ext.spider_opened, signal=signals.spider_opened)
        crawler.signals.connect(ext.spider_closed, signal=signals.spider_closed)
        crawler.signals.connect(ext.item_scraped, signal=signals.item_scraped)
        return ext

    def spider_opened(self, spider):
        logger.info("opened spider %s", spider.name)

    def spider_closed(self,spider):
        print('爬虫结束,准备发送短消息!')
        phone_path = settings['PHONENUMBER_PATH']
        phone.sendPhoneMsg(phone_path, "爬虫已结束")

    def item_scraped(self, item, spider):
        print('item',item)
        self.items_scraped += 1

