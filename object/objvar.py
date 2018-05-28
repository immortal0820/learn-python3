#!/usr/bin/env python3
#Filename: objvar.py

# 类变量：一个类中的所有对象（实例）共享使用。因此某个对象对类变量改动后，改动会反映到其他对象上。
# 对象变量：类的每个对象（实例）所拥有，不共享，虽然对象的变量有相同的名称，但是互不相关，有各自的值

class Robot:
	population = 0  # A class variable, use Robot.population.

	def __init__(self, name):	# name is object variable, use self.name.
		self.name = name
		print('(Initialize {0})'.format(self.name))

		Robot.population += 1

	def __del__(self):
		print('{0} is being destroyed!'.format(self.name))
		
		Robot.population -= 1

		if Robot.population == 0:
			print('{0} was the last one.'.format(self.name))
		else:
			print('There are still {0:d} robots working.'.format(Robot.population))

	def sayhi(self):
		print('Greetings, my master call me {0}'.format(self.name))

	def howMany():		# class method not object method
		print('We have {0:d} robots.'.format(Robot.population))

	howMany = staticmethod(howMany)  # static method


droid1 = Robot('R2-D2')
droid1.sayhi()
Robot.howMany()

droid2 = Robot('C-3P0')
droid2.sayhi()
Robot.howMany()

print('\nRobots can do some work here.\n')
print("Robots have finished their work, So let's destroy them.")

del droid1
del droid2

Robot.howMany()



