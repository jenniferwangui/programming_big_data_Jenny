# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 15:00:23 2017

@author: Jennifer
student No. 10223591

"""



from Calculator import *

def show_menu():
   print "#####################################"
   print "Select 1 for Addition"
   print "Select 2 for Subtraction"
   print "Select 3 for division"
   print "Select 4 for Multiplication"
   print "Select 5 for Exponential"
   print "Select 6 for Square-root"
   print "Select 7 for Sin"
   print "Select 8 for Cos"
   print "Select 9 for Tan"
   print "Select 10 for Cube-root"
   print "#####################################"

#menu for the user to make a choice on available functions of calculator provided

show_menu()
s_input = raw_input("Input menu choice> ")
choice = int(s_input)

def get_userinput(user_prompt): 
     
    str_inp = raw_input(user_prompt)   
    f1_scores = float(str_inp)  
     
    return f1_scores 
    
# calculator compute from user choice
    
if choice == 1:
   value1 = get_userinput('Enter your values\n')
   value2 = get_userinput('Enter the second value\n')
   myCalculator = Calculator()
   myCalculator.setAddation(value1, value2)
   result = myCalculator.getAddation()
   print 'Your answer is ', result

elif choice == 2:
   value1 = get_userinput('Enter your values\n')
   value2 = get_userinput('Enter the second value\n')
   myCalculator = Calculator()
   myCalculator.setSubtraction(value1, value2)
   result = myCalculator.getSubtraction()
   print 'Your answer is ', result   
    
elif choice == 3:
   value1 = get_userinput('Enter your values\n')
   value2 = get_userinput('Enter the second value\n')
   myCalculator = Calculator()
   myCalculator.setDivision(value1, value2)
   result = myCalculator.getDivision()
   print 'Your answer is ', result
   
elif choice == 4:
   value1 = get_userinput('Enter your values\n')
   value2 = get_userinput('Enter the second value\n')
   myCalculator = Calculator()
   myCalculator.setMultiplication(value1, value2)
   result = myCalculator.getMultiplication()
   print 'Your answer is ', result    

elif choice == 5:
   value1 = get_userinput('Enter your values\n')
   value2 = get_userinput('Enter the second value\n')
   myCalculator = Calculator()
   myCalculator.setExponential(value1, value2)
   result = myCalculator.getExponential()
   print 'Your answer is ', result   

elif choice == 6:
   value = get_userinput('Enter your values\n')
   myCalculator = Calculator()
   myCalculator.setSquareroot(value)
   result = myCalculator.getSquareroot()
   print 'Your answer is ', result    
    
elif choice == 7:
   value = get_userinput('Enter your values\n')
   myCalculator = Calculator()
   myCalculator.setSin(value)
   result = myCalculator.getSin()
   print 'Your answer is ', result
   
elif choice == 8:
   value = get_userinput('Enter your values\n')
   myCalculator = Calculator()
   myCalculator.setCos(value)
   result = myCalculator.getCos()
   print 'Your answer is ', result   

elif choice == 9:
   value = get_userinput('Enter your values\n')
   myCalculator = Calculator()
   myCalculator.setTan(value)
   result = myCalculator.getTan()
   print 'Your answer is ', result
   
elif choice == 10:
   value = get_userinput('Enter your values\n')
   myCalculator = Calculator()
   myCalculator.setCubeRoot(value)
   result = myCalculator.getCuberoot()
   print 'Your answer is ', result
else:
    print 'Invalid input'

    


