#!/usr/bin/env python3

x = input('Enter a num:')
y = input('Enter a num:')

def print_maxnum(a, b):
	if a > b:
		print(a, 'is maxnum')
	elif a == b:
		print(a, 'is equal', b)
	else:
		print(b, 'is maxnum')

print_maxnum(x, y)
