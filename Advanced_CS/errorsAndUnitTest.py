import unittest

class numTests(unittest.TestCase):
    
    def __init__(self, value):
        self.value = value
        
    def test_isNum(self):
        try:
            int(self.value)
            return True
        except ValueError:
            return False
            
    def test_isEven(self):
        if self.value % 2 == 0:
            return True
        else:
            return False
            
    def suite(self):
        suite = unittest.TestSuite
        suite.addTest(numTests('test_isNum', 4))
        suite.addTest(numTests('test_isEven', 4))
        
if __name__ == '__main__':
    unittest.main()

#test = numTests()
#suite = numTests.suite(test)
#unittest.TextTestRunner(verbosity=2).run(suite)