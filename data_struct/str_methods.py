#!/usr/bin/env python3
#Filename: str_methods.py

name = 'Swaroop'

if name.startswith('Sw'):
	print('Yes, the string starts with "Sw"')

if 'a' in name:
	print('Yes, it contains the string "a"')

if name.find('w') != -1:
	print('Yes, it contains the string "w"')
	
delimiter = '_*_'
mylist = ['Brazil', 'Russia', 'India', 'China']
print(delimiter.join(mylist))	# str method join
