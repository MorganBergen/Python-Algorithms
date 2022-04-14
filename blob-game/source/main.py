'''
@file       main.py
@author     Morgan Bergen
@date       April 14 2022
@brief      the executive main which calls upon the input.txt file
'''

def main():
    f_name = input("enter file name: ")
    fileIO(f_name)


def fileIO(file):
    in_file = open(file)



main()