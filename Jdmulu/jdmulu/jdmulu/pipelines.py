# # -*- coding: utf-8 -*-
#
# # Define your item pipelines here
# #
# # Don't forget to add your pipeline to the ITEM_PIPELINES setting
# # See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
# from scrapy import signals
# import json
# import codecs
# import sys
#
# # class JdmuluPipeline(object):
# #     def __init__(self):
# #         #self.file = codecs.open('data_jd.json', 'wb', encoding='utf-8')
# #         self.file = "data"
# #         self.file += ".txt"
# #         self.fp = open(self.file, 'w',encoding='utf-8')
# #
# #     def process_item(self, item, spider):
# #         # file_name = "data"
# #         # file_name += ".txt"
# #         # fp = open(file_name, 'wb')
# #         # fp.write(item)
# #         # fp.close()
# #         # line = json.dumps(dict(item), ensure_ascii=False) + "\n"
# #         # self.file.write(line)
# #         mulu_level1 = str(item['mulu_level1']).replace('[\'','')
# #         mulu_level1 = mulu_level1.replace('\']','')
# #         mulu_level2 = str(item['mulu_level2']).replace('[\'','')
# #         mulu_level2 = mulu_level2.replace('\']', '')
# #         mulu_level3 = str(item['mulu_level3']).replace('[\'','')
# #         mulu_level3 = mulu_level3.replace('\']', '')
# #         mulu_level3 = mulu_level3.replace('\'', '')
# #
# #         for value in item['mulu_level3']:
# #             #print('x',value)
# #             #mulu_level = mulu_level1 + "_" + mulu_level2 + "_" + value + "\n"
# #             mulu_level = value + "\n"
# #             self.fp.write(mulu_level)
# #         #fp.write('0123456789abcd')
# #         #fp.write(mulu_level1)
# #         #fp.close()
# #
# #         return item
# #
# #     def spider_closed(self, spider):
# #         #self.file.close()
# #         pass
#
# class JdproductPipeline(object):
#     def __init__(self):
#         #print('kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk',item['keyword'])
#         self.file = "phone_brand"
#         #self.file = "phone_id"
#         self.file += ".txt"
#         self.fp = open(self.file, 'w',encoding='utf-8')
#
#         self.fp_id = open("phone_id.txt",'w',encoding='utf-8')
#
#
#     def process_item(self, item, spider):
#         #print('item',item)
#         for value in item['brand']:
#             if '\n' not in value:
#                 brand = value + '\n'
#                 self.fp.write(brand)
#
#         for value in item['id']:
#             id = value + '\n'
#             self.fp_id.write(id)
#
#         # brand = str(item['brand']).strip() + "\n"
#         # print(brand)
#         # self.fp.write(brand)
#         #
#         # id = str(item['id']).strip() + "\n"
#         # print('ddddddddddd', id)
#         # self.fp.write(id)
#         #print('dddddddddddddddddddd',item['brand'])
#         # name = item['keyword']
#         # self.fp_id.write("#####################################################" + str(name[0]).strip() + "\n")
#        # return item
#
#     def spider_closed(self, spider):
#         #self.fp.close()
#         pass
#     pass
#
#
