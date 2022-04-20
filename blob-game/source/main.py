'''
@file       main.py
@author     Morgan Bergen
@date       April 14 2022
@brief
'''

from map import Map
from blob import Blob

def main():
	exec = Blob()
	print()
	
#	exec.start()
	
	exec.indexes()
	exec.print()
	exec.move(0, 2)
	
	

if __name__ == "__main__":
	main()
