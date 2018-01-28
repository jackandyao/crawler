# this is use python script!
# -*- coding: UTF-8 -*-

#提供封装各个平台抓取数据的参数条件
import urllib,json
from scrapy.conf import settings
from component.util.config_util import ConfigUtil as conf

search_type = settings['SEARCH_TYPE']
search_param_file = settings['SEARCH_PARAM_FILE']
clazz = settings['SWITCH_DIR_CLASS']

#封装共用的查询条件
class CommonParamUtil:

    #查询关键件
    def getSearchKWList(self,search_dir_kw,setpath):
        dir_name = search_dir_kw
        objlist = []

        if "," in dir_name:
            dirs = dir_name.split(",")
            for dir in dirs:
                fileName = dir
                self.__readKeyFromFile(fileName, objlist,setpath)
        else:
            fileName = dir_name
            self.__readKeyFromFile(fileName, objlist,setpath)

        return objlist

    # 从配置文件读取
    def __readKeyFromFile(self, fileName, objlist,setpath):
        fileName = fileName + ".txt"
        fullPath = setpath + "/" + fileName
        f = open(fullPath, "r", encoding='UTF-8')
        lines = f.readlines()  # 读取全部内容
        for line in lines:
            objlist.append(line.strip())


    # 获取真实要抓取的关键字和对应的抓取满足页数
    def getKeywordAndPageNumber(self, cat_name_obj):
        # cat_name_obj:苹果手机&{"startTkRate": "0.1", "startBiz30day": "3", "startPrice": "2000", "sortType": "9", "endPrice": "10000"}$1
        # cat_name_obj:手机配件_手机配件_手机移动电源&{"startTkRate": "10", "startBiz30day": "30", "startPrice": "10", "sortType": "9", "endPrice": "1000"}
        param = {}
        # 需要切割真实满足要求的页数
        if "$" in cat_name_obj:
            obj = cat_name_obj.split("$")
            page = obj[1]
            kp = obj[0]
            kps = kp.split("&")
            keyword = kps[0]
            keyparam = kps[1]
        else:
            kps = cat_name_obj.split("&")
            keyword = kps[0]
            keyparam = kps[1]
            page = -1

        param['page'] = page
        param['param'] = keyparam
        param['keyword'] = keyword

        return param

    # 封装不同业务类型所请求的URL
    def getHttpUrlByType(self):
        urldic = {
            "all": "http://pub.alimama.com/items/search.json"
            , "nine": "http://pub.alimama.com/items/channel/9k9.json"
            , "twent": "http://pub.alimama.com/items/channel/20k.json"
            ,"jd_brand":"https://search.jd.com/Search"
        }
        return urldic[search_type]

#淘宝查询条件封装
class TaoBaoUtil(CommonParamUtil):

    #查询某个目录下面的所有关键字
    def getSearchKeyWordList(self, search_dir_kw,setpath):
        return super(TaoBaoUtil,self).getSearchKWList(search_dir_kw,setpath)

    #通过读取参数配置文件来生成查询条件
    def __createSearchCondition(self,selection):
        print('selection_value',selection,conf(search_param_file).getValue(selection,"startPrice"))
        return conf(search_param_file).readConf(selection)

    #添加其他额外查询条件
    def __combineExtralCondtion(self,values):
        type = search_type

        # 基于全站根据关键字查询
        if (type == 'all'):
            #只查询天猫
            # values['shopTag'] = "b2c,yxjh"
            values['shopTag'] = "yxjh"

        # 基于全球购搜索
        if (type == 'qqg'):
            values['typeTag'] = 'qqg'
            # values['shopTag'] = "b2c,yxjh"
            values['shopTag'] = "yxjh"

        # 基于9.9根据关键字查询
        if (type == 'nine'):
            values['catIds'] = 1
            values['channel'] = '9k9'
            values['level'] = "1"

        # 基于20根据关键字查询
        if (type == 'twent'):
            values['catIds'] = 1
            values['channel'] = '20k'
            values['level'] = "1"

        return values

    #使用单一查询条件
    def __createHttpParamBySingleConditon(self,keyWord,conditon):
        # print('single condtion....',keyWord,conditon)
        values = json.loads(conditon)
        values['perPageSize'] = "40"
        values['q'] = keyWord
        values = self.__combineExtralCondtion(values)
        return urllib.parse.urlencode(values)

    #使用统一配置文件
    def __createHttpParmByConfigFile(self,keyWord,cat_path):
        values = self.__createSearchCondition(cat_path)
        values['perPageSize'] = "40"
        values['q'] = keyWord
        values = self.__combineExtralCondtion(values)
        return urllib.parse.urlencode(values)


    #匹配关键字后缀
    def __andKeywordSuffiex(self,keyword):
        if (settings['KEY_WORD_PATTERN_SWITCH']=='on'):
            suffix = settings['KEY_WORD_SUFFIEX']
        else:
            suffix = ""

        return keyword +suffix
    # 根据请求的参数类型不同,创建不同的http请求连接参数'
    def __createHttpParam(self,keyWord,condition,cat_path):
        keyWord = self.__andKeywordSuffiex(keyWord)
        print('增加后缀之后的关键字..',keyWord)
        #从配置文件读取
        if (condition ==""):
            return self.__createHttpParmByConfigFile(keyWord,cat_path)
        #从关键字后面读取
        if (condition !=""):
            return self.__createHttpParamBySingleConditon(keyWord,condition)

    #匹配返回的查询条件
    def __switchHttpParam(self,search_condition,kw,cat_path):
        if (search_condition ==""):
            return self.__createHttpParam(kw,"",cat_path)
        else:
            return self.__createHttpParam(kw,search_condition,"")

    #切割字符串 根据目录级别
    def __splitStr(self,str):
        if "%" in str:
            param = str.split("%")
            cls = param[1]
            dir = param[0]
        else:
            cls = clazz
            dir = str
        return self.__getDirByCls(cls,dir)


    def __getDirByCls(self,cls,dir):
        strs = dir.split("_")
        if (cls == "one"):
            return strs[0]
        elif (cls == "second" or cls =="two"):
            return strs[0]+"_"+strs[1]
        elif (cls == "third"):
            return strs[0]+"_"+strs[1]+"_"+strs[2]
        elif (cls == "all"):
            return strs[0]
        else:
            return dir

    #初始化查询条件
    def initSearchCondtion(self,key):

        search_cond ={}
        if (key == ""):
            print("对不起没有需要抓取的关键字")
        else:
            # 针对每个关键字都有对应的查询条件
            if "&" in key:
                cat_path = key.split("&")[0]
                dir_name_obj = cat_path
                cat_name_obj = key[key.rfind("_") + 1:]
                param = super(TaoBaoUtil,self).getKeywordAndPageNumber(cat_name_obj)
                cat_name = param['keyword']
                search_condition = param['param']
                real_page = param['page']
                # print('每个关键字-实际参数', cat_path, cat_name, search_condition, real_page)

            # 从统一的配置文件读取
            else:
                #从指定的配置文件读取具体抓取条件
                if "%" in key:
                    real_page = -1
                    search_condition = ""
                    dir_name_obj = key
                    obj = key.split("%")
                    key = obj[0]
                    cat_name = key[key.rfind("_") + 1:]
                    cat_path = key
                    # print('统一关键字-实际参数', cat_path, cat_name)
                else:
                    cat_path = key.split("&")[0]
                    cat_name = key[key.rfind("_") + 1:]
                    dir_name_obj = cat_path
                    real_page = -1
                    search_condition = ""
                    # print('统一关键字-实际参数', cat_path, cat_name)

            http_url = super(TaoBaoUtil,self).getHttpUrlByType()
            selection = self.__splitStr(dir_name_obj)
            #print('selection',selection)
            data = self.__switchHttpParam(search_condition,cat_name,selection)
            # print('data',data)
            search_url = http_url + "?" + data

            search_cond['cat_name'] =cat_name
            search_cond['cat_path'] =cat_path
            search_cond['real_page'] =real_page
            search_cond['search_url'] =search_url

            return search_cond

#封装JD
class JDUtil(CommonParamUtil):

    # 查询某个目录下面的所有关键字
    def getSearchKeyWordList(self, search_dir_kw,setpath):
        return super(JDUtil,self).getSearchKWList(search_dir_kw,setpath)

    #切割获取对应的具体查询关键字
    def getSearchKeyWord(self,key):
        search_cond = {}
        if (key == ""):
            print("对不起没有需要抓取的关键字")
        else:
            # 针对每个关键字都有对应的查询条件
            if "&" in key:
                cat_path = key.split("&")[0]
                cat_name_obj = key[key.rfind("_") + 1:]
                param = super(JDUtil,self).getKeywordAndPageNumber(cat_name_obj)
                cat_name = param['keyword']

            # 从统一的配置文件读取
            else:
                # 从指定的配置文件读取具体抓取条件
                if "%" in key:
                    obj = key.split("%")
                    cat_path = obj[0]
                    cat_name = obj[0][obj[0].rfind("_") + 1:]
                else:
                    cat_path = key.split("&")[0]
                    cat_name = key[key.rfind("_") + 1:]

            search_cond['cat_name'] = cat_name
            search_cond['cat_path'] = cat_path
            return search_cond
#条件工厂
class ConditionFactory:
    CONDITION_TYPE_TB ="TB"
    CONDITION_TYPE_JD = "JD"

    def getCondtionInstance(self,type):
        if (type == self.CONDITION_TYPE_TB):
            return TaoBaoUtil
        elif (type == self.CONDITION_TYPE_JD):
            return JDUtil
        else:
            return None


#if __name__ == '__main__':
