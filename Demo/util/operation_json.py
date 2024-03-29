# _*_ coding:utf-8 _*_
import json
import sys
# import importlib
# importlib.reload(sys)

"""
读取json文件工具类
"""
class OperationJson:
    def __init__(self):
        self.data = self.read_data()

    #读取json文件
    def read_data(self):
        #with open("../dataconfig/logincom.json") as fp:
         with open("/Users/mac/Desktop/测试资料/python_jiekou_auto/python_jiekou_git/Demo/dataconfig/logincom.json") as fp:
            data = json.load(fp)
            return data

    #根据关键字获取数据
    def get_data(self, id):
        #return self.data[id]
        return json.dumps(self.data[id])

if __name__ == '__main__':
    operJson = OperationJson()
    print(operJson.get_data('login'))
