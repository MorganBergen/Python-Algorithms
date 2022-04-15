'''
@file       main.py
@author     Morgan Bergen
@date       April 14 2022
@brief      the executive main which calls upon the input.txt file
'''

from map import Map
from blob import Blob

def main():
	
	obj = Blob()
	print(obj.name)
	
	obj.destory(4)



if __name__ == "__main__":
	main()
