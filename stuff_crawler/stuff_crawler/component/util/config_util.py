import configparser

#读取配置
class ConfigUtil:

    def __init__(self,file):
        self.parser = configparser.ConfigParser()
        self.content = self.parser.read(file)

    #读取配置文件 把所有的键值对转换为json格式数据
    def readConf(self,section):
        p = {}
        content = self.content
        if len(content)<1:
            print("配置文件内容为空,请填充配置文件的内容")
        else:
            #重新获取
            p['startPrice'] =self.parser.get(section,"startPrice")
            p['endPrice'] = self.parser.get(section,"endPrice")
            p['sortType']=9
            p['startBiz30day'] =self.parser.get(section,"startBiz30day")
            p['startTkRate'] = self.parser.getfloat(section,"startTkRate")
            # p['b2c'] = self.parser.get(section, "b2c")
        # print('config param',p)
        return p



    #从配置文件获取指定的key对应的值
    def getValue(self,selection,key):
        value = self.parser.get(selection,key)
        return value

    def getIntValue(self,selection,key):
        return self.parser.getint(selection,key)

    def getFloatValue(self,selection,key):
        return self.parser.getfloat(selection,key)

    def getBooleanValue(self,selection,key):
        return self.parser.getboolean(selection,key)