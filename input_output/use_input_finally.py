#!/usr/bin/env python3
#Filename: use_input_finally.py

import string

def reverse(text):
	return text[::-1]

def is_palindrome(text):
	text = text.lower()
	text = text.replace(' ', '')
	for char in string.punctuation:
		text = text.replace(char, '')
	
	return text == reverse(text)

def main():
	something = input('Enter something:')

	if (is_palindrome(something)):
		print('{0} is palindrome.'.format(something))
		return 0
	elif something == 'quit' or something == 'exit':
		return 0
	else:
		print('{0} is not palindrome.'.format(something))
		return -1
		

if __name__ == '__main__':
	while 1:
		ret = main()
		if ret == 0:
			break
		else:
			continue

else:
	print('use_input_finally.py was imported.')
