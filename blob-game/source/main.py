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
	
	works = False
	
	
	
	try:
#		stream = open(file, 'r')
		fo = open(file, 'r')
		decrepid = open("fatal.txt", 'r')
	except FileNotFoundError as e:
		print(e)
	finally:
		print("name of file is ", fo.name)
		dimensions = fo.readline().split()
		start_dimensions = fo.readline().split()
		numRows = dimensions[0]
		numCols = dimensions[1]
		startRow = start_dimensions[0]
		startCol = start_dimensions[1]
		map = fo.read().splitlines()
		print(f"startRow = {startRow}")
		print(f"startCol = {startCol}")
		print(f"numRows = {numRows}")
		print(f"numCols = {numCols}")
		print(map)
		fo.close()
		print("closed ", fo.closed)



main()
