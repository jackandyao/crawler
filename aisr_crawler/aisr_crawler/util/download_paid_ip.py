# this is use python script!
# -*- coding: UTF-8 -*-
#下载大象代理可用的IP 并写入到指定的文件中
import urllib.request
req= urllib.request.Request("http://tvp.daxiangdaili.com/ip/?tid=559873152815618&num=2&operator=1&protocol=https&foreign=only&filter=on")
resp= urllib.request.urlopen(req)
result = resp.read()
with open('../config/paid_agent_ip.txt', 'a') as f:
    f.write(str("https://"+result))
#b'103.56.207.206:8080\r\n68.128.212.240:8080' 需要解析