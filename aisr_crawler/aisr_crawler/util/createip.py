# this is use python script!
# -*- coding: UTF-8 -*-
if __name__ == '__main__':
    file ='../config/ip.txt'
    for line in open(file,encoding="utf-8"):
        wf = open('../config/paid_agent_ip.txt','a')
        wf.write("https://"+line +"\n")
    print('文件写入成功')