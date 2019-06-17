# coding=utf8
import requests
import json
import os

class CaseLogin():
    def __init__(self, url):
        #self.token = token
        self.url = url

    # def base_dir():
    #     '''返回token文件的目录文件保存绝对地址'''
    #     return os.path.join(os.path.dirname(__file__), 'token.md')

    def go_to_login(self):
        response = requests.post(url=self.url, data=json.dumps({'operId': '15616699600', 'operPwd': '123456'}),
                      headers={'Content-Type': 'application/json'})
        print(self.url)
        print(response.status_code)
        result = response.json()
        print(result)
        token = result["data"]["token"]
        print("token值：", token)
        # with open(base_dir(self), 'w') as f:
        #     f.write(token)
        return token

    # def getToken():
    #     '''读取存储在文件中的token'''
    #     with open(base_dir(), 'r') as f:
    #     return f.read()


    # def go_to_home(self):
    #     response = requests.get(url="http://182.61.33.241:8089/app/api/private/1.0/homePage/index",
    #                             headers={'Authorization':self.token,'Content-Type': 'application/json'})
    #     print(response.status_code)
    #     result = response.json()
    #     return result

if __name__ == '__main__':
    login = CaseLogin("http://182.61.33.241:8089/app/api/public/1.0/open/login")
    login.go_to_login()
    # response_data = login.go_to_login()
    # print("打印登录结果：", response_data)
    # token = response_data["data"]["token"]
    # print("token值：", token)
    #print(login.go_to_home())

