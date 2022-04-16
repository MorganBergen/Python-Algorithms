'''
@file       main.py
@author     Morgan Bergen
@date       April 14 2022
@brief
'''

from map import Map
from blob import Blob

def main():
	
	obj = Blob()
	obj.traverse()
	
	map_obj = Map()
	map.prinMap()
	
	'''
	we must be able to catch runtimeerrors or file errors that generate a loop within the main and not for the Map class.  
	'''
	

if __name__ == "__main__":
	main()
