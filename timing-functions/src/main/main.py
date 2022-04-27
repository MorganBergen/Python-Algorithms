'''
@file		main.py
@author		Morgan Bergen
@date		
@brief	
'''

from one import One
from two import Two
from three import Three
from four import Four
from five import Five
from six import Six


'''
@pre		None
@post		None
@param		None
@raises		None
@returns	None
'''
def operationOne():
    test = One()
    test.execute()
    test.fileIO()

def operationTwo():
    test = Two()
    test.execute()
    test.fileIO()

def operationThree():
    test = Three()
    test.execute()
    test.fileIO()

def opertionFour():
    test = Four()
    test.execute()
    test.fileIO("four.txt")

def operationFive():
   test = Five()
   test.execute()
   test.fileIO("five.txt")

def main():
    test = Six()
    test.execute()
    test.generate_stats("six.txt")

main()