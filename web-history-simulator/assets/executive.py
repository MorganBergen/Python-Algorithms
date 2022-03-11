'''
@file		executive.py
@author		Morgan Bergen
@date		March 11 2022
@brief		This is the excecutive class which generates the Browser object.
'''

from browser import Browser


class Executive:
	
	def __init__(self, file):
		self.exec = Browser(file)
		self.exec.fileIO()
