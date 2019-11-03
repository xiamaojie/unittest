from TaceCase.unit_testing import TestMathMethod
import unittest


suite = unittest.TestSuite()  # todo 实例化对象，存储用例

# 方法1
# 执行单条用例，传用例(函数)名称
#suite.addTest(TestMathMethod.test_add_two_positive)

# 方法2 TestLoader创建一个加载器
loader = unittest.TestLoader()
# TODO 传执行的类名
suite.addTest(loader.loadTestsFromTestCase(TestMathMethod))

from TaceCase import unit_testing
# TODO 传执行的.py模块名
#suite.addTest(loader.loadTestsFromModule(unit_testing))

# 执行
runner = unittest.TextTestRunner()
runner.run(suite)