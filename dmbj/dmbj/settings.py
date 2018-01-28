# -*- coding: utf-8 -*-
#爬虫生成的名称
BOT_NAME = 'dmbj'

#爬虫的模块
SPIDER_MODULES = ['dmbj.spiders']
NEWSPIDER_MODULE = 'dmbj.spiders'


# Obey robots.txt rules
ROBOTSTXT_OBEY = True

#MONGODB的基础信息
MONGODB_HOST = "192.168.14.107" #MONGOD的地址
MONGODB_PORT = 27017 #MONGOD默认端口
MONGODB_DB = 'crawler_weather' #MONGO创建的DB名称
MONGODB_COLL = 'weather'  #MONGO创建COLLECTION名称


# SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
# SCHEDULER_PERSIST = True
# SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderPriorityQueue"
#分布式情况下-slave节点配置的
#REDIS_URL = 'redis://192.168.14.245:6379'

# REDIS_URL = None
# #分布式情况下master节点配置的
# REDIS_HOST = '192.168.14.245'
# REDIS_PORT = 6379

#指定爬虫访问的客户端,实际生产环境可以配置多个
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'

#指定处理爬取过之后的数据的管道,一般都是持久化操作
#这里的写法也是固定的,类似于java中的包名+类名
ITEM_PIPELINES = {
   'dmbj.pipelines.DmbjPipeline': 300,
}

#下载中间件 0-1000
DOWNLOADER_MIDDLEWARES = {
    'dmbj.download_proxy_middle_ware.DmbjDownLoadProxyIPMiddleWare': 541,
    'dmbj.proxy_middle_ware.DmbjSpiderHttpProxyMiddleware': 542,
    'dmbj.random_user_agent.DmbjSpiderUserAgentMiddleware': 543,
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 542,
 }

#配置IP代理池
IPPOOL=[
    {"ip_addr": "106.46.204.53:31772"},
    {"ip_addr": "58.217.25.244:34791"},
    {"ip_addr": "218.91.20.98:44230"},
    {"ip_addr": "125.112.197.165:33508"},
    {"ip_addr": "110.85.89.205:33716"},
    {"ip_addr": "183.52.76.127:44390"},
    {"ip_addr": "223.245.251.57:35160"}
]
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