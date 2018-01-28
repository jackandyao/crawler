# this is use python script!
# -*- coding: UTF-8 -*-
import logging,json

# logging.basicConfig(level=logging.INFO,
#                     format='%(message)s',
#                     filename='myapp.log',
#                     filemode='w')
#
# logging.basicConfig(level=logging.INFO,
#                     format='%(message)s')

#logging.info('1001'+":" +"abc" +":" +"双节棍")

str ="手机配件_手机配件_苹果周边:{'startTkRate': '10', 'startBiz30day': '30', 'startPrice': '1', 'sortType': '9', 'endPrice': '1000'}"

jsonstr = "{'startTkRate': '10', 'startBiz30day': '30', 'startPrice': '1', 'sortType': '9', 'endPrice': '1000'}"
#strs = str.split("_")
#print(json.loads(jsonstr))

jsonData = '{"a":1,"b":2,"c":3,"d":4,"e":5}'

text = json.loads(jsonData)
print(text)

a ='手机支架&{"startTkRate": "15", "startBiz30day": "30", "startPrice": "10", "sortType": "9", "endPrice": "1000"}'
ss =  a.split("&")
print(json.loads(ss[1])["startTkRate"])