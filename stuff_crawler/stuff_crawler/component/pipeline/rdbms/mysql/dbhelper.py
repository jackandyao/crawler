# this is use python script!
# -*- coding: UTF-8 -*-
import pymysql
from scrapy.conf import settings
from component.util.config_util import ConfigUtil as conf
#连接DB数据库的工具类
class DBHelper:

    #初始化数据
    def __init__(self):
        #因为python自带的解析配置文件中 对于value中包含%这种字符串的 存在识别问题
        #file = settings['MYSQL_CONF_FILE']
        #selection = "mysql_" + settings['PROJECT_MODE_TYPE']
        #self.host = conf(file).getValue(selection,'MYSQL_HOST')
        #self.port = conf(file).getValue(selection,'MYSQL_PORT')
        #self.user =conf(file).getValue(selection,'MYSQL_USER')
        #self.passwd = conf(file).getValue(selection,'MYSQL_PASSWD')
        #self.db = self.conf(file).getValue(selection,'MYSQL_DBNAME')
        #print('mysql info...',file,selection,self.host,self.port,self.user,self.passwd,self.db)

        self.host = settings['MYSQL_HOST']
        self.port = settings['MYSQL_PORT']
        self.user = settings['MYSQL_USER']
        self.passwd = settings['MYSQL_PASSWD']
        self.db = settings['MYSQL_DBNAME']
    # 连接到mysql，不是连接到具体的数据库
    def connectMysql(self):
        conn = pymysql.connect(host=self.host,
                               port=self.port,
                               user=self.user,
                               passwd=self.passwd,
                               # db=self.db,不指定数据库名
                               charset='utf8')  # 要指定编码，否则中文可能乱码
        return conn

    # 连接到具体的数据库（settings中设置的MYSQL_DBNAME）
    def connectDatabase(self):
        conn = self.mysqldb.connect(host=self.host,
                               port=self.port,
                               user=self.user,
                               passwd=self.passwd,
                               db=self.db,
                               charset='utf8')  # 要指定编码，否则中文可能乱码
        return conn

    # 创建数据库
    def createDatabase(self):
        conn = self.connectMysql()  # 连接数据库
        sql = "create database if not exists " + self.db
        cur = conn.cursor()
        cur.execute(sql)  # 执行sql语句
        cur.close()
        conn.close()

    # 创建表
    def createTable(self, sql):
        conn = self.connectDatabase()
        cur = conn.cursor()
        cur.execute(sql)
        cur.close()
        conn.close()
        # 插入数据

    #插入操作 注意这里params要加*,因为传递过来的是元组，*表示参数个数不定
    def insert(self, sql, *params):
        conn = self.connectDatabase()
        cur = conn.cursor();
        cur.execute(sql, params)
        conn.commit()
        cur.close()
        conn.close()

    # 更新数据
    def update(self, sql, *params):
        conn = self.connectDatabase()

        cur = conn.cursor()
        cur.execute(sql, params)
        conn.commit()  # 注意要commit
        cur.close()
        conn.close()

    # 删除数据
    def delete(self, sql, *params):
        conn = self.connectDatabase()
        cur = conn.cursor()
        cur.execute(sql, params)
        conn.commit()
        cur.close()
        conn.close()