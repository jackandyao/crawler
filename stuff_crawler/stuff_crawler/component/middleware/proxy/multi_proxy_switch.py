# this is use python script!
# -*- coding: UTF-8 -*-
import random
import time
from scrapy.conf import settings

#通过读取指定代理IP的配置文件获取代理IP
class SpiderMultiProxyMiddleWare(object):

	def process_request(self,request, spider):
		proxy = self.get_random_proxy()
		print("this is request ip:"+proxy)
		request.meta['proxy'] = proxy


	def process_response(self, request, response, spider):

		# 如果返回的response状态不是200，重新生成当前request对象
		if response.status != 200:
			proxy = self.get_random_proxy()
			print("this is response ip:"+proxy)
			# 对当前reque加上代理
			request.meta['proxy'] = proxy
			return request
		return response

	def get_random_proxy(self):
		file_path = settings['IP_FILE_PATH']
		while 1:
			with open(file_path, 'r') as f:
				proxies = f.readlines()
			if proxies:
				break
			else:
				time.sleep(1)
		proxy = random.choice(proxies).strip()
		return proxy