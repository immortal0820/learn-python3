#!/usr/bin/env python3

def Max(x, y):
	'''Prints the maxinum of two numbers.

	The two num must be integers.'''
	x = int(x)
	y = int(y)

	if x > y:
		return x
	else:
		return y

def printMax():
	x = int(input('please input a num of x:'))
	y = int(input('please input a num of y:'))

	max = Max(x, y)
	#print(Max.__doc__)
	print(max, 'is maxnum')

printMax()
