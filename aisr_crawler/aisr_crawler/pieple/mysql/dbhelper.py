# this is use python script!
# -*- coding: UTF-8 -*-
import pymysql
from scrapy.utils.project import get_project_settings

#连接DB数据库的工具类
class DBHelper:

    #初始化数据
    def __init__(self):
        self.settings = get_project_settings()  # 获取settings配置，设置需要的信息
        self.host = self.settings['MYSQL_HOST']
        self.port = self.settings['MYSQL_PORT']
        self.user = self.settings['MYSQL_USER']
        self.passwd = self.settings['MYSQL_PASSWD']
        self.db = self.settings['MYSQL_DBNAME']

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