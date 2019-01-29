import sys
import unittest
from src.main import Craddle


class Test_Expressions(unittest.TestCase):

    craddle = None
    """ Test global variables """
    @classmethod
    def setUp(cls):
        craddle = Craddle('a') 
        craddle.tokenize()       
        return 
    
    @classmethod
    def tearDown(cls):
        return super().tearDown()

    def test_01_constants(self):
        craddle = Craddle('-a') 
        craddle.tokenize()       

    def test_02_(self):
        craddle = Craddle('a+b') 
        craddle.tokenize()       

    def test_03_(self):
        craddle = Craddle('a-b') 
        craddle.tokenize()       

    def test_04_(self):
        craddle = Craddle('a+b-c') 
        craddle.tokenize()       

    def test_05_(self):
        craddle = Craddle('a-b+d') 
        craddle.tokenize()       

    def test_06_(self):
        craddle = Craddle('(a+b)-d') 
        craddle.tokenize()       

    def test_07_(self):
        craddle = Craddle('a+(b-d)') 
        craddle.tokenize()       

    


if __name__ == '__main__':
    unittest.main()    