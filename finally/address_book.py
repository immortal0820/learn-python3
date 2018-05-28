#!/usr/bin/env python3
# coding: utf-8
# Filename: address_book.py

import os, pickle

class Contacts:
	filename = 'address.data'

	def __init__(self, name, address):
		self.name = name
		self.address = address
		
		if self.name == '' or self.address == '':
			self.personlist = {}
		else:
			self.personlist = {self.name:self.address}

	def add(self):
		self.name = input('Enter name: ')
		if self.name in self.personlist.keys():
			print('The name is exist')
		else:
			self.address = input('Enter address(exp: mail, phone): ')
			self.personlist[self.name] = self.address
			print('Added')

	def delete(self):
		self.name = input('Enter name which you want to delete: ')
		if self.name in self.personlist.keys():
			del self.personlist[self.name]
			print('Deleted')
		else:
			print('The name is not exist')

	def modify(self):
		self.name = input('Enter name which you want to modify: ')
		if self.name in self.personlist.keys():
			self.address = input('Enter address(exp: mail, phone): ')
			self.personlist[self.name] = self.address
			print('Modified')
		else:
			print('The name is not exist')

	def select(self):
		self.name = input('Enter name which you want to select: ')
		if self.name in self.personlist.keys():
			print('Name:{0} address:{1}'.format(self.name, self.address))
		else:
			print('The name is not exist')

	def show(self):
		for self.name, self.address in self.personlist.items():
			print('Name:{0} address:{1}'.format(self.name, self.address))

	def create_load(self):
		if os.path.exists(Contacts.filename):
			with open(Contacts.filename, 'rb') as fp:
				self.personlist = pickle.load(fp)

	def save(self):
		with open(Contacts.filename, 'wb') as fp:
			pickle.dump(self.personlist, fp)

'''
def main():
	command = ['add', 'delete', 'modify', 'select', 'show', 'quit']
	person = Contacts('', '')
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
				ch = input("Your contacts not saved, saved it now?(y/n): ")
				if ch == 'y':
					person.save()
					exit()
				else:
					exit()
		else:
			print('The command is error')

if __name__ == '__main__':
	main()
'''
