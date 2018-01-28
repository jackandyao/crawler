# this is use python script!
# -*- coding: UTF-8 -*-
import requests

try:
    requests.get('http://wenshu.court.gov.cn/', proxies={"https":"https://117.91.138.131:808"})
except:
    print ('connect failed')
else:
    print ('success')