# this is use python script!
# -*- coding: UTF-8 -*-
import random
from dmbj.settings import IPPOOL
#实现IP代理池
class DmbjSpiderHttpProxyMiddleware(object):
    def __init__(self, ip=''):
        self.ip = ip

    def process_request(self, request, spider):
        proxy_ip = random.choice(IPPOOL)
        print("proxy_ip:" + proxy_ip["ip_addr"])
        request.meta["proxy"] = "http://" + proxy_ip["ip_addr"]