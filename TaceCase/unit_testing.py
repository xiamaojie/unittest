from TaceCase.math_method import TestMethod     # todo 测试的目标类
import unittest


#1: 写用例 TestCaase
#2: 执行用例  1:TestSuite 存储用例  2:TestLoader 找用例，加载用例，存储到TestSuite里面
#3：对比实际结果和期望结果   断言Assert
#4：测试报告   htmltestrunner


class TestMathMethod(unittest.TestCase):
    '''测试数学方法'''

    # 编写用例
    # ：一个用例就是一个函数，不能传参，只有self关键字
    # ：所有用例已test_开头
    # ：运行时光标不能乱放，鼠标最好放末尾和开头
    def test_add_two_positive(self):
        '''测试2个正数相加'''
        result = TestMethod(3,3).add()
        print("3+3的结果值是：",result)

    def test_add_two_zero(self):
        '''测试2个0相加'''
        result = TestMethod(0,0).add()
        print("0+0的结果值是：",result)

    def test_add_two_negative(self):
        '''测试2个负数相加'''
        result = TestMethod(-3,-3).add()
        print("-3+-3的结果值是：",result)

if __name__ == '__main__':
    '''unittest的执行顺序为ascii编码，a-z的顺序执行'''
    unittest.main()