#coding=utf-8

from main.case_run import CaseLogin
import requests

class CaseHome:
    def __init__(self):
        login = CaseLogin("http://182.61.33.241:8089/app/api/public/1.0/open/login")
        self.token = login.go_to_login()
        self.headers = {
            'Authorization': 'Bearer '+self.token,
            'Content-Type': 'application/json'
        }

    def go_to_home(self):
        response = requests.get(url="http://182.61.33.241:8089/app/api/private/1.0/homePage/index",
                                    headers=self.headers)
        print("拿到的token值：", self.token)
        print(response.status_code)
        result = response.json()
        return result

if __name__ == '__main__':
    home = CaseHome()
    print(home.go_to_home())


