# this is use python script!
# -*- coding: UTF-8 -*-
import urllib.request
from bs4 import BeautifulSoup
import lxml
from multiprocessing import Process, Queue
import random
import requests
#操作IP工具类
class IPUtil:

    #下载收费的IP
    def downloadPaidIp(self):
        req = urllib.request.Request(
            "http://tvp.daxiangdaili.com/ip/?tid=559873152815618&num=2&operator=1&protocol=https&foreign=only&filter=on")
        resp = urllib.request.urlopen(req)
        result = resp.read()
        with open('../config/paid_agent_ip.txt', 'a') as f:
            f.write(str("https://" + result))

    #免费IP
    def __init__(self, page=3):
        self.proxies = []
        self.verify_pro = []
        self.page = page
        self.headers = {
        'Accept': '*/*',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8'
        }
        self.get_proxies()
        self.get_proxies_nn()

    #获取所有的代理IP
    def get_proxies(self):
        page = random.randint(1,10)
        page_stop = page + self.page
        while page < page_stop:
            url = 'http://www.xicidaili.com/nt/%d' % page
            html = requests.get(url, headers=self.headers).content
            soup = BeautifulSoup(html, 'lxml')
            ip_list = soup.find(id='ip_list')
            for odd in ip_list.find_all(class_='odd'):
                protocol = odd.find_all('td')[5].get_text().lower()+'://'
                self.proxies.append(protocol + ':'.join([x.get_text() for x in odd.find_all('td')[1:3]]))
            page += 1

    def get_proxies_nn(self):
        page = random.randint(1,10)
        page_stop = page + self.page
        while page < page_stop:
            url = 'http://www.xicidaili.com/nn/%d' % page
            html = requests.get(url, headers=self.headers).content
            soup = BeautifulSoup(html, 'lxml')
            ip_list = soup.find(id='ip_list')
            for odd in ip_list.find_all(class_='odd'):
                protocol = odd.find_all('td')[5].get_text().lower() + '://'
                self.proxies.append(protocol + ':'.join([x.get_text() for x in odd.find_all('td')[1:3]]))
            page += 1

    #验证代理IP
    def verify_proxies(self):
        # 没验证的代理
        old_queue = Queue()
        # 验证后的代理
        new_queue = Queue()
        print ('verify proxy........')
        works = []
        for _ in range(15):
            works.append(Process(target=self.verify_one_proxy, args=(old_queue,new_queue)))
        for work in works:
            work.start()
        for proxy in self.proxies:
            old_queue.put(proxy)
        for work in works:
            old_queue.put(0)
        for work in works:
            work.join()
        self.proxies = []
        while 1:
            try:
                self.proxies.append(new_queue.get(timeout=1))
            except:
                break
        print ('verify_proxies done!')


    #具体实现验证代理IP的方法
    def verify_one_proxy(self, old_queue, new_queue):
        while 1:
            proxy = old_queue.get()
            if proxy == 0:break
            protocol = 'https' if 'https' in proxy else 'http'
            proxies = {protocol: proxy}
            try:
                if requests.get('http://www.baidu.com', proxies=proxies, timeout=2).status_code == 200:
                    print('success %s' % proxy)
                    new_queue.put(proxy)
            except:
                print ('fail %s' % proxy)

    #验证IP是否可以正常使用
    def validationIp(self):
        try:
            requests.get('http://wenshu.court.gov.cn/', proxies={"https": "https://117.91.138.131:808"})
        except:
            print('connect failed')
        else:
            print('success')