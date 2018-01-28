# this is use python script!
# -*- coding: UTF-8 -*-
import re

for idhtml in open('../config/idhtml.txt'):
    id = re.sub("\D", "", idhtml)
    with open('../config/id_regex.txt','a')as f:
        f.write(id+'\n')
    print(id)