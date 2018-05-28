#!/usr/bin/env python3
# coding: utf-8
# Filename: address_book_main.py

import address_book

def main():
	command = ['add', 'delete', 'modify', 'select', 'show', 'quit']
	person = address_book.Contacts('', '')
	person.create_load()
	while True:
		str = input('Enter command(add/delete/modify/select/show/quit): ')
		if str in command:
			if str == 'add':
				person.add()
			elif str == 'delete':
				person.delete()
			elif str == 'modify':
				person.modify()
			elif str == 'select':
				person.select()
			elif str == 'show':
				person.show()
			else:
				ch = input('Your contacts not saved, saved it now?(y/n): ')
				if ch == 'y':
					person.save()
					exit()
				else:
					exit()
		else:
			print('The command is error')

if __name__ == '__main__':
	main()
else:
	print('the is owner programming')
