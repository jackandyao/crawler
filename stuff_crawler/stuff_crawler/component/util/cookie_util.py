# this is use python script!
# -*- coding: UTF-8 -*-

#把浏览器里面用户登录的原始cookie信息转换成scrapy能识别数据格式
class CookieJar:
    def getCookie(cookie):
        itemDict = {}
        items = cookie.split(';')
        for item in items:
            key = item.split('=')[0].replace(' ', '')
            value = item.split('=')[1]
            itemDict[key] = value
        return itemDict

if __name__ == "__main__":
    ck = 't=dc43f2e577337a76d7551feec8e30576; undefined_yxjh-filter-1=true; cookie2=4ef52244eb6263beaced7a66a5b256ce; _tb_token_=VdRMmDGzzwq; v=0; 106306839_yxjh-filter-1=true; cookie32=81b561b6a0fb8066f009f61b2d113974; cookie31=MTA2MzA2ODM5LHRiOTkzMzU3ODAsNzg2NjQ4NjQzQHFxLmNvbSxUQg%3D%3D; alimamapwag=TW96aWxsYS81LjAgKE1hY2ludG9zaDsgSW50ZWwgTWFjIE9TIFggMTBfMTJfNSkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzYwLjAuMzExMi4xMTMgU2FmYXJpLzUzNy4zNg%3D%3D; login=WqG3DMC9VAQiUQ%3D%3D; alimamapw=TVIPCFVSVAcPCTkCBAVXBFYPDgBUBFFYU1NRCVMBBlJQUAYPCFYCAAIEAw%3D%3D; taokeisb2c=; rurl=aHR0cDovL3B1Yi5hbGltYW1hLmNvbS8%2Fc3BtPWEyMWFuLjc2NzYwMDcuYTIxNHRyOC4xNi42MDM0NTMwNnRTeXdTVg%3D%3D; apushf4f28b675ff5e94dc07d6a8cd29d040c=%7B%22ts%22%3A1503972858529%2C%22parentId%22%3A1503972846483%7D; cna=mBwcEl+tJCwCAWfyqKcW/U8I; isg=Au7uNO50O3052E8oKPWT7eqbP0K6Q6wHud4BBRi3PPG0-49VgH5M-cQ9xVHs'
    print(CookieJar.getCookie(ck))