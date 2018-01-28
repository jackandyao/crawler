# this is use python script!
# -*- coding: UTF-8 -*-
# class Employee:
#     '所有员工的基类'
#     empCount = 0
#
#     # 类被实例化的时候会首先调用该函数,类似于java中的构造器功能
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#         Employee.empCount += 1
#
#     def displayCount(self):
#         print("Total Employee %d" % Employee.empCount)
#
#     def displayEmployee(self):
#         print("Name : ", self.name, ", Salary: ", self.salary)
# "创建 Employee 类的第一个对象"
# emp1 = Employee("Zara", 2000)
# # "创建 Employee 类的第二个对象"
# emp2 = Employee("Manni", 5000)
# # emp1.displayEmployee()
# # emp2.displayEmployee()
# # emp1.displayCount()
# emp_list =[]
# emp_list.append(emp1)
# emp_list.append(emp2)
# dict_emp = dict(emp1)
# print(dict_emp)

#import ConfigParser
# import configparser
# parser = configparser.SafeConfigParser()
# parser.read("../config/test.conf")
# ##params = parser.items("test_dev")
# p={}
# #for k,v in params:
#     #p[k]=v
#     #print(k,v)
# #print('p',p)
#
#
# import platform
# print(platform.system())

import re
str ="鹤顺堂（HESHUNTANG）养生酒"
str2 = re.sub('（[^）]+）','',str)
print(str2)

strs =str.split('\t')
for s in strs:
    print(s)


