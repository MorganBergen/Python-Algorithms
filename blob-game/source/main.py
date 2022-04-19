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
	exec.indexes()
	exec.start()
	
	exec.print()
	
	exec.move(0, 2)
	
	exec.print()

if __name__ == "__main__":
	main()
