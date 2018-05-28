#!/usr/bin/env python3
# Filename: class_init.py

class Person:
	def __init__(self, name):
		self.name = name

	def sayhi(self):
		print('hi, my name is', self.name)


p = Person('')
p.sayhi()

Person('immortal').sayhi()
