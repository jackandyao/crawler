# this is use python script!
# -*- coding: UTF-8 -*-
from scrapy import cmdline
#爬虫方法入口处
#注意这里是固定写法:'scrapy crawl +爬虫名称(你项目中定义的爬虫name是什么就是什么)'
cmdline.execute("scrapy crawl woaidu".split())

