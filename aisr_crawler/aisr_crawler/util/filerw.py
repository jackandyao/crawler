# this is use python script!
# -*- coding: UTF-8 -*-
import logging
import os
import os.path
#处理关键字的文件读写
class FileHandle():


    # 读取抓取文件类目
    def getKeyWord(file):
        keyword_list = []
        f = open(file, "r", encoding='UTF-8')
        lines = f.readlines()  # 读取全部内容
        for line in lines:
            keywords = line.split("  ")
            for key in keywords:
                keyword_list.append(key.strip())
        return keyword_list;

    # 读取每个关键字所对应的目录
    def getKeyWordJson(file):
        keyword_list = []
        f = open(file, "r", encoding='UTF-8')
        lines = f.readlines()  # 读取全部内容
        obj = {}
        for line in lines:
            keywords = line.split(":")
            obj['key'] = keywords[0]
            obj['catId'] = keywords[1]
        return obj;

    #从配置文件读取多行关键字
    def getTBKeyWordJson(file):
        keyword_list = []
        f = open(file, "r", encoding='UTF-8')
        lines = f.readlines()  # 读取全部内容

        for line in lines:
            obj = {}
            keywords = line.split("_")
            obj['key'] = keywords[2].strip()
            obj['catName'] = line.strip()
            keyword_list.append(obj)
        return keyword_list



    #通过关键字匹配待抓取文件目录
    @staticmethod
    def getFileName(keyword):
        file_list = []
        rootdir = "aisr_crawler/config/data"
        #rootdir = "../data"
        for parent, dirnames, filenames in os.walk(rootdir):
            for filename in filenames:
                fs = filename.split("_")
                fname = fs[0]
                if(keyword == fname):
                    file_list.append(filename)
            return file_list

    #通过获取待抓取文件的所有ID
    def getIDListByFile(self,keyword):
        root = "aisr_crawler/config/data/"
        #root = "../data/"
        fs = self.getFileName(keyword)
        id_list = []
        for file in fs:
            print(file)
            for id in open(root+file,encoding='utf-8'):
                file_obj = {}
                file_obj['file'] = file
                file_obj['id']=id.strip()
                id_list.append(file_obj)
        return id_list

if __name__ == '__main__':
    fw = FileHandle()
    fs =fw.getIDListByFile('手机')
    for f in fs:
        print(f)
