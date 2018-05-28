#!/usr/bin/env python3

'''
num = 11
guess = int(input('please input a num:'))

if guess == num:
	print('you guess it!')
elif guess < num:
	print('the num lower than that')
else:
	print('the num higher than that')
'''

num = 15
run = True

while run:
	guess = int(input('please input a guess num:'))
	
	if guess < num:
		print('the num is lower than that')
	elif guess > num:
		print('the num is higher than that')
	else:
		print('you guess it!')
		run = False
else:
	print('the loop is over!')

