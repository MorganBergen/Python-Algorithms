'''
@file       main.py
@author     Morgan Bergen
@date       April 14 2022
@brief      the executive main which calls upon the input.txt file
'''

def main():

	run = False
	while run == False:
		file = input("file name: ")
		run = fileIO(file)
		
def fileIO(file):

	try:
		stream = open(file, 'r')
	except FileNotFoundError("error: file not found, please try again"):
		print(e)
		return False
	else:
		dimen = stream.readline().split()
		start = stream.readline().split()
		num_rows = int(dimen[0])
		num_cols = int(dimen[1])
		if num_rows < 1 or num_cols < 1:
			print("invalid")
			return False
		print("valid")
		return True

	
	
'''
✓ invalid file if the file does not exit
if numRows are less than 1
if numCols are less than 1
if start position is not within range
'''

if __name__ == "__main__":
	main()
