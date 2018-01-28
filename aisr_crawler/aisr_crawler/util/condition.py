# this is use python script!
# -*- coding: UTF-8 -*-

#创造查询条件-淘宝
class CreateCondition():

    #通过读取参数配置文件来生成查询条件
    def createSearchCondition(file):
        try:
            data = open(file,encoding='UTF-8')
            p = {}
            for f in data:
                params = f.split(":")
                key = params[0].strip()
                value = params[1].strip()
                p[key] = value
            return p

        except IOError as err:
            print('File Error:' + str(err))
        finally:
            if 'data' in locals():
                data.close()
if __name__ == "__main__":
    print(CreateCondition.createSearchCondition("../config/taobao_param.txt"))