
# 通用断言函数
import json

from public import add

import app


def assert_common(httpcode, success, code, message, response, self):
    self.assertEqual(httpcode, response.status_code)  # 断言响应状态码
    self.assertEqual(success, response.json().get("success"))  # 断言success
    self.assertEqual(code, response.json().get("code"))  # 断言code
    self.assertIn(message, response.json().get("message"))  # 断言message


# 读取登录数据的函数
# 定义读取数据的函数，并从外界接收文件名
def read_login_data(filename):
    with open(filename,mode='r',encoding='utf8') as f:
        jsonData = json.load(f)
        # 定义一个存放数据的空列表
        result_list = list()
        for login_data in jsonData:
            result_list.append(tuple(login_data.values()))
    # print(result_list)
    return result_list

def read_employee_data(filename,name):
    with open(filename,mode='r',encoding='utf8') as f:
        jsonData = json.load(f)
        emp_data = jsonData.get(name)
        result_list = list()
        result_list.append(tuple(emp_data.values()))
    # print(result_list)
    return result_list

if __name__ == '__main__':
    filename = app.BASE_DIR + "/data/employee_data.json"
    read_employee_data(filename,"add_emp")
    read_employee_data(filename, "query_emp")
    read_employee_data(filename, "modify_emp")
    read_employee_data(filename, "delete_emp")