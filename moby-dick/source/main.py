'''
@file		main.py
@author		Morgan Bergen
@date		February 17 2022
@brief		this main.py contains the following functions which are called via main()
			The purpose of this program is to process the text Moby Dick and provide two output files
			word_data.txt contains the words and their corresponding counts
			unique_words.txt contains a listing (no counts) of all words that appear exactly once
			main() is in charge of calling the following functions
			prompt()
			clean_word(word)
			build_count(text)
			unique_words(p_dictionary)
			fileInput(p_file)
			word_data_FIO(p_dictionary)
			unique_words_FIO(p_list)
'''

import string
from collections import Counter

'''
@pre     mobydick.txt must exist in the same file path as main.py
@param   none
@throws  none
@returns none
'''
def main():
	text = prompt()
	dictionary = build_count(text)
	word_data_FIO(dictionary)
	list = unique_words(dictionary)
	unique_words_FIO(list)

'''
@pre     file name must be provided
@param   none
@throws  none
@returns file_string - the name of the the file inputted by the user
'''
def prompt():
	print("===========Welcome to the word counter!===========")
	file_name = input("Enter a file name: ")
	file_string = fileInput(file_name)
	print(f"The file {file_name} has been processed.")
	print(f"Output has been stored in word_data.txt and unique_words.txt")
	print("Exiting...")
	return(file_string)

'''
@pre	 build_count must have been called with the contents of the mobydick.txt allocated within a string
@param   word which is a string of each instance of a word in the mobydick.txt
@throws  none
@returns word is cleaned and altered with the following changes
   converted to all lower-case
   all occurrences of '!', '?', ':', ';', ',', '|', '.', and '--' (those are two dashes side-by-side) are removed
   all leading and trailing whitespace are removed
'''
def clean_word(word):
	word = word.casefold()
	word = word.strip()
	word = word.strip("'")
	word = word.strip("]")
	word = word.strip("[")
	if '!' in word:
		word = word.replace('!', "")
	if '?' in word:
		word = word.replace('?', "")
	if ':' in word:
		word = word.replace(':', "")
	if ';' in word:
		word = word.replace(';', "")
	if ',' in word:
		word = word.replace(',', "")
	if '|' in word:
		word = word.replace('|', "")
	if '.' in word:
		word = word.replace('.', "")
	if '--' in word:
		word = word.replace('--', "")
	return(word)

'''
@pre
@param   text
@throws  none
@returns dictionary - with every word in the text and the count of how many times that words appeared in the text
'''
def build_count(text):
	text = text.split()
	i = 0
	for element in text:
		text[i] = clean_word(element)
		i = i + 1
	dictionary = {}
	dictionary = dict(Counter(text))
	return(dictionary)


'''
@pre     build_count(text) must have called and returned a dictionary of the text
@param   p_dictionary - takes in a dictionary of words and their counts
@throws  none
@returns new_list - a list (not a dict!) of all words that have a count of exactly 1
'''
def unique_words(p_dictionary):
	new_list = []
	for key, value in p_dictionary.items():
		if value == 1:
			new_list.append(key)
	return(new_list)

'''
@pre     prompt must have been called and returned a string with the name of the file mobydick.txt
@param   p_file - the name of the file mobydick.txt
@throws  none
@returns a string literal of all of the words from mobydick.txt
'''
def fileInput(p_file):
	in_file = open(p_file)
	stringed_file = ""
	stringed_file = in_file.read()
	in_file.close()
	return(stringed_file)

'''
@pre     a cleaned dictionary must have been created by all other functions above
@param   p_dictionary
@throws  none
@returns none
'''
def word_data_FIO(p_dictionary):
	in_file = open("word_data.txt", 'w')
	for key in p_dictionary:
		in_file.write(str(p_dictionary[key]) + '	' + key + '\n')
	in_file.close()
	return(None)

'''
@pre     unqiue_words(dictionary) must have already returned a cleaned list
@param   p_list - a list containing all of the unique instances of words from mobydick.txt
@throws  none
@returns none
'''
def unique_words_FIO(p_list):
	in_file = open("unique_words.txt", 'w')
	length = len(p_list)
	for i in range(length):
		in_file.write(str(p_list[i]) + '\n')
	in_file.close()
	return(None)

if __name__ == "__main__":
	main()
