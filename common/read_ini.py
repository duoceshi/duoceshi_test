#coding=utf-8
"""
===========================
Author:多测师_王sir
Time:2020-12-16 20:12
Wechat:xiaoshubass
website:www.duoceshi.cn
===========================
"""

'''
此模块是用来读取ini文件的
安装：
pip install configparser
'''

from configparser import ConfigParser   #导入ConfigParser类
from common.handle_path import *
import os

class Read_Ini(ConfigParser):

    def __init__(self,filename):
        super(Read_Ini, self).__init__()   #继承ConfigParser父类的构造方法
        self.read(filename)

    def get_value(self,section=None, option=None):
        '''
        封装一个根据section和option获取对应value值的工具方法
        :return:
        '''
        value = self.get(section,option)
        return value

path = os.path.join(conf_path,'data.ini')
read = Read_Ini(path)
# url = read.get_value('env','url')  #http://cms.duoceshi.cn
# headers = read.get_value('env','headers') #{"Content-Type":"application/x-www-form-urlencoded"}









