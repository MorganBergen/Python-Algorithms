
from browser import Browser


class Executive:
	
	def __init__(self, file):
		self.exec = Browser(file)
		self.exec.fileIO()
