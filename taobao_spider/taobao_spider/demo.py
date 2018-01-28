# this is use python script!
# -*- coding: UTF-8 -*-
import re
str ="久量<span class=H>电</span><span class=H>蚊拍</span>充<span class=H>电</span>式超强大号苍蝇拍<span class=H>电</span>子灭蚊器打蚊子家用<span class=H>电</span>文拍正品"
phanzi = re.compile(u'[\u4e00-\u9fa5]');
res=phanzi.findall(str)
a=""
for r in res:
     a+=r

url ="//img.alicdn.com/bao/uploaded/i1/TB1frqORXXXXXauXFXXXXXXXXXX_!!0-item_pic.jpg"
if "http" in url:
    print("true",url)
else:
    print("false","http:"+url)
print("res",a)
