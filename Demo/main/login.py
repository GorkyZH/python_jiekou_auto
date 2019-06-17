# coding:utf-8
import requests
import os
import json

class Login:
    def __init__(self, url):
        self.url = url

    def login(self):
        """把token字符串写入到文件中"""
        r = requests.post(
        url=self.url+"login", data=json.dumps({'operId': '15616699600', 'operPwd': '123456'}),
                      headers={'Content-Type': 'application/json'})
        with open(base_dir(), 'w') as f:
            f.write(r.json()['data']['token'])
        return r.json()['data']['token']

def base_dir():
    '''返回toeken文件的目录文件保存绝对地址'''
    return os.path.join(os.path.dirname(__file__), 'token.md')

def getToken():
    '''读取存储在文件中的token'''
    with open(base_dir(),'r') as f:
        return f.read()

    """ 随便写个登录后的接口"""
def test_toekn_apply():
    r = requests.get("http://182.61.33.241:8089/app/api//private/1.0/homePage/index",headers={"Authorization": 'Bearer '+getToken(),'Content-Type': 'application/json'})
    return r.json()

if __name__ == '__main__':
    login = Login("http://182.61.33.241:8089/app/api/public/1.0/open/")
    login.login()
    print(test_toekn_apply())
