'''
@file
@author
@date
@brief
'''

from re import S
from matplotlib import lines

def main():
    file_name = input("Enter file name: ")
    file(file_name)

def file(name):
    fo = open(name, "")

main()


'''
lines = list()

    with open(name, mode="r") as f:
        lines f.readlines()

    for line in lines:
        print(lines)
'''˝˝