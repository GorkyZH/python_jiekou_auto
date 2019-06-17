#coding:utf-8

"""
封装常量
"""
class global_var:
    Id = '0'    #ID
    module = '1'   #模块
    url = '2'   #url接口地址
    run = '3'   #是否运行
    request_type = '4'  #请求类型
    header = '5'   #头部
    case_dependent = '6'  #case依赖
    data_dependent = '7'  #依赖的返回数据
    key_depedent = '8'   #依赖字段
    parameter = '9'   #请求参数
    expect = '10'   #预期结果
    result = '11'   #实际结果

#获取id
def get_id():
    return global_var.Id

#获取url
def get_url():
    return global_var.url

#是否运行
def get_run():
    return global_var.run

#获取请求类型
def get_request_type():
    return global_var.request_type

#获取头部
def get_header():
    return global_var.header

#获取头部值
def get_header_value():
    Headers = {
        "Content-Type":"application/json"
    }
    return Headers

#获取带token的头部值
def get_token_header_value(token_value):
    Headers = {
        "Authorization":'Bearer '+token_value,
        "Content-Type":"application/json"
    }
    return Headers

#获取case依赖
def get_case_dependent():
    return global_var.case_dependent

#获取返回数据依赖
def get_data_dependent():
    return global_var.data_dependent

#获取返回数据的依赖字段
def get_key_dependent():
    return global_var.key_depedent

#获取请求参数
def get_parameter():
    return global_var.parameter

#获取预期结果
def get_except():
    return global_var.expect

#获取实际结果
def get_result():
    return global_var.result

