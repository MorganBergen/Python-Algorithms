'''
@file		browser.py
@author		Morgan Bergen
@date		March 11 2022
@brief  	This is the Browser class
			The purpose of this class is to mimic the behavior of a web browser's back button, forward button, and address bar.
			The following defines the general functionality of methods for the Browser class.
			
			def __init__(self)
			- Initializes the Browser
			- generates an empty linkedlist object
			- defines and stores a file for which the browser will be refering to for command behvaior
			- initizes a current page to 0, to be defined as the 0th index position in the empty linkedlist
			
			def navigate_to(self, url)
			- The browser navigate to the given url
			- This method will store a given url into the end of the linkedlist if the current page is equal to that of the self.web_history.get_length() - 1
			- Navigating to a URL retains all URLs accessible from going BACK
			- However URLs that would have accessible from going FORWARD are would be lost
			
			def back(self)
			- If possible, the browser navigates backwards in the history otherwise it keeps focus
			- This method is called when a command indicating the web browser is redirected to the previous URL in the history.
			- If there is no URL further back, then the browser stays on the current URL.
			- Essentially if it is possible for the browser to go back a page, then current is decremented by obne.
			
			def forward(self)
			- If possible, the browser navigates forward in the history otherwise it keeps focus
			- This method is called when a command indicating the web browser is redirected to the next URL in the history.
			- If there is no URL that is next, then the browser stays on the current URL.
			- Essentially if it is possible for the browser to go forward a page, then current is incremented by one.
			
			def history(self)
			- Prints the URL history to the screen.
'''

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
		self.web_history.clear()
