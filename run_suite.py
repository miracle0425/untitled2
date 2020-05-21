import unittest
import app
from script.test_ihrm_employee_prarms import TestIHRMEmployee02
from script.test_ihrm_login_prarms import TestIHRMLogin
import HTMLTestRunner_PY3
# 创建测试套件
suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestIHRMLogin))
suite.addTest(unittest.makeSuite(TestIHRMEmployee02))

report_name = app.BASE_DIR + "/report/ihrm.html"

with open(report_name,"wb") as f:
    runner = HTMLTestRunner_PY3.HTMLTestRunner(f,verbosity=2,title="IHRM接口测试报告",description="这是人力资源管理系统的测试报告")
    runner.run(suite)

print("测试新增一行代码，会不会触发轮训构建3")
print("--" * 10)