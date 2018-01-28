# this is use python script!
# -*- coding: UTF-8 -*-
import json
file ='../config/JD_个性化妆.txt'

for key in open(file,encoding="utf-8"):
    ks = key.split(",")
    for k in ks:
        print(k)
