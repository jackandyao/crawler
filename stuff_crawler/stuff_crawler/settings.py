# -*- coding: utf-8 -*-

# 避免被禁止(ban)
'''
使用user agent池，轮流选择之一来作为user agent。池中包含常见的浏览器的user agent(google一下一大堆)
禁止cookies(参考 COOKIES_ENABLED)，有些站点会使用cookies来发现爬虫的轨迹。
设置下载延迟(2或更高)。参考 DOWNLOAD_DELAY 设置。
如果可行，使用 Google cache 来爬取数据，而不是直接访问站点。
使用IP池。例如免费的 Tor项目 或付费服务(ProxyMesh)。
使用高度分布式的下载器(downloader)来绕过禁止(ban)，您就只需要专注分析处理页面。这样的例子有: Crawlera
增加并发 CONCURRENT_REQUESTS = 100
禁止cookies:COOKIES_ENABLED = False
禁止重试:RETRY_ENABLED = False
减小下载超时:DOWNLOAD_TIMEOUT = 15
禁止重定向:REDIRECT_ENABLED = False
启用 “Ajax Crawlable Pages” 爬取:AJAXCRAWL_ENABLED = True
'''


BOT_NAME = 'stuff_crawler'

SPIDER_MODULES = ['stuff_crawler.spiders']

NEWSPIDER_MODULE = 'stuff_crawler.spiders'

# Obey robots.txt rules
#ROBOTSTXT_OBEY = True
#禁止重试
RETRY_ENABLED = False

ROBOTSTXT_OBEY = False

#配置爬虫IP被第三方网站拦截的时候 抛出的异常
HTTPERROR_ALLOWED_CODES = [403,400]
#禁止cookie
# COOKIES_ENABLED=False

# COOKIES_DEBUG=True

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
MYSQL_CONF_FILE ="component/config/mysql.conf"
#Mysql数据库的配置信息
MYSQL_HOST = '192.168.14.107'
MYSQL_DBNAME = 'qbao_stuff_v2'         #数据库名字，请修改
MYSQL_USER = 'wangping'             #数据库账号，请修改
MYSQL_PASSWD = 'sadas3432$#%ret@!'         #数据库密码，请修改
MYSQL_PORT = 3306               #数据库端口，在dbhelper中使用
#MONGODB的配置文件信息
#MONGODB_CONF_FILE ="component/config/mongo.conf"
MONGODB_CONF_FILE ="component/config/mongo.conf"
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

#配置HBASE文件
HBASE_CONF_FILE ="component/config/hbase.conf"


#下载中间件 0-1000
DOWNLOADER_MIDDLEWARES = {
    'component.middleware.agent.multi_agent_switch.SpiderUserAgentMiddleware': 541,
    #'component.middleware.proxy.multi_proxy_switch.SpiderMultiProxyMiddleWare': 542,
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    #'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 542,
 }

# 配置一些列的ITEM处理组件 后面数字代表执行的顺序(从低到高执行0-1000)
ITEM_PIPELINES = {
    'component.pipeline.duplicate.duplicate_pipelines.DuplicateScrapyPipeline' :3,
    #'component.pipeline.filter.deldissatisy_pipelines.DelDissatisyScrapyPipeline' :2,
    'component.pipeline.filter.handler_pipelines.HandlerScrapyPipeline' : 1,
    #'component.pipeline.nosql.hbase.hbase_pipelines.HBaseScrapyPipeline' : 2,
    'component.pipeline.nosql.mongodb.mongodb_pipelines.MongoDBScrapyPipeline' : 4,
    #'component.pipeline.rdbms.mysql.mysql_pipelines.MySQLScrapyPipeline' : 4
}


#配置mongodb执行操作的类型 insert update delete
MONGODB_OPERATOR_TYPE = 'insert'

#配置mysql操作语句
MYSQL_EXECUTION_SQL ="insert into qbao_stuff_v2.stuff(stuff_real_id,stuff_name,stuff_reserve_price,stuff_final_price,stuff_promotion_rate,stuff_url,stuff_img_url,stuff_order_num,stuff_rebate_id,stuff_android_promotion_url,stuff_ios_promotion_url,stuff_two_one_promotion_url,stuff_cat_id,stuff_cat_name,stuff_cat_path,stuff_status,stuff_source,stuff_id,stuff_create_time,stuff_update_time,stuff_operator_name) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

#配置读取IP的文件地址
IP_FILE_PATH =""


#配置的电话号码
PHONENUMBER_PATH ="component/config/phone.txt"

#保存抓取失败的URL或者关键字
STUFF_FAIL_URL ="component/config/fail_url.txt"

#启动自定义扩展功能
MYEXT_ENABLED = True

MYEXT_ITEMCOUNT = 1

#自定义扩展
# EXTENSIONS = {
#     'component.ext.spider_exit.SpiderOpenCloseLogging': 44,
# }

#搜索类型 all qqg nine twent
SEARCH_TYPE ="all"


#读取目录配置地址
STUFF_DIR_PATH ="component/data/dir"

#单个工具类util读取的地址
STUFF_DIR_PATH_NO_SPIDER ="../data/dir"

#测试目录
#STUFF_DIR_PATH ="component/data/test"
#搜索查询条件配置文件
SEARCH_PARAM_FILE ="component/config/search_cond.conf"
#SEARCH_PARAM_FILE ="component/config/test.conf"


#抓取目录关键字 可以是一个也可以是多个 如 手机配件，手机
# 已经抓取过的目录 个护化妆 手机 手机配件 住宅家具 健身 内衣家居服 办公设备 厨具 家庭清洁工具 数码相机 尿片洗护 智能设备 服饰内衣 武术
# 汽车用品 玩具童车益智 球 瑜伽 生活电器 电子词典  电脑办公 箱包 茶 运动休闲服装 运动鞋 隐形眼镜护理 饰品流行首饰 童装婴儿装亲子装01

SEARCH_DIR_KW ="运动鞋,箱包"

#查询抓取的最大页数
SEARCH_MAX_PAGE ="6"

#最低销量
SELL_MIN_NUMBER="2"

#产品推广有效期的结束日期ß
VARIABLE_END_DATE ="2017-08-30"

#最低佣金
PROMTION_RATE="1"

#过滤类型 销量 佣金比例 sell_number,ratio,end_date
FILTER_TYPE ="sell_number"

#项目当前所处的模式 开发dev 预发布pre 生产prod
PROJECT_MODE_TYPE = "dev"

#读取查询条件的层级 一级one 二级second 三级third 整体 all
SWITCH_DIR_CLASS ="one"

#保存京东每个关键字对应的品牌目录
JD_BRAND_PATH ="component/data/brand"

#京东产品关键字对应的商品id
JD_ID_PATH ="component/data/id"

#京东联盟后台登陆账号和密码
JD_USER_NAME ="18602507935"
JD_PASS_WORD="aa11ss33"

#淘宝商品200的写入地址
TAOBAO_ID_PATH ="component/data/200/id"
TAOBAO_ID_PATH_NO_SPIDER ="../data/200/id"
#选品库对应的组ID
TAOBAO_GROUP_ID_PATH ="component/data/200/group"
TAOBAO_GROUP_ID_PATH_NO_SPIDER="../data/200/group"
#批量excel写入路径
TAOBAO_EXCEL_PATH ="component/data/200/xls"
TAOBAO_EXCEL_PATH_NO_SPIDER ="../data/200/xls"
#关键字匹配后缀
KEY_WORD_SUFFIEX ="|男|秋季"
# on|off
KEY_WORD_PATTERN_SWITCH ="off"