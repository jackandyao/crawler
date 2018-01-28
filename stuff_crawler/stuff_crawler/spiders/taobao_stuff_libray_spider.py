from scrapy.spiders import CrawlSpider
import scrapy,time,sys,json
from component.util.param_util import ConditionFactory as cf
from scrapy.conf import settings
import random,urllib,requests,os
from component.util.system_util import SystemUtil as syst
from component.util.cookie_util import CookieJar as cj
#抓取淘宝商品库
class TaoBaoStuffLibraySpider(CrawlSpider):

    name ="taobaolibray"

    plat_form = syst().getPlatform()
    if (plat_form == "linux"):
        dir_name = sys.argv[0]
    else:
        dir_name = settings['SEARCH_DIR_KW']

    # 批量添加商品
    add_spu_url = "http://pub.alimama.com/favorites/item/batchAdd.json"

    # 创建选品库
    create_libray_url = "http://pub.alimama.com/favorites/group/save.json"

    # 批量导出excel
    export_spu_url = "http://pub.alimama.com/favorites/item/export.json"

    # 删除选品库
    del_libray_url = "http://pub.alimama.com/favorites/group/delete.json"

    # 选品库类型 普通和高佣
    libary_type =1

    # tb_token
    tb_token ="5xW5mnqhKyq"

    #商品导入平台类型
    spu_plat_form =["ios","and"]

    # ck = 't=dc43f2e577337a76d7551feec8e30576; undefined_yxjh-filter-1=true; cookie2=4ef52244eb6263beaced7a66a5b256ce; _tb_token_=VdRMmDGzzwq; v=0; 106306839_yxjh-filter-1=true; cookie32=81b561b6a0fb8066f009f61b2d113974; cookie31=MTA2MzA2ODM5LHRiOTkzMzU3ODAsNzg2NjQ4NjQzQHFxLmNvbSxUQg%3D%3D; alimamapwag=TW96aWxsYS81LjAgKE1hY2ludG9zaDsgSW50ZWwgTWFjIE9TIFggMTBfMTJfNSkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzYwLjAuMzExMi4xMTMgU2FmYXJpLzUzNy4zNg%3D%3D; login=WqG3DMC9VAQiUQ%3D%3D; alimamapw=TVIPCFVSVAcPCTkCBAVXBFYPDgBUBFFYU1NRCVMBBlJQUAYPCFYCAAIEAw%3D%3D; taokeisb2c=; rurl=aHR0cDovL3B1Yi5hbGltYW1hLmNvbS8%2Fc3BtPWEyMWFuLjc2NzYwMDcuYTIxNHRyOC4xNi42MDM0NTMwNnRTeXdTVg%3D%3D; apushf4f28b675ff5e94dc07d6a8cd29d040c=%7B%22ts%22%3A1503972858529%2C%22parentId%22%3A1503972846483%7D; cna=mBwcEl+tJCwCAWfyqKcW/U8I; isg=Au7uNO50O3052E8oKPWT7eqbP0K6Q6wHud4BBRi3PPG0-49VgH5M-cQ9xVHs'
    # ck ='t=dc43f2e577337a76d7551feec8e30576; undefined_yxjh-filter-1=true; 106306839_yxjh-filter-1=true; account-path-guide-s1=true; cookie2=0f02d660ece0e2f16e0ab22774390e8f; v=0; _tb_token_=5xW5mnqhKyq; taokeisb2c=; cookie32=81b561b6a0fb8066f009f61b2d113974; cookie31=MTA2MzA2ODM5LHRiOTkzMzU3ODAsNzg2NjQ4NjQzQHFxLmNvbSxUQg%3D%3D; alimamapwag=TW96aWxsYS81LjAgKE1hY2ludG9zaDsgSW50ZWwgTWFjIE9TIFggMTBfMTJfNSkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzYwLjAuMzExMi4xMTMgU2FmYXJpLzUzNy4zNg%3D%3D; login=W5iHLLyFOGW7aA%3D%3D; alimamapw=TVIPCFVSVAcPCTkCBAVXBFYPDgBUBFFYU1NRCVMBBlJQUAYPCFYCAAIEAw%3D%3D; rurl=aHR0cHM6Ly9wdWIuYWxpbWFtYS5jb20vP3NwbT1hMjMyMC43Mzg4NzgxLmNhMjE0dHI4LmQ5YmRhODdiYS42ZTM0YWRlNTBDMXl6NQ%3D%3D; cna=mBwcEl+tJCwCAWfyqKcW/U8I; apushf4f28b675ff5e94dc07d6a8cd29d040c=%7B%22ts%22%3A1504600338740%2C%22parentId%22%3A1504600308655%7D; isg=Ag8PRsx8iqiMq45vcZ6CIkPQnqUTmHywgOUAgiEdVn6T8CfyIwf0ps6mhBY1'
    ck ='t=dc43f2e577337a76d7551feec8e30576; undefined_yxjh-filter-1=true; 106306839_yxjh-filter-1=true; account-path-guide-s1=true; cookie2=0f02d660ece0e2f16e0ab22774390e8f; v=0; _tb_token_=5xW5mnqhKyq; taokeisb2c=; cookie32=81b561b6a0fb8066f009f61b2d113974; cookie31=MTA2MzA2ODM5LHRiOTkzMzU3ODAsNzg2NjQ4NjQzQHFxLmNvbSxUQg%3D%3D; alimamapwag=TW96aWxsYS81LjAgKE1hY2ludG9zaDsgSW50ZWwgTWFjIE9TIFggMTBfMTJfNSkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzYwLjAuMzExMi4xMTMgU2FmYXJpLzUzNy4zNg%3D%3D; login=VT5L2FSpMGV7TQ%3D%3D; alimamapw=TVIPCFVSVAcPCTkCBAVXBFYPDgBUBFFYU1NRCVMBBlJQUAYPCFYCAAIEAw%3D%3D; cna=mBwcEl+tJCwCAWfyqKcW/U8I; apushf4f28b675ff5e94dc07d6a8cd29d040c=%7B%22ts%22%3A1504604885791%2C%22parentId%22%3A1504604864725%7D; isg=AgAA-h6ATW1EizFSSlNlB2gV0YjYJfu1-wBfn3qQ-Juu9aofIpq94pGDe2vO'
    cookies = cj.getCookie(ck)

    post_headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Host" :"pub.alimama.com",
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
    }


    def start_requests(self):
        taobaoInstance = cf().getCondtionInstance("TB")()
        keywords = taobaoInstance.getSearchKeyWordList(self.dir_name,settings['TAOBAO_ID_PATH'])
        for key in keywords:
            ks = key.split(":")
            libray_name = ks[0]
            item_list = ks[1]
            time.sleep(random.randint(1, 3))
            data ={"groupTitle":libray_name,"groupType":str(self.libary_type),"_tb_token_":self.tb_token}
            # 模拟发送post请求格式数据
            yield scrapy.FormRequest(
                url=self.create_libray_url,
                cookies=self.cookies,
                formdata=data,
                headers=self.post_headers,
                meta={"libray_name":libray_name,"item_list":item_list},
                callback=self.add_spu_library
            )
            time.sleep(random.randint(1, 3))

    #创建商品选品库
    def add_spu_library(self,response):
        js = json.loads(response.body_as_unicode())
        falg = js['ok']
        libray_name = response.meta['libray_name']
        if (falg == True):
            item_list = response.meta['item_list']
            groupid = js['data']['data']
            # print(groupid,item_list)
            content = str(libray_name).replace("/", "|") + ":" + str(groupid)
            self.__writeIDToFile(settings['TAOBAO_GROUP_ID_PATH'] + "/" + self.dir_name + ".txt", content)
            print("选品库,[" + libray_name + "]" + "成功创建..")
            groupId = str(groupid)
            data = {"groupId": groupId, "itemListStr": item_list}
            # 模拟发送post请求格式数据
            yield scrapy.FormRequest(
                url=self.add_spu_url,
                cookies=self.cookies,
                meta={'groupid': groupid, 'libray_name': libray_name},
                formdata=data,
                headers=self.post_headers,
                callback=self.select_spu_library
            )
        else:
            print("选品库,[" + libray_name + "]" + "创建失败..",js)

    #生成导入的excel需要的参数
    def __getExportExcelParam(self, type, groupId):
        if (type == 'ios'):
            data = {"scenes": 1, "adzoneId": 76574177, "siteId": 23098705, "groupId": str(groupId)}
        elif (type == 'and'):
            data = {"scenes": 1, "adzoneId": 76562672, "siteId": 23088972, "groupId": str(groupId)}
        else:
            print('操作类型不能为空或者操作类型不正确..')
            data = {}
        # data = urllib.parse.urlencode(data)
        return data

    #把要待转链接的ID存入到文件里面  判断文件目录是否存在如果不存在 先创建
    def __writeIDToFile(self, idfile, content):
        with open(idfile, 'a') as f:
            f.write(content + '\n')

    # 生成excel文件命名
    def __generatorExcelName(self, groupTitle, type, source):
        dirs = groupTitle.split("_")
        return dirs[0] + "|" + dirs[1] + "|" + dirs[2] + "_" + "jiahongping" + "_" + source + "_" + type.upper()

    #选品库指定商品
    def select_spu_library(self,response):
        groupId = str(response.meta['groupid'])
        libray_name = response.meta['libray_name']
        js = json.loads(response.body_as_unicode())
        falg = js['ok']
        if (falg ==True):
            print("组," + str(groupId) + "添加商品成功")
            for type in self.spu_plat_form:
                data = self.__getExportExcelParam(type,groupId)
                data = urllib.parse.urlencode(data)
                yield scrapy.Request(
                    url=self.export_spu_url+"?"+data,
                    meta={'libray_name': libray_name, 'type': type,'groupId':groupId},
                    cookies=self.cookies,
                    callback=self.export_spu_library)

        else:
            print("组," + groupId + "添加商品失败",js)
    #导出选品库里面的商品
    def export_spu_library(self,response):
        libray_name = response.meta['libray_name']
        groupTitle = str(libray_name).replace("/", "|")
        type = response.meta['type']
        source = libray_name.split("_")[-1]

        if (response.status ==200):
            groupId = response.meta['groupId']
            dir_file =  settings['TAOBAO_EXCEL_PATH'] + "/" + self.dir_name
            if not os.path.exists(dir_file):
                os.mkdir(dir_file)
            excelfile = dir_file+ "/" + self.__generatorExcelName(groupTitle, type,source) + ".csv"

            resp = requests.get(response.url ,cookies=self.cookies,headers=self.post_headers)
            with open(excelfile, 'wb') as f:
                for chunk in resp.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
                        f.flush()
            print("文件" + groupTitle + "_" + source + "导出成功....")

            #删除选品库
            data = {"groupId": groupId, "_tb_token_": self.tb_token}
            # 模拟发送post请求格式数据
            yield scrapy.FormRequest(
                url=self.del_libray_url,
                cookies=self.cookies,
                meta={'groupid': groupId},
                formdata=data,
                headers=self.post_headers,
                callback=self.del_spu_library
            )
        else:
            print("文件" + groupTitle + "_" + source + "导出成功....")
    #删除已经导出商品的选品库
    def del_spu_library(self,response):
        groupId = response.meta['groupid']
        js = json.loads(response.body_as_unicode())
        falg = js['ok']
        if (falg == True):
            print("选品库ID," + groupId + "删除成功")
        else:
            print("选品库ID," + groupId + "删除失败",js)
