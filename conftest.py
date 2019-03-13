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
        "account": "yzdbt",
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


@pytest.fixture()
def admin_token():
    '''超级管理员token'''
    url = host_data + '/v1/auth/login/'
    r = requests.post(url, data=user_data[0])
    di = json.loads(r.text)
    token = di['data']['user_info']['token']
    return token


@pytest.fixture()
def worker_token():
    '''工作人员token'''
    url = host_data + '/v1/auth/login/'
    r = requests.post(url, data=user_data[1])
    di = json.loads(r.text)
    token = di['data']['user_info']['token']
    return token


@pytest.fixture()
def rddb_token():
    '''人大代表token'''
    url = host_data + '/v1/auth/login/'
    r = requests.post(url, data=user_data[2])
    di = json.loads(r.text)
    token = di['data']['user_info']['token']
    return token


@pytest.fixture()
def delegation_id(admin_token):
    '''获取余姚代表团id'''
    url = host_data + '/v1/pc/common/delegation/list/'
    headers = {
        "Authorization": admin_token
    }
    r = requests.get(url, headers=headers)
    di = json.loads(r.text)
    delegation_id = di["data"]["list"][0]["id"]
    return delegation_id


@pytest.fixture()
def unit_id(admin_token):
    '''获取unit'''
    url = host_data + '/v1/pc/common/unitRole/list/'
    headers = {
        "Authorization": admin_token
    }
    r = requests.get(url, headers=headers)
    di = json.loads(r.text)
    unit_id = di["data"]["default"]["default"]["unit"]
    return unit_id


@pytest.fixture()
def test_conference_id(admin_token, unit_id):
    '''获取会议id'''
    url = host_data + '/v1/pc/conference/conference/list/'
    headers = {
        "Authorization": admin_token,
        "unit": unit_id
    }
    params = {
        "is_parent": "true"
    }
    r = requests.get(url, headers=headers, params=params)
    di = json.loads(r.text)
    print(di)
    conference_id = di["data"]["list"][0]['id']
    return conference_id
