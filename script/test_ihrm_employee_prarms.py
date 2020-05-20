import logging
import unittest
import app
from utils import assert_common, read_employee_data
from parameterized import parameterized

class TestIHRMEmployee02(unittest.TestCase):
    # 初始化测试类
    def setUp(self):
        self.login_url = "http://ihrm-test.itheima.net" + "/api/sys/login"
        self.emp_url = "http://ihrm-test.itheima.net" + "/api/sys/user"
        from api.employee_api import TestEmployeeApi
        self.emp_api = TestEmployeeApi()  # 员工实例化
        from api.login_api import TestLoginApi
        self.login_api = TestLoginApi()  # 登录实例化

    # 编写测试用例
    def test_01_login(self):
        # 登录
        response = self.login_api.login({"mobile": "13800000002", "password": "123456"},
                                        {"Content-Type": "application/json"})
        # 打印登录的数据
        logging.info("登录的结果为：{}".format(response.json()))
        # 提取令牌
        token = response.json().get("data")
        # 保存令牌到请求头当中
        headers = {"Content-Type": "application/json", "Authorization": "Bearer " + token}
        app.HEADERS = headers
        # 打印令牌
        logging.info("请求头中令牌：{}".format(app.HEADERS))
    # 添加员工
    filename = app.BASE_DIR + "/data/employee_data.json"
    @parameterized.expand(read_employee_data(filename,"add_emp"))
    def test_02_add_emp(self,username,mobile,http_code,success,code,message):
        response = self.emp_api.add_emp(app.HEADERS,username,mobile)
        # 打印添加的结果
        logging.info("添加员工的结果为:{}".format(response.json()))
        # 提取添加员工中的id
        emp_id = response.json().get("data").get("id")
        app.EMP_ID = emp_id
        # 断言
        assert_common(http_code, success, code, message, response, self)
    # 查询员工
    filename = app.BASE_DIR + "/data/employee_data.json"
    @parameterized.expand(read_employee_data(filename,"query_emp"))
    def test_03_query_emp(self,http_code,success,code,message):
        response = self.emp_api.query_emp(app.EMP_ID, app.HEADERS)
        logging.info("查询员工的结果为:{}".format(response.json()))
        # 断言
        assert_common(http_code, success, code, message, response, self)
    # 修改员工
    filename = app.BASE_DIR + "/data/employee_data.json"
    @parameterized.expand(read_employee_data(filename,"modify_emp"))
    def test_04_modify_emp(self,username,http_code,success,code,message):
        response = self.emp_api.modify_emp(app.EMP_ID,app.HEADERS,username)
        # 打印修改的结果
        logging.info("修改员工的结果为:{}".format(response.json()))
        # 断言
        assert_common(http_code, success, code, message, response, self)
    # 删除员工
    filename = app.BASE_DIR + "/data/employee_data.json"
    @parameterized.expand(read_employee_data(filename,"delete_emp"))
    def test_05_delete_emp(self,http_code,success,code,message):
        response = self.emp_api.delete_emp(app.EMP_ID,app.HEADERS,)
        # 打印删除的结果
        logging.info("删除的结果为:{}".format(response.json()))
        # 断言
        assert_common(http_code, success, code, message, response, self)

