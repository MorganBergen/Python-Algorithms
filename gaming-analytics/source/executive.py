'''
@file		executive.py
@author		Morgan Bergen
@date		February 2 2022
@brief		This is the executive class
			The member variables store the file name and game objects.
			The member methods performs file I/O, prints the options menu, recieves input from the user, and performs tasks for each option.
'''

from math import ceil
from re import A, S
from boardgame import Boardgame

class Executive:
	
	def __init__(self, p_file):
		self.m_file = p_file
		self.game_object = Boardgame()

	def run(self):

		try:
			self.fileIO(self.m_file)
		except FileNotFoundError:
			print("Error: File not found please try again.")
			return(0)

		self.printMenu()
		self.userInterface()

	def printMenu(self):
		welcome = "Welcome to the Board Games Program!"
		prompt = "Select from the following menu options"
		option1 = "1. Print all games (same order as from file)"
		option2 = "2. Print all games from a year"
		option3 = "3. Print a ranking range"
		option4 = "4. The People VS Dr. Gibbons"
		option5 = "5. Print based on play time"
		option6 = "6. Exit the program"
		print(f"\n{welcome}\n\n{prompt}")
		print(f"\t{option1}\n\t{option2}\n\t{option3}\n\t{option4}\n\t{option5}\n\t{option6}")

	def fileIO(self, p_file):
		inFile = open(p_file)		
		for line in inFile:
			temp = line.split()	
			for i in range(len(temp)):
				if i == 0:
					self.game_object.setName(temp[i])					
				elif i == 1:
					self.game_object.setYear(temp[i])					
				elif i == 2:
					self.game_object.setGR(temp[i])					
				elif i == 3:
					self.game_object.setPR(temp[i])				
				elif i == 4:
					self.game_object.setMP(temp[i])
				elif i == 5:
					self.game_object.setMT(temp[i])					
				else:
					print("Error: Incompatable file provided")
					exit(1)
			
		inFile.close()

	def userInterface(self):
		option = input("Enter Option Number: ")
		option = int(option)
		if option == 6:
			exit(1)
		elif option == 1:
			self.option1()
		elif option == 2:
			self.option2()
		elif option == 3:
			self.option3()
		elif option == 4:
			self.option4()
		elif option == 5:
			self.option5()
		else:
			print("\nError: Invalid option, please try again.\n")
			self.userInterface()

	def option1(self):
		names = self.game_object.getName()
		years = self.game_object.getYear()
		gr = self.game_object.getGR()
		pr = self.game_object.getPR()
		mp = self.game_object.getMP()
		mt = self.game_object.getMT()
		total = ((len(names) + len(years) + len(gr) + len(pr) + len(mp) + len(mt))/6)

		for i in range(int(total)):
			print(f"{names[i]} ({years[i]}) [GR={gr[i]}, PR={pr[i]}, MP={mp[i]}, MT={mt[i]}]")

	def option2(self):

		user_year = input("\nEnter Year: ")
		names = self.game_object.getName()
		years = self.game_object.getYear()
		gr = self.game_object.getGR()
		pr = self.game_object.getPR()
		mp = self.game_object.getMP()
		mt = self.game_object.getMT()

		found = False

		for i in range(len(years)):
			if years[i] == user_year:
				print(f"{names[i]} ({years[i]}) [GR={gr[i]}, PR={pr[i]}, MP={mp[i]}, MT={mt[i]}]")
				found = True				
				
		if found == False:
			print("No games found")

	def option3(self):
		print("\nPlease input a Gibbons Ranking Range (i.e. floor - ceiling) (e.g. 1 - 10)")
		user_floor = input("Enter floor: ")
		user_ceiling = input("Enter ceiling: ")
		user_floor = float(user_floor)
		user_ceiling = float(user_ceiling)

		names = self.game_object.getName()
		years = self.game_object.getYear()
		gr = self.game_object.getGR()
		pr = self.game_object.getPR()
		mp = self.game_object.getMP()
		mt = self.game_object.getMT()

		found = False

		for i in range(len(gr)):
			if float(gr[i]) <= (user_ceiling) and float(gr[i]) >= (user_floor):
				print(f"{names[i]} ({years[i]}) [GR={gr[i]}, PR={pr[i]}, MP={mp[i]}, MT={mt[i]}]")
				found = True

		if found == False:
			print("No games found")
	
	def option4(self):
		print("\nThe People VS Dr. Gibbons Instructions:")
		print("Enter a number (0 - 10, decimals allowed)\nthe following will then print all games where\nthe People's rating and Dr. Gibbons rating\nare separated by how much you entered or more.")
		user_input = input("\nEnter a Ratings Difference: ")
		user_input = float(user_input)

		names = self.game_object.getName()
		years = self.game_object.getYear()
		gr = self.game_object.getGR()
		pr = self.game_object.getPR()
		mp = self.game_object.getMP()
		mt = self.game_object.getMT()

		found = False

		for i in range(len(gr)):
			difference = abs(float(gr[i]) - float(pr[i]))
			if difference >= user_input:
				print(f"{names[i]} ({years[i]}) [GR={gr[i]}, PR={pr[i]}, MP={mp[i]}, MT={mt[i]}]")
				found = True
		
		if found == False:
			print("No games found")

	def option5(self):
		print("\nPlease input a playtime (in minutes) and the following\nwill have a min playtime of your value or lower")
		user_time = input("\nEnter playtime: ")
		if user_time.isdigit() == False:
			print("Error: invalid input please try again.")
			self.option5()

		names = self.game_object.getName()
		years = self.game_object.getYear()
		gr = self.game_object.getGR()
		pr = self.game_object.getPR()
		mp = self.game_object.getMP()
		mt = self.game_object.getMT()

		found = False

		for i in range(len(mt)):
			if int(mt[i]) <= int(user_time):
				print(f"{names[i]} ({years[i]}) [GR={gr[i]}, PR={pr[i]}, MP={mp[i]}, MT={mt[i]}]")
				found = True
		
		if found == False:
			print("No games found")
