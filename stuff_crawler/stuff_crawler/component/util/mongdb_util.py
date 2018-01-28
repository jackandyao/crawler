import pymongo
from pymongo import MongoClient
from component.util.param_util import ConditionFactory as cf
from scrapy.conf import settings
class MongodUtil:

    def __init__(self):

        host = "192.168.14.107"
        port = 27017
        db = "stuff_spider"
        coll = "stuff_autumn"

        client = MongoClient(host=host, port=port)
        db = client.get_database(db)
        self.coll = db.get_collection(coll)

    #计算最大页数
    def __getTotalPages(self,totalcount,pagesize):
        totalpage = totalcount / pagesize if totalcount % pagesize == 0 else int(totalcount / pagesize) + 1
        return totalpage

    #查询数据 区分来源
    def getTbIdByStuffCatPathAndSource(self,stuff_cat_path,source,dir_name):
        if (source =='pc'):
            id_item = self.coll.find({"stuff_cat_path": stuff_cat_path},{"stuff_real_id": 1, "stuff_order_num": 1}).limit(200)
        else:
            id_item = self.coll.find({"stuff_cat_path": stuff_cat_path, "stuff_source": source},{"stuff_real_id": 1, "stuff_order_num": 1}).limit(200)

        if (id_item != None):
            id_list = []
            for id in id_item:
                spu_id = id['stuff_real_id']
                order_num = id['stuff_order_num']
                if (int(order_num) > 1):
                    id_list.append(str(spu_id))
            str_list = ",".join(id_list)
            if (len(str_list) > 0):
                content = str(stuff_cat_path).replace("/", "|") + "_" + source + ":" + str_list
                self.writeIDToFile(self.getFileName(dir_name, source), content)
            else:
                print("对不起根据关键字:[" + stuff_cat_path + "]" + "没有查询到结果...")

        else:
            print("对不起根据关键字:[" + stuff_cat_path + "]" + "没有查询到结果...")


                # id_item_count = self.coll.find({"stuff_cat_path":stuff_cat_path,"stuff_source":source}, {"stuff_real_id": 1,"stuff_order_num":1}).count()
        # totalpage = self.__getTotalPages(id_item_count,200)
        # pagesize = 200
        # num = 1
        # while num <= totalpage:
        #     id_item = self.coll.find({"stuff_cat_path":stuff_cat_path,"stuff_source":source}, {"stuff_real_id": 1,"stuff_order_num":1}).skip((num-1)*pagesize).limit(pagesize)
        #     if (id_item !=None):
        #         id_list =[]
        #         for id in id_item:
        #             spu_id = id['stuff_real_id']
        #             order_num =id['stuff_order_num']
        #             if (int(order_num)>1):
        #                 id_list.append(str(spu_id))
        #         str_list =",".join(id_list)
        #         if (len(str_list)>0):
        #             content = str(stuff_cat_path).replace("/","|")+"_"+source +":" + str_list
        #             self.writeIDToFile(self.getFileName(dir_name+str(num),source),content)
        #         else:
        #             print("对不起根据关键字:[" + stuff_cat_path + "]" + "没有查询到结果...")
        #
        #     else:
        #         print("对不起根据关键字:["+stuff_cat_path+"]"+"没有查询到结果...")
        #     num += 1


    #写入文件
    def getFileName(self,name,source):
       idfile = settings['TAOBAO_ID_PATH_NO_SPIDER']
       return idfile +"/" + name +".txt"

    #把要待转链接的ID存入到文件里面
    def writeIDToFile(self,idfile,content):
      with open(idfile, 'a') as f:
          f.write(content + '\n')

if __name__ == "__main__":
    sources = ["taobao", "tmall"]
    # sources = ["pc"]
    dir_name_str = "运动鞋,箱包"
    dirs = dir_name_str.split(",")
    for dir_name in dirs:
        jdInstance = cf().getCondtionInstance("JD")()
        setpath =settings['STUFF_DIR_PATH_NO_SPIDER']
        keywords = jdInstance.getSearchKeyWordList(dir_name,setpath)
        for key in keywords:
            obj = jdInstance.getSearchKeyWord(key)
            cat_name = obj['cat_name']
            cat_path = obj['cat_path']
            #遍历来源
            for source in sources:
                MongodUtil().getTbIdByStuffCatPathAndSource(cat_path,source,dir_name)
                print(cat_path+",查询完毕...")
        print("目录{"+dir_name+"}"+",查询完毕...")




