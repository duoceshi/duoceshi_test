#coding=utf-8
"""
===========================
Author:多测师_王sir
Time:2020-12-16 21:32
Wechat:xiaoshubass
website:www.duoceshi.cn
===========================
"""

'''
备注在Jenkins构建项目的时候、有可能找不到项目的地址、python项目的环境地址
所以需要加入项目的地址
'''
import sys
sys.path.append("C:\Git\duoceshi_test")
#加入第三方环境的地址
sys.path.append('C:\Python37\Lib\site-packages')

import unittest
from common.read_ini import read
from common.send_requests import Send_Requests
from common.handle_excel import Read_Excel
from library.ddt import ddt,data
from common.handle_path import *
import os

case_file = os.path.join(data_path, 'apicases.xlsx')

@ddt
class Test_UpdateLoginPwd(unittest.TestCase):
    read_excel = Read_Excel(case_file, 'updateLoginPwd')
    cases = read_excel.get_data()  # cases是一个大的列表、列表里面有2个字典、每个字典都是一条用例
    request = Send_Requests()  # 创建发送接口请求的对象

    @classmethod
    def setUpClass(cls) -> None:
        #1.准备登录接口的入参
        url = read.get_value('env','url')+'/cms/manage/loginJump.do'

        data = {
            'userAccount':read.get_value('test_data','username'),
            'loginPwd':read.get_value('test_data','pwd')
        }
        headers = eval(read.get_value('env','headers'))

        #2.发送登录接口的请求
        response = cls.request.send(method='post',url=url,data=data,headers=headers)

    @data(*cases)
    def test01_updateLoginPwd(self,case):
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
























