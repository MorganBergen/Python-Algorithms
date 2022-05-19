


from node import Node

class Tree:
	def __init__(self):
		self.root = None
		self.size = 0

	def fileio(self, p_file):
		in_stream = open(p_file, 'w')
		
		data = in_stream.read(10)
		print(data)


		in_stream.close()