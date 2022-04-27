'''
@file		main.py
@author		Morgan Bergen
@date		April 27 2022
@brief	    This is the executive file which will run all the operations for testing the time complexities for specific data structures
            operationOne() will test the time complexity of a single pop() for ADT stack
            operationTwo() will test the time complexity of all possible pop() for ADT stack
            operationThree() will test the time complexity of enqueue() for ADT queue
            operationFour() will test the time complexity of get_entry(0) for ADT linkedList
            operationFive() will test the time complexity of get_entry(list.size-1) for ADT linkedList
            operationSix() will test the time complexity of print_list() using get_entry() for ADT linkedList
'''

import sys
sys.path.insert(0, './test_1')
sys.path.insert(0, './test_2')
sys.path.insert(0, './test_3')
sys.path.insert(0, './test_4')
sys.path.insert(0, './test_5')
sys.path.insert(0, './test_6')

from one import One
from two import Two
from three import Three
from four import Four
from five import Five
from six import Six

'''
@pre	    None
@post		popping a single item from a stack
@param		None
@raises		None
@returns	None
'''
def operationOne():
    test = One()
    test.execute()
    test.generate_statistics("test_1/statistics.txt")

'''
@pre	    None
@post		popping all items from a stack
@param		None
@raises		None
@returns	None
'''
def operationTwo():
    test = Two()
    test.execute()
    test.generate_statistics("test_2/statistics.txt")

'''
@pre	    None
@post		generates a file which contains the time complexity of the queue's enqueue
@param		None
@raises		None
@returns	None
'''
def operationThree():
    test = Three()
    test.execute()
    test.fileIO("three_statistics.txt")

def operationFour():
    test = Four()
    test.execute()
    test.fileIO("four_statistics.txt")

def operationFive():
   test = Five()
   test.execute()
   test.fileIO("five_statistics.txt")

def operationSix():
    test = Six()
    test.execute()
    test.generate_stats("six_statistics.txt")
    
def main():
    operationOne()
    # operationTwo()
    # operationThree()
    # operationFour()
    # operationFive()
    # operationSix()


if __name__ == "__main__":
    main()
