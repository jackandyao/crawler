# -*- coding: utf-8 -*-


BOT_NAME = 'aisr_crawler'

SPIDER_MODULES = ['aisr_crawler.spiders']

NEWSPIDER_MODULE = 'aisr_crawler.spiders'

HTTPERROR_ALLOWED_CODES = [400]

COOKIES_ENABLED=True

COOKIES_DEBUG=True

#ROBOTSTXT_OBEY = True
ROBOTSTXT_OBEY = False

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

#Mysql数据库的配置信息
MYSQL_HOST = '192.168.14.107'
MYSQL_DBNAME = 'qbao_stuff'         #数据库名字，请修改
MYSQL_USER = 'wangping'             #数据库账号，请修改
MYSQL_PASSWD = 'sadas3432$#%ret@!'         #数据库密码，请修改
MYSQL_PORT = 3306               #数据库端口，在dbhelper中使用

#MONGODB的基础信息
MONGODB_HOST = "192.168.14.107" #MONGOD的地址
MONGODB_PORT = 27017 #MONGOD默认端口
#MONGODB_USERNAME = "aisr123" #MONGOD用户名
#MONGODB_PASSWORD = "aisr??$$" #MONGOD密码
MONGODB_DB = 'jd_spiders' #MONGO创建的DB名称
MONGODB_COLL = 'jd_0706'  #MONGO创建COLLECTION名称

#REDIS消息队列
# SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
# SCHEDULER_PERSIST = True
# SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderPriorityQueue"
#分布式情况下-slave节点配置的
#REDIS_URL = 'redis://192.168.14.245:6379'

# REDIS_URL = None
# # #分布式情况下master节点配置的
# REDIS_HOST = '192.168.14.245'
# REDIS_PORT = 6379

#下载中间件 0-1000
DOWNLOADER_MIDDLEWARES = {
    #'aisr_crawler.middleware.proxy.multi_proxy_ip.SpiderDownLoadProxyIPMiddleWare': 541,
    'aisr_crawler.middleware.agent.multi_agent_switch.SpiderUserAgentMiddleware': 542,
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    #'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 542,
 }

#指定处理爬取过之后的数据的管道,一般都是持久化操作
#这里的写法也是固定的,类似于java中的包名+类名 MongoUpdatePipeline
ITEM_PIPELINES = {
   'aisr_crawler.pieple.mongo.mongodb_pipelines.MongoPipeline': 300,
   #'aisr_crawler.pieple.mongo.mongodb_update_pipelines.MongoUpdatePipeline': 300,
   #'aisr_crawler.pieple.mysql.mysql_pipelines.JsonWithEncodingPipeline':300,
   #'aisr_crawler.pieple.mysql.mysql_pipelines.MySQLScrapyPipeline':300
}
