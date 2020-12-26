#coding=utf-8
"""
===========================
Author:多测师_王sir
Time:2020-12-16 21:51
Wechat:xiaoshubass
website:www.duoceshi.cn
===========================
"""

import time
from library.HTMLTestRunnerNew import HTMLTestRunner
from library.mail3 import SendMail
import unittest
from common.handle_path import *

#定义生成报告的绝对路径和文件名称
now = time.strftime('%Y-%m-%d-%H-%M-%S')
filename = report_path + '\\' + str(now) + '_api_report.html'

def auto_run():
    '''自动搜索用例并且运行'''
    discover = unittest.defaultTestLoader.discover(start_dir=testcase_path,pattern='test_*.py')
    f = open(filename,'wb')
    runner = HTMLTestRunner(stream=f,title='cms接口自动化测试报告',
                            description='用例执行情况如下：',
                            tester='多测师_王sir')
    runner.run(discover)
    f.close()

def sendMail():
    sm = SendMail(send_msg=filename,attachment=filename)
    sm.send_mail()


if __name__ == '__main__':
    auto_run()
    sendMail()




#作业：
#1.熟悉这个接口框架的代码、用Word去梳理一下
#2.把查询用户接口用这个框架去写一遍、调通生成报告

















