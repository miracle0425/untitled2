# 1 我们先用设计模式实现ihrm登录
# 2 根据我们设计模式的实现封装ihrm登录接口
# 3 根据封装的接口，优化ihrm登录的代码
# 导包
import unittest
import logging
from fileinput import filename
import requests
from parameterized import parameterized

import app
from utils import assert_common, read_login_data


# 创建测试类，继承unittest.TestCase
class TestIHRMLogin(unittest.TestCase):
    # 初始化
    def setUp(self):
        self.login_url = "http://ihrm-test.itheima.net" + "/api/sys/login"
        from api.login_api import TestLoginApi  # 导入封装的API模块
        self.login_api = TestLoginApi()  # 实例化登录API

    def tearDown(self):
        ...

    # 编写第一个案例，测试登录
    filename = app.BASE_DIR + "/data/login_data.json"
    @parameterized.expand(read_login_data(filename))
    def test_login(self,case_name,jsonData,http_code,success,code,message):
        # IHRM项目发送登录请求
        headers = {"Content-Type": "application/json"}  # 定义请求头
        jsonData = jsonData
        # 发送登录请求
        response = self.login_api.login(jsonData, headers)
        # 打印登录的结果
        result = response.json()
        logging.info("登录的结果为:{}".format(result))
        # 使用封装的通用断言函数实现优化断言
        assert_common(http_code, success, code, message, response, self)

