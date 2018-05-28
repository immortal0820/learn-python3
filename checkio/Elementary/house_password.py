#!/usr/bin/env python3
#coding: utf-8
#Filename: house_password.py

import re

Digit = re.compile('\d')
Upper = re.compile('[A-Z]')
Lower = re.compile('[a-z]')

def checkio(data):
	"This is Checkio give solution"

	if len(data) < 10:
		return False

	if not Digit.search(data):
		return False
	if not Upper.search(data):
		return False
	if not Lower.search(data):
		return False

	return True

'''
def checkio(data):
	"This is my solution"

	digit = False
	upper = False
	lower = False

	if len(data) < 10:
		return False

	for c in data:
		if c.isdigit():
			digit = True
		elif c.isupper():
			upper = True
		elif c.islower():
			lower = True
		else:
			return False
	if digit and upper and lower:
		return True
	else:
		return False
'''

if __name__ == '__main__':
	ret = checkio('aaarAaaaaaaa')
	if ret and True:
		print('Ok')
	else:
		print('Fail')
