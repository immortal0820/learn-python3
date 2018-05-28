#!/usr/bin/env python3
# Filename: raise_except.py

class ShortInputException(Exception):
	'''A user-defined exception class'''
	def __init__(self, length, atleast):
		Exception.__init__(self)
		self.length = length
		self.atleast = atleast

try:
	text = input('Enter something --> ')
	if len(text) < 3:
		raise ShortInputException(len(text), 3)
except EOFError:
	print('Why do you do an error on me?')
except ShortInputException as ex:
	print('ShortInputException the input {0} was long, exceped atleast {1}'.format(ex.length, ex.atleast))
else:
	print('No exception was raised!')

