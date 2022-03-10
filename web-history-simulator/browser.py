

from linkedlist import LinkedList

class Browser:
	
	def __init__(self, file):
		self.history = LinkedList()
		self.file = file
		
	def fileIO(self):
		return(self.file)
		
	
	
	
	


'''
history.get_length()
history.is_empty()
history.get_entry(index, data)
histroy.clear()


raises index errors
	history.get_node_at(index)
	history.insert(index, data)
	history.get_entry(index)
	
raises runtime error and index error
	histroy.remove(index)
	
'''
