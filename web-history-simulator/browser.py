
from linkedlist import LinkedList

class Browser:
	
	def __init__(self, file):
		self.web_history = LinkedList()
		self.current = 0
		self.file = file
	
	def navigate_to(self, url):
		if self.web_history.is_empty():
			self.web_history.insert(0, url)
			self.current = 0
		
		elif (self.web_history.get_length() - 1) == self.current:
			self.web_history.insert(self.web_history.get_length(), url)
			self.current = self.web_history.get_length() - 1
		else:
			for x in reversed(range(self.current+1, self.web_history.get_length())):
				self.web_history.remove(x)
			self.current = self.current + 1
			self.web_history.insert(self.current, url)
	
	def back(self):
		if self.current != 0:
			self.current = self.current - 1
	
	def forward(self):
		if self.current != self.web_history.get_length() - 1:
			self.current = self.current + 1
	
	
	def history(self):
		print("Oldest")
		print("===========")
		for i in range(self.web_history.get_length()):
			if i == self.current:
				
				print(f"{self.web_history.get_entry(i)}", end="")
				print(f" <== current")
			else:
				print(self.web_history.get_entry(i))
		print("===========")
		print("Newest")
	
	def fileIO(self):
		in_file = open(self.file)
		for line in in_file:
			command = line.split()
			if command[0] == "NAVIGATE":
				self.navigate_to(command[1])
			
			elif command[0] == "HISTORY":
				self.history()
			
			elif command[0] == "BACK":
				self.back()
			
			elif command[0] == "FORWARD":
				self.forward()
		in_file.close()
