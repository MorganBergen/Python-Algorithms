'''
@file		boardgame.py
@author		Morgan Bergen
@date		February 2 2022
@brief		This is the boardgame class
			The member variables store data from the input file.
			The member methods initialize and return the data.
'''

class Boardgame:
	def __init__(self):
		self.m_name = []
		self.m_year = []
		self.m_gr = []
		self.m_pr = []
		self.m_mp = []
		self.m_mt = []
		
	def setName(self, p_name):
		self.m_name.append(p_name)
		
	def getName(self):
		return(self.m_name)

	def setYear(self, p_year):
		self.m_year.append(p_year)
	
	def getYear(self):
		return(self.m_year)
		
	def setGR(self, p_gr):
		self.m_gr.append(p_gr)
	
	def getGR(self):
		return(self.m_gr)
	
	def setPR(self, p_pr):
		self.m_pr.append(p_pr)
		
	def getPR(self):
		return(self.m_pr)
		
	def setMP(self, p_mp):
		self.m_mp.append(p_mp)
		
	def getMP(self):
		return(self.m_mp)
		
	def setMT(self, p_mt):
		self.m_mt.append(p_mt)
		
	def getMT(self):
		return(self.m_mt)
