# coding=utf8
import requests
import json
import unittest

class CaseLogin(unittest.TestCase):
    def setUp(self):
        self.url = "http://182.61.33.241:8089/app/api/public/1.0/open/login"

    def test_01_login(self):
        response = requests.post(url=self.url, data=json.dumps({'operId': '15616699600', 'operPwd': '123456'}),
                      headers={'Content-Type': 'application/json'})
        print(self.url)
        print(response.status_code)
        result = response.json()
        print("打印登录结果：", result)
        self.token = result["data"]["token"]
        print("登录返回的token值：", self.token)

    def test_02_home(self):
        response = requests.get(url="http://182.61.33.241:8089/app/api/private/1.0/homePage/index",
                                headers={'Authorization':'Bearer '+self.token,'Content-Type': 'application/json'})
        print("首页获取到的token值：", self.token)
        print(response.status_code)
        result = response.json()
        return result

if __name__ == '__main__':
    unittest.main()





