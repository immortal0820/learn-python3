#!/usr/bin/env python3
# Filename: use_input.py

def reverse(text):
	return text[::-1]

def is_palindrome(text):
	return text == reverse(text)

count = True

while count:
	something = input('Enter text:')

	if (is_palindrome(something)):
		print('Yes, it is a palindrome.')
		count = False
	else:
		print("No, it is't a palindrome.")
