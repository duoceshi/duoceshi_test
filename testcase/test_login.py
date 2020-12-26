#coding=utf-8
"""
===========================
Author:多测师_王sir
Time:2020-12-16 21:00
Wechat:xiaoshubass
website:www.duoceshi.cn
===========================
"""

'''
此模块就是用来编写测试用例
'''


import unittest
from common.handle_excel import Read_Excel
from common.handle_path import *
import os
from library.ddt import ddt,data
from common.send_requests import Send_Requests
from common.read_ini import read  #导入read对象

case_file = os.path.join(data_path,'apicases.xlsx')

@ddt
class Test_Login(unittest.TestCase):
    read_excel = Read_Excel(case_file,'login')
    cases = read_excel.get_data()   #cases是一个大的列表、列表里面有3个字典、每个字典都是一条用例
    request = Send_Requests()  #创建发送接口请求的对象

    @data(*cases)  #*cases是列表、里面有3个字典
    def test01_login(self,case):  #case是一个一个的字典
        #1.准备接口的入参
        url = read.get_value('env','url') + case['url']
        #eval函数的作用：就是执行一个字符串表达式、并且返回结果
        headers = eval(read.get_value('env','headers'))
        method = case['method']  #post
        data = eval(case['data'])   #通过eval函数把字符串转换为字典<class 'dict'>
        expected = eval(case['expected'])
        case_id = case['case_id']
        row = case_id + 1
        #2.发送接口的请求
        response = self.request.send(method=method,url=url,data=data,headers=headers)
        result = response.json()

        #3.进行接口的断言
        try:  #用来捕获异常
            self.assertEqual(result['msg'],expected['msg'])
            self.assertEqual(result['code'],expected['code'])
        except Exception as e:
            print(e)
            self.read_excel.write_data(row,8,'未通过')
        else:
            self.read_excel.write_data(row,8,'通过')

if __name__ == '__main__':
    unittest.main()








































