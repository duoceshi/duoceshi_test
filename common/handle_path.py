#coding=utf-8
"""
===========================
Author:多测师_王sir
Time:2020-12-16 20:06
Wechat:xiaoshubass
website:www.duoceshi.cn
===========================
"""

'''
此模块封装的是每个包的绝对路径
'''

import os

#定义项目的路径
base_path = os.path.dirname(os.path.dirname(__file__))
# print(base_path)  #C:/project/dcs1_cms_framework

#conf的路径
conf_path = os.path.join(base_path,'conf')

#data的路径
data_path = os.path.join(base_path,'data')

#report的路径
report_path = os.path.join(base_path,'report')

#testcase的路径
testcase_path = os.path.join(base_path,'testcase')






















