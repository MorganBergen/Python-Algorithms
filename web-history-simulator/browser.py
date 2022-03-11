

from linkedlist import LinkedList

class Browser:
	
	def __init__(self, file):
		self.web = LinkedList() #self.web_history rename after youre done
		self.current = 0
		self.file = file
		
		
	def navigate_to(self, url):
		if self.web.is_empty():
			self.web.insert(0, url)
			self.current = 0
		
		elif (self.web.get_length() - 1) == self.current:
			self.web.insert(self.web.get_length(), url)
			self.current = self.web.get_length() - 1
		# length = 6, current = 2
		# remove index 3, 4, 5
		# position = 3
		# remove(3)
		# remove (4)
		# remove(5)
		else:
			position = self.current + 1
			for position in range(self.web.get_length()):
				self.web.remove(position)
		# current = 2
		# current = 2 + 1
		# insert (3, url)
			self.current = self.current + 1
			self.web.insert(self.current, url)
		self.history()
			
	def back(self):
	def forward(self):
	def history(self):
		print("Oldest")
		print("===========")
		for i in range self.web.get_length():
			if i == self.current:
				print(f"{i} {self.web.get_entry(i)} <== current {self.current}")
			else:
				print(f"{i} {self.web.get_entry(i)}")
		print("===========")
		print("Newest")
		
	def tester(self):
		self.web.navigate
	
	
	
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
