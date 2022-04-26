
from one import One
from two import Two
from three import Three
from four import Four
from five import Five

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

def opertionFive():
    test = Five()

def main():
    print()
    x = Four()
    x.execute()
    # x.fileIO("four.txt")
    


main()