'''用户相关测试'''
import json

import pytest
import requests

host_data = 'http://112.13.89.101:9011'
user_data = [
    {
        "account": "admin",
        "mobile_phone": "",
        "password": "123456",
        "code": "",
        "way": "1",
        "source": "1"
    },  # 超级管理员
    {
        "account": "yydbt",
        "mobile_phone": "",
        "password": "nbrd@123",
        "code": "",
        "way": "1",
        "source": "1"
    },  # 余姚代表团工作人员
    {
        "account": "",
        "mobile_phone": "18815276687",
        "password": "",
        "code": "190212",
        "way": "3",
        "source": "2"
    },  # 代表
]


class TestLogin():
    '''用户登录'''

    def setup_class(self):
        self.url = host_data + '/v1/auth/login/'

    @pytest.mark.admin
    def test_case1(self):
        """超级管理管理员登录成功"""
        r = requests.post(self.url, data=user_data[0])
        di = json.loads(r.text)
        assert di.get('code') == 0

    @pytest.mark.worker
    def test_case2(self):
        """工作人员登陆成功"""
        r = requests.post(self.url, data=user_data[1])
        di = json.loads(r.text)
        assert di.get('code') == 0

    @pytest.mark.rddb
    def test_case3(self):
        """人大代表登陆成功"""
        r = requests.post(self.url, data=user_data[2])
        di = json.loads(r.text)
        assert di.get('code') == 0

    def test_case4(self):
        """账号正确密码错误"""
        user_data[0]['password'] = '123123'
        r = requests.post(self.url, data=user_data[0])
        print(user_data[0])
        di = json.loads(r.text)
        assert di.get('code') == 1

    def test_case5(self):
        """账号为空密码正确"""
        user_data[0]['account'] = ''
        r = requests.post(self.url, data=user_data[0])
        di = json.loads(r.text)
        assert di.get('code') == 1

    def test_case6(self):
        """账号正确密码为空"""
        user_data[0]['password'] = ''
        r = requests.post(self.url, data=user_data[0])
        di = json.loads(r.text)
        assert di.get('code') == 1
