
from one import One
from two import Two
from three import Three
from four import Four
from five import Five
from six import Six

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
    


main()