# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 15:01:55 2017

@author: Jennifer

student No. 10223591
"""


# class for calculator

class Calculator(object):
    
#constructor    
    def __init__(self):
        self.__addation = 0
        self.__subtraction = 0
        self.__multiplication = 0
        self.__division = 0
        self.__exponential = 0
        self.__squareroot = 0
        self.__sin = 0
        self.__cos = 0
        self.__tan = 0
        self.__cuberoot = 0
        
#getters and setters for every function
        
    def setAddation(self, value1, value2):
        self.__addation = value1 + value2
    
    def getAddation(self):
        return self.__addation
        
    def setMultiplication(self, value1, value2):
        self.__multiplication = value1 * value2
    
    def getMultiplication(self):
        return self.__multiplication    
    
    def setDivision(self, value1, value2):
        if value2 == 0:
            return 'undefined'
        
        else:    
            self.__division = value1 / value2
    
    def getDivision(self):
        return self.__division
        
    def setSubtraction(self, value1, value2):
        self.__subtraction = value1 - value2
    
    def getSubtraction(self):
        return self.__subtraction 
        
    def setExponential(self, value1, value2):
        self.__exponential = round(value1 ** value2)
    
    def getExponential(self):
        return self.__exponential 
    
    def setSquareroot(self, value):
        self.__squareroot = round(value ** (1.0/2.0))
    
    def getSquareroot(self):
        return self.__squareroot
    
    def setSin(self, value):
        import math
        self.__sin = round(math.sin(value))
        
    def getSin(self):
        return self.__sin
    
    def setCos(self, value):
        import math
        self.__cos = round(math.cos(value))
        
    def getCos(self):
        return self.__cos
        
    def setTan(self, value):
        import math
        self.__tan = round(math.tan(value))
        
    def getTan(self):
        return self.__tan    
    
    def setCubeRoot(self, value):
        self.__cuberoot = round(value ** (1.0/3.0))
    
    def getCuberoot(self):
        return self.__cuberoot
    
