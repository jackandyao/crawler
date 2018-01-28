# this is use python script!
# -*- coding: UTF-8 -*-
from urllib import request
from urllib import error
from urllib import parse
from http import cookiejar
from bs4 import BeautifulSoup
from aisr_crawler.test.red import JDRedirectHandler
login_url = 'https://passport.jd.com/uc/loginService'
date_url = 'https://media.jd.com/gotoadv/goods?pageSize=50'  # 利用cookie请求访问另一个网址
#登陆Form_Data信息
Login_Data = {}
Login_Data['loginname'] = '18602507935'
Login_Data['nloginpwd'] = 'aa11ss33'
Login_Data['ReturnUrl'] = 'https://media.jd.com/gotoadv/goods?pageSize=50'
#使用urlencode方法转换标准格式
logingpostdata = parse.urlencode(Login_Data).encode('utf-8')

head = {
"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
"Accept-Encoding":"utf-8",
"Accept-Language":"zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3",
"Connection":"keep-alive",
"Host":"www.media.jd.com",
"Referer":"http://c.highpin.cn/",
"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:32.0) Gecko/20100101 Firefox/32.0"
}

#声明一个CookieJar对象实例来保存cookie
cookie = cookiejar.CookieJar()
#利用urllib.request库的HTTPCookieProcessor对象来创建cookie处理器,也就CookieHandler
cookie_support = request.HTTPCookieProcessor(cookie)
#通过CookieHandler创建opener
opener = request.build_opener(cookie_support)

#创建Request对象
req1 = request.Request(url=login_url, data=logingpostdata, headers=head)
req2 = request.Request(url=date_url, headers=head)

try:
    print('进入try')
    # 使用自己创建的opener的open方法
    response1 = opener.open(req1)
    print('r1')
    header = response1.headers
    print('header', header)
    print("login",response1.read().decode('utf-8'))
    response2 = opener.open(req2)
    header = response2.headers
    print('header',header)
    body = response2.read().decode('utf-8')

    # 打印查询结果
    print("body",body)

except error.URLError as e:
    if hasattr(e, 'code'):
        print("HTTPError:%d" % e.code)
        print(e)
    elif hasattr(e, 'reason'):
        print("URLError:%s" % e.reason)

