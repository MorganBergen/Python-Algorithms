

from linkedlist import LinkedList

class Browser:
	
	def __init__(self, file):
		self.history = LinkedList()
		self.file = file
		self.current = -1
		
	def navigate(self, command, url):
		self.current = self.current + 1
		if self.history.is_empty():
			self.history.insert(self.history.get_length(), url)
		else:
			self.history.insert(self.history.get_length(), url)
		
		
	def print(self, command):
		if self.history.is_empty():
			print("Oldest")
			print(self.current)
			print("===========")
			print("===========")
			print("Newest")
		else:
			print("Oldest")
			print("===========")
			for i in range(self.history.get_length()):
				if i == self.current:
					print(f"{self.history.get_entry(i)} <==current {self.current}")
				else:
					print(self.history.get_entry(i))
			
			print("===========")
			print("Newest")
		
	def back(self, command):
		self.current = self.current - 1
		
		
	def forward(self, command):
		self.current = self.current + 1
		print(self.current)
	
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
