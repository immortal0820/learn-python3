#!/usr/bin/env python3
# Filename: inherit.py

class SchoolMember:
	'''Represent any school member.'''

	def __init__(self, name, age):
		self.name = name
		self.age = age
		print('(Initialize SchoolMember:{0})'.format(self.name))

	def tell(self):
		'''Tell any details.'''
		print('Name:{0}, Age:{1:d}'.format(self.name, self.age), end = ', ')	# print 默认结尾'\n', 指定了end = ', ', 表示不换行，以', '结尾

class Teacher(SchoolMember):		# 继承了一个以上的基类，称为多重继承
	'''Represent a teacher.'''

	def __init__(self, name, age, salary):
		SchoolMember.__init__(self, name, age)  # python 不会自动调用基本类中的方法，需要手动调用
		self.salary = salary
		print('(Initialize Teacher:{0})'.format(self.name))

	def tell(self):
		SchoolMember.tell(self)
		print('Salary:{0:d}.'.format(self.salary))		# {0：d} d:表示整数类型

class Student(SchoolMember):
	'''Represent a student.'''

	def __init__(self, name, age, mark):
		SchoolMember.__init__(self, name, age)
		self.mark = mark
		print('(Initialize Student:{0})'.format(self.name))

	def tell(self):
		SchoolMember.tell(self)
		print('Mark:{0:d}.'.format(self.mark))

t = Teacher('Harden.James', 35, 8000)
s = Student('Zhouqi', 25, 80)

print() # print a empty block(空行)

members = [t, s]
for member in members:
	member.tell()
