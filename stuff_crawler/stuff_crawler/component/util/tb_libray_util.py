import requests,os
import json,time,random
from component.util.cookie_util import CookieJar as cj
import urllib
from component.util.param_util import ConditionFactory as cf
from scrapy.conf import settings
class TBLibrayUtil:

    #批量添加商品
    batch_spu_url = "http://pub.alimama.com/favorites/item/batchAdd.json"

    #创建选品库
    create_libray_url ="http://pub.alimama.com/favorites/group/save.json"

    #批量导出excel
    batch_export_url ="http://pub.alimama.com/favorites/item/export.json"

    #删除选品库
    del_libray_url ="http://pub.alimama.com/favorites/group/delete.json"

    post_headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Host": "pub.alimama.com",
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
    }

    # ck ='t=dc43f2e577337a76d7551feec8e30576; undefined_yxjh-filter-1=true; 106306839_yxjh-filter-1=true; account-path-guide-s1=true; cookie2=0f02d660ece0e2f16e0ab22774390e8f; v=0; _tb_token_=UuQ4yzK8Ayq; cookie32=81b561b6a0fb8066f009f61b2d113974; cookie31=MTA2MzA2ODM5LHRiOTkzMzU3ODAsNzg2NjQ4NjQzQHFxLmNvbSxUQg%3D%3D; alimamapwag=TW96aWxsYS81LjAgKE1hY2ludG9zaDsgSW50ZWwgTWFjIE9TIFggMTBfMTJfNSkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzYwLjAuMzExMi4xMTMgU2FmYXJpLzUzNy4zNg%3D%3D; login=URm48syIIVrSKA%3D%3D; alimamapw=TVIPCFVSVAcPCTkCBAVXBFYPDgBUBFFYU1NRCVMBBlJQUAYPCFYCAAIEAw%3D%3D; isg=At_f4iUi-j2udv4fAY5ysvPAbjWp7DKAMPVQEnEsLA7eAP-CeRTDNl2QtKeE; cna=mBwcEl+tJCwCAWfyqKcW/U8I; apushf4f28b675ff5e94dc07d6a8cd29d040c=%7B%22ts%22%3A1504416702961%2C%22parentId%22%3A1504362497326%7D'
    #ck ='t=dc43f2e577337a76d7551feec8e30576; undefined_yxjh-filter-1=true; 106306839_yxjh-filter-1=true; account-path-guide-s1=true; cookie2=0f02d660ece0e2f16e0ab22774390e8f; v=0; _tb_token_=F4952KQSHyq; cookie32=81b561b6a0fb8066f009f61b2d113974; cookie31=MTA2MzA2ODM5LHRiOTkzMzU3ODAsNzg2NjQ4NjQzQHFxLmNvbSxUQg%3D%3D; alimamapwag=TW96aWxsYS81LjAgKE1hY2ludG9zaDsgSW50ZWwgTWFjIE9TIFggMTBfMTJfNSkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzYwLjAuMzExMi4xMTMgU2FmYXJpLzUzNy4zNg%3D%3D; login=V32FPkk%2Fw0dUvg%3D%3D; alimamapw=TVIPCFVSVAcPCTkCBAVXBFYPDgBUBFFYU1NRCVMBBlJQUAYPCFYCAAIEAw%3D%3D; isg=AnBwr_9H3di7w4HiemP1t3jlQTgCEVVlC_DPz2rBPEueJRDPEskkk8YVCxq_; apushf4f28b675ff5e94dc07d6a8cd29d040c=%7B%22ts%22%3A1504419150609%2C%22parentId%22%3A1504362497326%7D; cna=mBwcEl+tJCwCAWfyqKcW/U8I'

    # ck ='t=dc43f2e577337a76d7551feec8e30576; undefined_yxjh-filter-1=true; 106306839_yxjh-filter-1=true; account-path-guide-s1=true; cookie2=0f02d660ece0e2f16e0ab22774390e8f; v=0; _tb_token_=F4952KQSHyq; cookie32=81b561b6a0fb8066f009f61b2d113974; cookie31=MTA2MzA2ODM5LHRiOTkzMzU3ODAsNzg2NjQ4NjQzQHFxLmNvbSxUQg%3D%3D; alimamapwag=TW96aWxsYS81LjAgKE1hY2ludG9zaDsgSW50ZWwgTWFjIE9TIFggMTBfMTJfNSkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzYwLjAuMzExMi4xMTMgU2FmYXJpLzUzNy4zNg%3D%3D; login=U%2BGCWk%2F75gdr5Q%3D%3D; alimamapw=TVIPCFVSVAcPCTkCBAVXBFYPDgBUBFFYU1NRCVMBBlJQUAYPCFYCAAIEAw%3D%3D; isg=Aiwse-M-WVQy8U1WVo_xyxxx_QyeTdHpr-SDm4ZtOFd6kcybrvWgHyIhx2_S; apushf4f28b675ff5e94dc07d6a8cd29d040c=%7B%22ts%22%3A1504424072480%2C%22parentId%22%3A1504362497326%7D; cna=mBwcEl+tJCwCAWfyqKcW/U8I'

    # ck ='t=dc43f2e577337a76d7551feec8e30576; undefined_yxjh-filter-1=true; 106306839_yxjh-filter-1=true; account-path-guide-s1=true; cookie2=0f02d660ece0e2f16e0ab22774390e8f; v=0; _tb_token_=mYG5w6aPIyq; cookie32=81b561b6a0fb8066f009f61b2d113974; cookie31=MTA2MzA2ODM5LHRiOTkzMzU3ODAsNzg2NjQ4NjQzQHFxLmNvbSxUQg%3D%3D; alimamapwag=TW96aWxsYS81LjAgKE1hY2ludG9zaDsgSW50ZWwgTWFjIE9TIFggMTBfMTJfNSkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzYwLjAuMzExMi4xMTMgU2FmYXJpLzUzNy4zNg%3D%3D; login=Vq8l%2BKCLz3%2F65A%3D%3D; alimamapw=TVIPCFVSVAcPCTkCBAVXBFYPDgBUBFFYU1NRCVMBBlJQUAYPCFYCAAIEAw%3D%3D; isg=AjY2XToLcypEoQdwsF1LhdKjh2r4_3v3sfbJPaAfIpm049Z9COfKoZyTjYl0; apushf4f28b675ff5e94dc07d6a8cd29d040c=%7B%22ts%22%3A1504426155295%2C%22parentId%22%3A1504362497326%7D; cna=mBwcEl+tJCwCAWfyqKcW/U8'
    # ck ='t=dc43f2e577337a76d7551feec8e30576; undefined_yxjh-filter-1=true; 106306839_yxjh-filter-1=true; account-path-guide-s1=true; cookie2=0f02d660ece0e2f16e0ab22774390e8f; v=0; _tb_token_=BQJ54jytIyq; cookie32=81b561b6a0fb8066f009f61b2d113974; cookie31=MTA2MzA2ODM5LHRiOTkzMzU3ODAsNzg2NjQ4NjQzQHFxLmNvbSxUQg%3D%3D; alimamapwag=TW96aWxsYS81LjAgKE1hY2ludG9zaDsgSW50ZWwgTWFjIE9TIFggMTBfMTJfNSkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzYwLjAuMzExMi4xMTMgU2FmYXJpLzUzNy4zNg%3D%3D; login=U%2BGCWk%2F75gdr5Q%3D%3D; alimamapw=TVIPCFVSVAcPCTkCBAVXBFYPDgBUBFFYU1NRCVMBBlJQUAYPCFYCAAIEAw%3D%3D; isg=AuTkU-zwYfy8QJUOzic5ExRpteQW1QmBt8z74_4FcK9yqYRzJo3YdxoJHzdK; apushf4f28b675ff5e94dc07d6a8cd29d040c=%7B%22ts%22%3A1504429777903%2C%22parentId%22%3A1504362497326%7D; cna=mBwcEl+tJCwCAWfyqKcW/U8I'

    # ck ='t=dc43f2e577337a76d7551feec8e30576; undefined_yxjh-filter-1=true; 106306839_yxjh-filter-1=true; account-path-guide-s1=true; cookie2=0f02d660ece0e2f16e0ab22774390e8f; v=0; _tb_token_=5xW5mnqhKyq; cookie32=81b561b6a0fb8066f009f61b2d113974; cookie31=MTA2MzA2ODM5LHRiOTkzMzU3ODAsNzg2NjQ4NjQzQHFxLmNvbSxUQg%3D%3D; alimamapwag=TW96aWxsYS81LjAgKE1hY2ludG9zaDsgSW50ZWwgTWFjIE9TIFggMTBfMTJfNSkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzYwLjAuMzExMi4xMTMgU2FmYXJpLzUzNy4zNg%3D%3D; login=WqG3DMC9VAQiUQ%3D%3D; alimamapw=TVIPCFVSVAcPCTkCBAVXBFYPDgBUBFFYU1NRCVMBBlJQUAYPCFYCAAIEAw%3D%3D; cna=mBwcEl+tJCwCAWfyqKcW/U8I; apushf4f28b675ff5e94dc07d6a8cd29d040c=%7B%22ts%22%3A1504443113589%2C%22heir%22%3A1504443110197%2C%22parentId%22%3A1504362497326%7D; isg=Aufny0etclX_mvbnyVbqKrsodh1xxLooaC1YCrlUR3adqAVqwD2En3auvJ_M'
    # ck ='t=dc43f2e577337a76d7551feec8e30576; undefined_yxjh-filter-1=true; 106306839_yxjh-filter-1=true; account-path-guide-s1=true; cookie2=0f02d660ece0e2f16e0ab22774390e8f; v=0; _tb_token_=5xW5mnqhKyq; cookie32=81b561b6a0fb8066f009f61b2d113974; cookie31=MTA2MzA2ODM5LHRiOTkzMzU3ODAsNzg2NjQ4NjQzQHFxLmNvbSxUQg%3D%3D; alimamapwag=TW96aWxsYS81LjAgKE1hY2ludG9zaDsgSW50ZWwgTWFjIE9TIFggMTBfMTJfNSkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzYwLjAuMzExMi4xMTMgU2FmYXJpLzUzNy4zNg%3D%3D; login=VT5L2FSpMGV7TQ%3D%3D; alimamapw=TVIPCFVSVAcPCTkCBAVXBFYPDgBUBFFYU1NRCVMBBlJQUAYPCFYCAAIEAw%3D%3D; cna=mBwcEl+tJCwCAWfyqKcW/U8I; apushf4f28b675ff5e94dc07d6a8cd29d040c=%7B%22ts%22%3A1504447842466%2C%22heir%22%3A1504447709025%2C%22parentId%22%3A1504362497326%7D; isg=AgMDcI1PXsbMXhILRcJWHv_UksFt0JbcrGG8JjXg-WLZ9CcWv0mQC7giGLNA'

    # ck ='t=dc43f2e577337a76d7551feec8e30576; undefined_yxjh-filter-1=true; 106306839_yxjh-filter-1=true; account-path-guide-s1=true; cookie2=0f02d660ece0e2f16e0ab22774390e8f; v=0; _tb_token_=5xW5mnqhKyq; cookie32=81b561b6a0fb8066f009f61b2d113974; cookie31=MTA2MzA2ODM5LHRiOTkzMzU3ODAsNzg2NjQ4NjQzQHFxLmNvbSxUQg%3D%3D; alimamapwag=TW96aWxsYS81LjAgKE1hY2ludG9zaDsgSW50ZWwgTWFjIE9TIFggMTBfMTJfNSkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzYwLjAuMzExMi4xMTMgU2FmYXJpLzUzNy4zNg%3D%3D; login=URm48syIIVrSKA%3D%3D; alimamapw=TVIPCFVSVAcPCTkCBAVXBFYPDgBUBFFYU1NRCVMBBlJQUAYPCFYCAAIEAw%3D%3D; taokeisb2c=; rurl=aHR0cDovL3B1Yi5hbGltYW1hLmNvbS8%2Fc3BtPWEyMWFuLjc5Mjc0NzEuYTIxNHRyOC4xNS43MGE1NWU3YWxsdkJVVA%3D%3D; isg=AgIC-Zgk73FZV_OUHFlHaWb_Uw5ufxkLxbqd2UwbmXUgn6IZNGNW_YifOa0Y; apushf4f28b675ff5e94dc07d6a8cd29d040c=%7B%22ts%22%3A1504489745246%2C%22parentId%22%3A1504487277067%7D; cna=mBwcEl+tJCwCAWfyqKcW/U8I'

    # ck ='t=dc43f2e577337a76d7551feec8e30576; undefined_yxjh-filter-1=true; 106306839_yxjh-filter-1=true; account-path-guide-s1=true; cookie2=0f02d660ece0e2f16e0ab22774390e8f; v=0; _tb_token_=5xW5mnqhKyq; taokeisb2c=; cookie32=81b561b6a0fb8066f009f61b2d113974; cookie31=MTA2MzA2ODM5LHRiOTkzMzU3ODAsNzg2NjQ4NjQzQHFxLmNvbSxUQg%3D%3D; alimamapwag=TW96aWxsYS81LjAgKE1hY2ludG9zaDsgSW50ZWwgTWFjIE9TIFggMTBfMTJfNSkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzYwLjAuMzExMi4xMTMgU2FmYXJpLzUzNy4zNg%3D%3D; login=UIHiLt3xD8xYTw%3D%3D; alimamapw=TVIPCFVSVAcPCTkCBAVXBFYPDgBUBFFYU1NRCVMBBlJQUAYPCFYCAAIEAw%3D%3D; cna=mBwcEl+tJCwCAWfyqKcW/U8I; apushf4f28b675ff5e94dc07d6a8cd29d040c=%7B%22ts%22%3A1504495047180%2C%22parentId%22%3A1504487277067%7D; isg=AqOjl8cN_iakm7IrpeL2Pl-0MuFHNCg8DEEcxtUByYJ5FMc2XWvPK9RCeNLh'
    # ck ='t=dc43f2e577337a76d7551feec8e30576; undefined_yxjh-filter-1=true; 106306839_yxjh-filter-1=true; account-path-guide-s1=true; cookie2=0f02d660ece0e2f16e0ab22774390e8f; _tb_token_=FRTCPtLryq; v=0; cookie32=81b561b6a0fb8066f009f61b2d113974; cookie31=MTA2MzA2ODM5LHRiOTkzMzU3ODAsNzg2NjQ4NjQzQHFxLmNvbSxUQg%3D%3D; alimamapwag=TW96aWxsYS81LjAgKE1hY2ludG9zaDsgSW50ZWwgTWFjIE9TIFggMTBfMTJfNSkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzYwLjAuMzExMi4xMTMgU2FmYXJpLzUzNy4zNg%3D%3D; login=Vq8l%2BKCLz3%2F65A%3D%3D; alimamapw=TVIPCFVSVAcPCTkCBAVXBFYPDgBUBFFYU1NRCVMBBlJQUAYPCFYCAAIEAw%3D%3D; cna=mBwcEl+tJCwCAWfyqKcW/U8I; apushf4f28b675ff5e94dc07d6a8cd29d040c=%7B%22ts%22%3A1504763207855%2C%22parentId%22%3A1504763188781%7D; isg=AtfX88bnQp6oZ8Y3eeb6Wst4Zk0rsLSY-J1IOikEFqZWWPSaMO35z8o-zM49'
    # ck ='t=dc43f2e577337a76d7551feec8e30576; undefined_yxjh-filter-1=true; 106306839_yxjh-filter-1=true; account-path-guide-s1=true; cookie2=d9e1685844b7cd0c44ba124957b87190; _tb_token_=UUXFCTbAwzq; v=0; cookie32=81b561b6a0fb8066f009f61b2d113974; cookie31=MTA2MzA2ODM5LHRiOTkzMzU3ODAsNzg2NjQ4NjQzQHFxLmNvbSxUQg%3D%3D; alimamapwag=TW96aWxsYS81LjAgKE1hY2ludG9zaDsgSW50ZWwgTWFjIE9TIFggMTBfMTJfNSkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzYwLjAuMzExMi4xMTMgU2FmYXJpLzUzNy4zNg%3D%3D; login=UtASsssmOIJ0bQ%3D%3D; alimamapw=TVIPCFVSVAcPCTkCBAVXBFYPDgBUBFFYU1NRCVMBBlJQUAYPCFYCAAIEAw%3D%3D; cna=mBwcEl+tJCwCAWfyqKcW/U8I; apushf4f28b675ff5e94dc07d6a8cd29d040c=%7B%22ts%22%3A1505210409729%2C%22parentId%22%3A1505210393680%7D; isg=AiQkkNSuISAK-1VOjud5U1Qp9SQcEVcLd4y7oz5FSO-y6cezZ8-9tnwP33eK'


    # ck ='t=dc43f2e577337a76d7551feec8e30576; undefined_yxjh-filter-1=true; 106306839_yxjh-filter-1=true; account-path-guide-s1=true; cookie2=d9e1685844b7cd0c44ba124957b87190; v=0; _tb_token_=CYNDNOs00r; cookie32=81b561b6a0fb8066f009f61b2d113974; cookie31=MTA2MzA2ODM5LHRiOTkzMzU3ODAsNzg2NjQ4NjQzQHFxLmNvbSxUQg%3D%3D; alimamapwag=TW96aWxsYS81LjAgKE1hY2ludG9zaDsgSW50ZWwgTWFjIE9TIFggMTBfMTJfNSkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzYwLjAuMzExMi4xMTMgU2FmYXJpLzUzNy4zNg%3D%3D; login=UtASsssmOIJ0bQ%3D%3D; alimamapw=TVIPCFVSVAcPCTkCBAVXBFYPDgBUBFFYU1NRCVMBBlJQUAYPCFYCAAIEAw%3D%3D; cna=mBwcEl+tJCwCAWfyqKcW/U8I; apushf4f28b675ff5e94dc07d6a8cd29d040c=%7B%22ts%22%3A1505218609611%2C%22parentId%22%3A1505218571504%7D; isg=AklJrcumdE_HCAgZO7wsbOkSWHOpOiLk2ucGlOu_3THXMmpEMufxmNYkAqF-'
    # ck ='t=dc43f2e577337a76d7551feec8e30576; undefined_yxjh-filter-1=true; 106306839_yxjh-filter-1=true; account-path-guide-s1=true; cookie2=d9e1685844b7cd0c44ba124957b87190; v=0; _tb_token_=CYNDNOs00r; cookie32=81b561b6a0fb8066f009f61b2d113974; cookie31=MTA2MzA2ODM5LHRiOTkzMzU3ODAsNzg2NjQ4NjQzQHFxLmNvbSxUQg%3D%3D; alimamapwag=TW96aWxsYS81LjAgKE1hY2ludG9zaDsgSW50ZWwgTWFjIE9TIFggMTBfMTJfNSkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzYwLjAuMzExMi4xMTMgU2FmYXJpLzUzNy4zNg%3D%3D; login=V32FPkk%2Fw0dUvg%3D%3D; alimamapw=TVIPCFVSVAcPCTkCBAVXBFYPDgBUBFFYU1NRCVMBBlJQUAYPCFYCAAIEAw%3D%3D; cna=mBwcEl+tJCwCAWfyqKcW/U8I; apushf4f28b675ff5e94dc07d6a8cd29d040c=%7B%22ts%22%3A1505226392309%2C%22parentId%22%3A1505226378157%7D; isg=Ag0NWZv5aFvVV8xV35Cg2LUGHC9HQkDbtnPCWE-SyKQPRin4FjucjOiQxu3a'
    # ck ='t=dc43f2e577337a76d7551feec8e30576; undefined_yxjh-filter-1=true; 106306839_yxjh-filter-1=true; account-path-guide-s1=true; cookie2=d9e1685844b7cd0c44ba124957b87190; v=0; _tb_token_=CYNDNOs00r; cookie32=81b561b6a0fb8066f009f61b2d113974; cookie31=MTA2MzA2ODM5LHRiOTkzMzU3ODAsNzg2NjQ4NjQzQHFxLmNvbSxUQg%3D%3D; alimamapwag=TW96aWxsYS81LjAgKE1hY2ludG9zaDsgSW50ZWwgTWFjIE9TIFggMTBfMTJfNSkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzYwLjAuMzExMi4xMTMgU2FmYXJpLzUzNy4zNg%3D%3D; login=URm48syIIVrSKA%3D%3D; alimamapw=TVIPCFVSVAcPCTkCBAVXBFYPDgBUBFFYU1NRCVMBBlJQUAYPCFYCAAIEAw%3D%3D; cna=mBwcEl+tJCwCAWfyqKcW/U8I; apushf4f28b675ff5e94dc07d6a8cd29d040c=%7B%22ts%22%3A1505266151941%2C%22parentId%22%3A1505266117842%7D; isg=AmRk20al4W9z-RWOTqe5k5TpNWRcUZdLN0x7Y36HMi_yKRXzpg5W9tHPn7bL'
    # ck='t=dc43f2e577337a76d7551feec8e30576; undefined_yxjh-filter-1=true; 106306839_yxjh-filter-1=true; account-path-guide-s1=true; cookie2=d9e1685844b7cd0c44ba124957b87190; v=0; _tb_token_=CYNDNOs00r; cookie32=81b561b6a0fb8066f009f61b2d113974; cookie31=MTA2MzA2ODM5LHRiOTkzMzU3ODAsNzg2NjQ4NjQzQHFxLmNvbSxUQg%3D%3D; alimamapwag=TW96aWxsYS81LjAgKE1hY2ludG9zaDsgSW50ZWwgTWFjIE9TIFggMTBfMTJfNSkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzYwLjAuMzExMi4xMTMgU2FmYXJpLzUzNy4zNg%3D%3D; login=Vq8l%2BKCLz3%2F65A%3D%3D; alimamapw=TVIPCFVSVAcPCTkCBAVXBFYPDgBUBFFYU1NRCVMBBlJQUAYPCFYCAAIEAw%3D%3D; cna=mBwcEl+tJCwCAWfyqKcW/U8I; apushf4f28b675ff5e94dc07d6a8cd29d040c=%7B%22ts%22%3A1505287374913%2C%22parentId%22%3A1505268007044%7D; isg=AldXcu2VwhYpcEa3-WZ62kv45s2rMDTSeB3IuqmEtCbh2HQasG10Tqu-TE-'
    # ck='t=dc43f2e577337a76d7551feec8e30576; undefined_yxjh-filter-1=true; 106306839_yxjh-filter-1=true; account-path-guide-s1=true; cookie2=d9e1685844b7cd0c44ba124957b87190; v=0; _tb_token_=RTP1667eB0r; cookie32=81b561b6a0fb8066f009f61b2d113974; cookie31=MTA2MzA2ODM5LHRiOTkzMzU3ODAsNzg2NjQ4NjQzQHFxLmNvbSxUQg%3D%3D; alimamapwag=TW96aWxsYS81LjAgKE1hY2ludG9zaDsgSW50ZWwgTWFjIE9TIFggMTBfMTJfNSkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzYwLjAuMzExMi4xMTMgU2FmYXJpLzUzNy4zNg%3D%3D; login=U%2BGCWk%2F75gdr5Q%3D%3D; alimamapw=TVIPCFVSVAcPCTkCBAVXBFYPDgBUBFFYU1NRCVMBBlJQUAYPCFYCAAIEAw%3D%3D; cna=mBwcEl+tJCwCAWfyqKcW/U8I; apushf4f28b675ff5e94dc07d6a8cd29d040c=%7B%22ts%22%3A1505292309039%2C%22parentId%22%3A1505287357447%7D; isg=AkxMGvkgeSdSD232Ni8Ra3zRHax0Ke8Dj0RjO6YNOfe9Me47zpc5v4GHpw7z'
    # ck ='t=dc43f2e577337a76d7551feec8e30576; undefined_yxjh-filter-1=true; 106306839_yxjh-filter-1=true; account-path-guide-s1=true; cookie2=d9e1685844b7cd0c44ba124957b87190; v=0; _tb_token_=RTP1667eB0r; cookie32=81b561b6a0fb8066f009f61b2d113974; cookie31=MTA2MzA2ODM5LHRiOTkzMzU3ODAsNzg2NjQ4NjQzQHFxLmNvbSxUQg%3D%3D; alimamapwag=TW96aWxsYS81LjAgKE1hY2ludG9zaDsgSW50ZWwgTWFjIE9TIFggMTBfMTJfNSkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzYwLjAuMzExMi4xMTMgU2FmYXJpLzUzNy4zNg%3D%3D; login=URm48syIIVrSKA%3D%3D; alimamapw=TVIPCFVSVAcPCTkCBAVXBFYPDgBUBFFYU1NRCVMBBlJQUAYPCFYCAAIEAw%3D%3D; rurl=aHR0cHM6Ly9wdWIuYWxpbWFtYS5jb20vP3NwbT1hMjE5dC43NjY0NTU0LmEyMTR0cjguNy40NTM1NjEzM2E2ZWxycQ%3D%3D; cna=mBwcEl+tJCwCAWfyqKcW/U8I; apushf4f28b675ff5e94dc07d6a8cd29d040c=%7B%22ts%22%3A1505730557647%2C%22parentId%22%3A1505730537597%7D; isg=AnV1I_NfQIv8qKQdB5i4EJ2OhPclXjdijstqkPebRuwQzpbAvkCO1acIbqSD'
    # ck ='t=dc43f2e577337a76d7551feec8e30576; undefined_yxjh-filter-1=true; 106306839_yxjh-filter-1=true; account-path-guide-s1=true; cookie2=d9e1685844b7cd0c44ba124957b87190; v=0; _tb_token_=sQJJs5991r; cookie32=81b561b6a0fb8066f009f61b2d113974; cookie31=MTA2MzA2ODM5LHRiOTkzMzU3ODAsNzg2NjQ4NjQzQHFxLmNvbSxUQg%3D%3D; alimamapwag=TW96aWxsYS81LjAgKE1hY2ludG9zaDsgSW50ZWwgTWFjIE9TIFggMTBfMTJfNSkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzYwLjAuMzExMi4xMTMgU2FmYXJpLzUzNy4zNg%3D%3D; login=UIHiLt3xD8xYTw%3D%3D; alimamapw=TVIPCFVSVAcPCTkCBAVXBFYPDgBUBFFYU1NRCVMBBlJQUAYPCFYCAAIEAw%3D%3D; cna=mBwcEl+tJCwCAWfyqKcW/U8I; apushf4f28b675ff5e94dc07d6a8cd29d040c=%7B%22ts%22%3A1505731921694%2C%22parentId%22%3A1505731894616%7D; isg=ApqaM7jGlypl7RustFFvER5360a2ZwDD7SL1gaQSSi3gFz5RjVmTtGUhkdVw'
    # ck ='t=dc43f2e577337a76d7551feec8e30576; undefined_yxjh-filter-1=true; 106306839_yxjh-filter-1=true; account-path-guide-s1=true; cookie2=d9e1685844b7cd0c44ba124957b87190; v=0; _tb_token_=sQJJs5991r; cookie32=81b561b6a0fb8066f009f61b2d113974; cookie31=MTA2MzA2ODM5LHRiOTkzMzU3ODAsNzg2NjQ4NjQzQHFxLmNvbSxUQg%3D%3D; alimamapwag=TW96aWxsYS81LjAgKE1hY2ludG9zaDsgSW50ZWwgTWFjIE9TIFggMTBfMTJfNSkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzYwLjAuMzExMi4xMTMgU2FmYXJpLzUzNy4zNg%3D%3D; login=VFC%2FuZ9ayeYq2g%3D%3D; alimamapw=TVIPCFVSVAcPCTkCBAVXBFYPDgBUBFFYU1NRCVMBBlJQUAYPCFYCAAIEAw%3D%3D; cna=mBwcEl+tJCwCAWfyqKcW/U8I; apushf4f28b675ff5e94dc07d6a8cd29d040c=%7B%22ts%22%3A1505738527363%2C%22parentId%22%3A1505738210126%7D; isg=AgIC-HmG72JXWPOUHFlHaWb_Uw6keweIxbqd2UwbuHUgn6AZNWKf_NqZOa0Y'
    ck ='t=dc43f2e577337a76d7551feec8e30576; undefined_yxjh-filter-1=true; 106306839_yxjh-filter-1=true; account-path-guide-s1=true; cookie2=d9e1685844b7cd0c44ba124957b87190; v=0; _tb_token_=sQJJs5991r; cookie32=81b561b6a0fb8066f009f61b2d113974; cookie31=MTA2MzA2ODM5LHRiOTkzMzU3ODAsNzg2NjQ4NjQzQHFxLmNvbSxUQg%3D%3D; alimamapwag=TW96aWxsYS81LjAgKE1hY2ludG9zaDsgSW50ZWwgTWFjIE9TIFggMTBfMTJfNSkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzYwLjAuMzExMi4xMTMgU2FmYXJpLzUzNy4zNg%3D%3D; login=U%2BGCWk%2F75gdr5Q%3D%3D; alimamapw=TVIPCFVSVAcPCTkCBAVXBFYPDgBUBFFYU1NRCVMBBlJQUAYPCFYCAAIEAw%3D%3D; cna=mBwcEl+tJCwCAWfyqKcW/U8I; apushf4f28b675ff5e94dc07d6a8cd29d040c=%7B%22ts%22%3A1505743127531%2C%22parentId%22%3A1505743113492%7D; isg=Aq6u8l8IeyZl9I_oaDVTrarb_wKwB3PM-R5BRdh36rFsu00VQT5-uAj9BRGs'
    cookies = cj.getCookie(ck)


    #创建选品库
    def createSelectLibray(self,title,dir_name):
        data ={"groupTitle":title,"groupType":1,"_tb_token_":"sQJJs5991r"}
        data = urllib.parse.urlencode(data)
        result = requests.post(self.create_libray_url, data=data, cookies=self.cookies, headers=self.post_headers)
        res = result.text
        print('res',res)
        js = json.loads(res)
        falg =js['ok']
        if(falg ==True):
            groupid = js['data']['data']
            content = str(title).replace("/","|")+":"+str(groupid)
            self.writeIDToFile(settings['TAOBAO_GROUP_ID_PATH_NO_SPIDER']+"/" +dir_name+".txt",content)
            print("选品库,["+title+"]"+"成功创建..")
        else:
            print("选品库,["+title+"]"+"创建失败..")

    #把要待转链接的ID存入到文件里面
    def writeIDToFile(self, idfile, content):
        with open(idfile, 'a') as f:
            f.write(content + '\n')



    #批量添加商品到指定的选品库中
    def batchAdd(self,groupId,idlist):
        data = {"groupId":groupId, "itemListStr":idlist}
        data = urllib.parse.urlencode(data)
        result = requests.post(self.batch_spu_url, data=data, cookies=self.cookies, headers=self.post_headers)
        res = result.text
        js = json.loads(res)
        falg = js['ok']
        # print(falg)
        if (falg == True):
            print("组,"+groupId+"添加商品成功")
        else:
            print("组,"+groupId+"添加商品失败")

   #读取选品库组的ID
    def getGroupIdJson(self,dir_name):
        fileName = dir_name + ".txt"
        filePath = settings['TAOBAO_GROUP_ID_PATH_NO_SPIDER']
        fullPath = filePath + "/" + fileName
        f = open(fullPath, "r", encoding='UTF-8')
        lines = f.readlines()  # 读取全部内容
        obj ={}
        for line in lines:
             ls = line.split(":")
             obj[ls[0]] = ls[1].strip()
        return obj

    # 查询关键件
    def getSearchKWList(self, search_dir_kw,setpath):
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
        fullPath = setpath + "/" +fileName
        f = open(fullPath, "r", encoding='UTF-8')
        lines = f.readlines()  # 读取全部内容
        for line in lines:
            objlist.append(line.strip())

    #拼接参数
    def __getExportExcelParam(self,type,groupId):
        if(type =='ios'):
            data = {"scenes":1,"adzoneId":76574177,"siteId":23098705,"groupId":groupId}
        elif(type =='and'):
            data = {"scenes": 1, "adzoneId": 76562672, "siteId": 23088972, "groupId": groupId}
        elif (type == 'pc'):
            data = {"scenes": 1, "adzoneId": 107382759, "siteId": 27992589, "groupId": groupId}
        else:
            print('操作类型不能为空或者操作类型不正确..')
            data ={}
        data = urllib.parse.urlencode(data)
        return data


    #批量生成excel
    def batchExportExcel(self,groupId,groupTitle,type,dir_name,source):
        data = self.__getExportExcelParam(type,groupId)
        resp = requests.get(self.batch_export_url, params=data, cookies=self.cookies, headers=self.post_headers)
        dir_file =settings['TAOBAO_EXCEL_PATH_NO_SPIDER']+"/"+dir_name

        if not os.path.exists(dir_file):
            os.mkdir(dir_file)

        excelfile=dir_file+"/"+self.__generatorExcelName(groupTitle,type,source)+".xls"

        with open(excelfile, 'wb') as f:
            for chunk in resp.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
                    f.flush()
        print("文件"+groupTitle+"_"+source+"导出成功....")


    #生成excel文件命名
    def __generatorExcelName(self,groupTitle,type,source):
        dirs =groupTitle.split("_")
        # if (source =='pc'):
        #     return dirs[0] + "|" + dirs[1] + "|" + dirs[2] + "_" + "jiahongping" + "_" + source.upper()
        # else:
        #     return dirs[0] + "|" + dirs[1] + "|" + dirs[2] + "_" + "jiahongping" + "_" + source + "_" + type.upper()

        return dirs[0] + "|" + dirs[1] + "|" + dirs[2] + "_" + "jiahongping" + "_" + source + "_" + type.upper()

    #删除指定的选品库
    def delSelectLibray(self,groupId):
        data = {"groupId": groupId, "_tb_token_": "sQJJs5991r"}
        data = urllib.parse.urlencode(data)
        result = requests.post(self.del_libray_url, data=data, cookies=self.cookies, headers=self.post_headers)
        res = result.text
        js = json.loads(res)
        falg = js['ok']
        print(res)
        if (falg == True):
            print("选品库ID," + groupId + "删除成功")
        else:
            print("选品库ID," + groupId + "删除失败")

if __name__ == '__main__':

    tbu = TBLibrayUtil()
    # platforms =["and", "ios"]
    platforms = ["pc"]
    # #批量创建选品库 ,服饰内衣,电子词典,瑜伽,粮油食品,童装婴儿装亲子装01
    dir_name_str = "鞋"
    dirs = dir_name_str.split(",")
    for dir_name in dirs:
        #创建选品库
        keywords = tbu.getSearchKWList(dir_name, settings['TAOBAO_ID_PATH_NO_SPIDER'])
        for key in keywords:
            ks = key.split(":")
            cat_path = ks[0]
            tbu.createSelectLibray(cat_path,dir_name)
            time.sleep(random.randint(1, 3))
        print("目录{" + dir_name + "}" + ",所有选品库创建完毕...")

        #选品库导入商品
        obj = tbu.getGroupIdJson(dir_name)
        keywords = tbu.getSearchKWList(dir_name, settings['TAOBAO_ID_PATH_NO_SPIDER'])
        for key in keywords:
            ks = key.split(":")
            cat_path = ks[0]
            # 批量选取商品到指定的选品库中
            if cat_path in obj:
                groupId = obj[cat_path]
                id_list = str(ks[1]).strip()
                tbu.batchAdd(groupId, id_list)
                time.sleep(random.randint(2, 5))

        #批量导出选品库的商品
        keywords = tbu.getSearchKWList(dir_name, settings['TAOBAO_GROUP_ID_PATH_NO_SPIDER'])
        for key in keywords:
            ks = key.split(":")
            groupTitle = ks[0]
            # 批量选取商品到指定的选品库中
            groupId = str(ks[1])
            source = groupTitle.split("_")[-1]
            print('source',source)
            # print(groupTitle,groupId)
            # 把选定的选品库中的商品批量导出excel
            groupTitle = str(groupTitle).replace("/", "|")
            # ios and
            for platform in platforms:
                tbu.batchExportExcel(groupId, groupTitle, platform, dir_name, source)
                time.sleep(random.randint(1, 3))

        #删除已导出商品的选品库
        keywords = tbu.getSearchKWList(dir_name, settings['TAOBAO_GROUP_ID_PATH_NO_SPIDER'])
        for key in keywords:
            ks = key.split(":")
            groupId = str(ks[1])
            tbu.delSelectLibray(str(groupId))
            time.sleep(random.randint(1, 3))





