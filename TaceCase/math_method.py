
class TestMethod():
    # 编写用例
    #：一个用例就是一个函数，不能传参，只有self关键字
    #：所有用例已test_开头
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def add(self):
        '''加法'''
        return self.a+self.b

    def multi(self):
        '''乘法'''
        return self.a*self.b