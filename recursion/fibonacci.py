'''
@file		fibonacci.py
@author		Morgan Bergen
@date		March 28 2022
@brief		Exercise 3:  Good Old Fibonacci
   The Fibonacci sequence is a famous numerical series in which every number (after the first two) is the sum of the previous two numbers added together. The sequence is defined as...
   f(0) = 0
   f(1) = 1
   f(i) = f(i - 1) + f(i - 2)
   For your reference, here are the first few numbers in the Fibonacci sequence:
   
   ith		0  1  2  3  4  5  6  7  8  9  10 11
   value 	0  1  1  2  3  5  8  13 21 34 55 89

   Create a program that takes an integer and a mode from the user.
   The mode will indicate one of two options:
   -i mode
   Short for "ith" where the user wants to know the ith Fibonacci number
   (note the lowest valid would be zero)
   -v mode
   Short for "verify" where the user wants to know if the number given is in the Fibonacci sequence
'''

def main():
	user_input = input("Enter mode and value: ")
	user_input = user_input.split()
	if len(user_input) != 2:
		print("Invalid input, please re-intrepret this program and try again")
	else:
		mode = user_input[0]
		value = user_input[1]
		value = int(value)
		if mode == '-v':
			if verify(value, 0) == True:
				print(f"{value} is in the sequence")
			else:
				print(f"{value} is not in the sequence")
		elif mode == '-i':
			print(fib(value))


def verify(value, ith):
	if fib(ith) < value:
		return(verify(value, ith + 1))
	elif fib(ith) == value:
		return True
	elif fib(ith) > value:
		return False


def fib(n):
	if n == 0:
		return (0)
	elif n == 1:
		return (1)
	else:
		return (fib(n - 1) + fib(n - 2))

main()































