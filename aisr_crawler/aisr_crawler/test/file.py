# this is use python script!
# -*- coding: UTF-8 -*-
import os
import os.path
#小米 红米Note4 全网通版 3GB+32GB 金色 移动联通电信4G手机
#
# dirname ='球'
# one_clas ='球'
# two_class ='球类'
# dir_values='篮球,足球,排球,网球,羽毛球,高尔夫,棒球'
#
# file_path ='../config/data/'+dirname+'.txt'
#
# values = dir_values.split(",")
#
# for value in values:
#     with open (file_path,'a',encoding='utf-8') as file:
#         file.write(one_clas+"_"+two_class+"_"+value + '\n')
# print(one_clas+'目录生产完毕')

file_list = []
# rootdir = "aisr_crawler/config/data"
rootdir = "../config/data/手机/"
for parent, dirnames, filenames in os.walk(rootdir):
    for filename in filenames:
    #     fs = filename.split("_")
    #     fname = fs[0]
    #     if (keyword == fname):
    #         file_list.append(filename)
    # return file_list
        fs = filename.split("_")
        #print(filename)
        #print('split',fs[0],fs[1],fs[2])
        #print(fs[0]+"_"+fs[1]+"_"+fs[2])
        #print(filename)
        print(filename[:-7])