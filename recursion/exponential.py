'''
@file		exponential.py
@author		Morgan Bergen
@date		March 28 2022
@brief		Exercise 1:  Recursive Power Function
			Create a program that takes in a base and exponent for the user. If the input is valid, it prints the answer of the base taken to the power given. You must require the user to give ints for both the base and the exponent. Also, the exponent must be zero or larger.
			rec_func
			base case/terminating case is if power is 0
			recursive case is
			
'''

def main():

	valid = False
	base = input("Enter a base: ")
	power = input("Enter a power: ")
	while valid == False:
	
		try:
			base = int(base)
			valid = True
		except ValueError as e:
			print(f"Sorry, your base must be an integer.")
			base = input("Enter a base: ")
			
		try:
			power = int(power)
			if power < 0:
				print("Sorry, your exponent must be zero or larger.")
				power = input("Enter a power: ")
				valid = False
			else:
				valid = True
		except ValueError as e:
			print(f"Sorry, your power must be an integer")
			power = input("Enter a power: ")
	
	print(f"Answer: {rec_func(base, power)}")
	
def rec_func(base, power):
	if power == 0:
		return (1)
	elif power > 0:
		return (rec_func(base, power - 1) * base)
		
main()
