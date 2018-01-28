# -*- coding: utf-8 -*-

# Scrapy settings for taobao_spider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'taobao_spider'

SPIDER_MODULES = ['taobao_spider.spiders']
NEWSPIDER_MODULE = 'taobao_spider.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'taobao_spider (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True
#ROBOTSTXT_OBEY = False
# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'taobao_spider.middlewares.TaobaoSpiderSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'taobao_spider.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'taobao_spider.pipelines.TaobaoSpiderPipeline': 300,
}


#MONGODB的基础信息
MONGODB_HOST = "127.0.0.1" #MONGOD的地址
MONGODB_PORT = 27017 #MONGOD默认端口
MONGODB_DB = 'taobao_crawler' #MONGO创建的DB名称
MONGODB_COLL = 'taobao'  #MONGO创建COLLECTION名称

USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'



#下载器超时时间(单位: 秒)
DOWNLOAD_TIMEOUT=180
#下载器在下载同一个网站下一个页面前需要等待的时间。该选项可以用来限制爬取速度， 减轻服务器压力。同时也支持小数
DOWNLOAD_DELAY = 1
#即Item Pipeline能同时处理(每个response的)item的最大值
CONCURRENT_ITEMS = 100

#并发请求(concurrentrequests)的最大值。
CONCURRENT_REQUESTS = 16

#对单个网站进行并发请求的最大值
CONCURRENT_REQUESTS_PER_DOMAIN = 8

#对单个IP进行并发请求的最大值
CONCURRENT_REQUESTS_PER_IP = 0

#爬取网站最大允许的深度(depth)值。如果为0，则没有限制
DEPTH_LIMIT = 0
#整数值。用于根据深度调整request优先级 如果为0，则不根据深度进行优先级调整
DEPTH_PRIORITY = 0

#否启用DNS内存缓存(DNS in-memory cache)
DNSCACHE_ENABLED = True

AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 3.0
AUTOTHROTTLE_CONCURRENCY_CHECK_PERIOD = 10