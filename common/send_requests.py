#coding=utf-8
"""
===========================
Author:多测师_王sir
Time:2020-12-16 20:20
Wechat:xiaoshubass
website:www.duoceshi.cn
===========================
"""

'''
封装一个发送接口请求的工具类
'''
import requests

class Send_Requests(object):

    def __init__(self):
        #创建一个session对象、用来保持会话
        self.session = requests.Session()

    def send(self,method,url,data=None,json=None,params=None,headers=None):
        '''封装一个发送接口请求的工具方法'''
        method = method.lower()   #把传进来的接口请求方法转换为小写
        if method == 'get':
            response = self.session.get(url=url,params=params)
        elif method == 'post':
            response = self.session.post(url=url,data=data,headers=headers)
        elif method == 'post_json':
            response = self.session.post(url=url,json=json,headers=headers)
        elif method == 'delete':
            response = self.session.delete(url=url,headers=headers)
        return response   #把得到的接口响应结果返回给到函数的调用处



























