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
	exec.print()
	exec.indexes()
	exec.move()
	exec.print()

if __name__ == "__main__":
	main()
