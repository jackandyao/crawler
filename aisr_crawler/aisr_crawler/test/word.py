# this is use python script!
# -*- coding: UTF-8 -*-
import jieba
key = '我们有个家电配件的需求'
word ='家电配件'
seg_list = jieba.cut(word, cut_all=False)
str = ": ".join(seg_list)
strs = str.split(":")
falg =[]
for s in strs:
    falg.append(s.strip() in key)


if(False in falg):
    print('no ok')
else:
    print('ok')

#print ("Default Mode:",strs)  # 精确模式

