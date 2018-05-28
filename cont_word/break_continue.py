#!/usr/bin/env python3

'''
while True:
	s = input('Enter something:')
	if s == 'quit' or s == 'exit':
		break
	print('Length of the string is', len(s))
else:
	print('Done')
'''

while True:
	s = input('Enter something:')
	if s == 'quit' or s == 'exit':
		break
	if len(s) < 4:
		print('Length too small')
		continue
	print('Input is of sufficient length')

