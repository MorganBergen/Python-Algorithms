

from linkedlist import LinkedList

class Browser:
	
	def __init__(self, file):
		self.web_history = LinkedList()
		self.file = file
		self.current = -1
		
	def navigate_to(self, command, url):
		
	def back(self, command):
		
	def forward(self, command):
		
	def print(self, command):
	
	
	def fileIO(self):
		
		in_file = open(self.file)
		
		for line in in_file:
			command = line.split()
			if command[0] == "NAVIGATE":
				self.navigate(command[0], command[1])
				
			elif command[0] == "HISTORY":
				self.print(command[0])
				
			elif command[0] == "BACK":
				self.back(command[0])
				
			elif command[0] == "FORWARD":
				self.forward(command[0])
			
		in_file.close()
	


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
