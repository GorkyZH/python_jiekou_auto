#coding:utf-8
from data.get_data import GetData
from base.run_method import RunMethod
from util.common_util import CommonUtil

class LoginApi:
    def __init__(self):
        self.data = GetData("/Users/mac/Desktop/测试资料/python_jiekou_auto/python_jiekou_git/Demo/dataconfig/login.xls")
        self.run_method = RunMethod()
        self.util = CommonUtil()

    def go_run_login(self):
        # 获取用例行数
        row_count = self.data.get_case_line()
        #循环用例
        for i in range(1, row_count):
            #获取isrun，是否运行该用例
            is_run = self.data.get_is_run(i)
            if is_run:
                #获取url
                url = self.data.get_url(i)
                request_type = self.data.get_request_type(i)
                header = self.data.get_header(i)
                request_data = self.data.get_data_for_json(i)
                response = self.run_method.run_main(request_type, url, request_data, header)
                print("返回结果：", response)
                expect_res = self.data.get_except(i)
                print("期望结果：", expect_res)
                if self.util.is_contain(expect_res, response):
                    self.data.write_result(i, "测试通过")
                    print("测试通过")
                else:
                    self.data.write_result(i, "测试失败")
                    print("测试失败")
        return response

if __name__ == '__main__':
    login = LoginApi()
    login.go_run_login()
