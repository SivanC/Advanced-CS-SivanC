import unittest
import random

class numTests(unittest.TestCase):
    
    def set_up(self, value):
        self.value = value
        
    def tear_down(self):
        self.value.dispose()
        self.value = None
        
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

test = numTests()
suite = numTests.suite(test)
unittest.TextTestRunner(verbosity=2).run(suite)