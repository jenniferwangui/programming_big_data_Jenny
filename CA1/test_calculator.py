# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

student No.10223591

"""

import unittest

from Calculator import *

class MyTest(unittest.TestCase):

    def setUp(self):
        self.Calculator = Calculator()
        
    def testAddation(self):
        self.assertEqual(0, self.Calculator.getAddation())
        self.Calculator.setAddation(2, 4)
        self.assertEqual(6, self.Calculator.getAddation())
        self.Calculator.setAddation(-10, 4)
        self.assertEqual(-6, self.Calculator.getAddation())
        self.Calculator.setAddation(6, -4)
        self.assertEqual(2, self.Calculator.getAddation())
        
    def testSubtraction(self):
        self.assertEqual(0, self.Calculator.getSubtraction())
        self.Calculator.setSubtraction(8, 4)
        self.assertEqual(4, self.Calculator.getSubtraction())
        self.Calculator.setSubtraction(-8, 4)
        self.assertEqual(-12, self.Calculator.getSubtraction())
        self.Calculator.setSubtraction(4, 4)
        self.assertEqual(0, self.Calculator.getSubtraction())
        
    def testMultiplication(self):
        self.assertEqual(0, self.Calculator.getMultiplication())
        self.Calculator.setMultiplication(4, 4)
        self.assertEqual(16, self.Calculator.getMultiplication())    
        self.Calculator.setMultiplication(-4, 4)
        self.assertEqual(-16, self.Calculator.getMultiplication())
        self.Calculator.setMultiplication(0, 4)
        self.assertEqual(0, self.Calculator.getMultiplication()) 
        self.Calculator.setMultiplication(-4, -4)
        self.assertEqual(16, self.Calculator.getMultiplication())
        
        
    def testDivision(self):
        self.assertEqual(0, self.Calculator.getDivision())
        self.Calculator.setDivision(24, 4)
        self.assertEqual(6, self.Calculator.getDivision())
        self.Calculator.setDivision(-24, 4)
        self.assertEqual(-6, self.Calculator.getDivision())
        
    
    def testExponential(self):
        self.assertEqual(0, self.Calculator.getExponential())
        self.Calculator.setExponential(2, 6)
        self.assertEqual(64, self.Calculator.getExponential())    
        self.Calculator.setExponential(-2, 4)
        self.assertEqual(16, self.Calculator.getExponential())  
        self.Calculator.setExponential(2, -6)
        self.assertEqual(0, self.Calculator.getExponential())  
        
    def testSquareroot(self):
        self.assertEqual(0, self.Calculator.getSquareroot())
        self.Calculator.setSquareroot(25)
        self.assertEqual(5, self.Calculator.getSquareroot())
        self.Calculator.setSquareroot(10)
        self.assertEqual(3.0, self.Calculator.getSquareroot())
        self.Calculator.setSquareroot(2)
        self.assertEqual(1, self.Calculator.getSquareroot())
        
    def testSin(self):
        self.assertEqual(0, self.Calculator.getSin())
        self.Calculator.setSin(90)
        self.assertEqual(1, self.Calculator.getSin()) 
        self.Calculator.setSin(-90)
        self.assertEqual(-1, self.Calculator.getSin())
        self.Calculator.setSin(25)
        self.assertEqual(0, self.Calculator.getSin())    
    
    def testCos(self):
        self.assertEqual(0, self.Calculator.getCos())
        self.Calculator.setCos(25)
        self.assertEqual(1, self.Calculator.getCos())
        self.Calculator.setCos(90)
        self.assertEqual(0, self.Calculator.getCos())
        self.Calculator.setCos(95)
        self.assertEqual(1, self.Calculator.getCos())    
    
    def testTan(self):
        self.assertEqual(0, self.Calculator.getTan())
        self.Calculator.setTan(90)
        self.assertEqual(-2, self.Calculator.getTan())
        self.Calculator.setTan(50)
        self.assertEqual(0, self.Calculator.getTan())
        self.Calculator.setTan(95)
        self.assertEqual(1, self.Calculator.getTan())    
    
    def testCuberoot(self):
        self.assertEqual(0, self.Calculator.getCuberoot())
        self.Calculator.setCubeRoot(25)
        self.assertEqual(3, self.Calculator.getCuberoot())
        self.Calculator.setCubeRoot(5)
        self.assertEqual(2, self.Calculator.getCuberoot())
        self.Calculator.setCubeRoot(50)
        self.assertEqual(4, self.Calculator.getCuberoot())
        
if __name__ == '__main__':
    unittest.main()        
