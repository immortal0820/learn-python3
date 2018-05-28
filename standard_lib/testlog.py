#!/usr/bin/env/python3
#coding: utf-8
#Filename: testlog.py

import logging

class Mylog:
	__file = 'my.log'
	__fmt = '%(asctime)s-%(filename)s:[line:%(lineno)s]-%(name)s-%(message)s'

	def __init__(self):
		logging.basicConfig(filename = Mylog.__file, filemode = 'a+', format = Mylog.__fmt)

		self.__handler = logging.NullHandler()
		self.__handler.setLevel(logging.DEBUG)

		formatter = logging.Formatter(Mylog.__fmt)
		self.__handler.setFormatter(formatter)

	def getlogger(self):
		logger = logging.getLogger('test')
		logger.setLevel(logging.DEBUG)
		logger.addHandler(self.__handler)
		return logger

if __name__ == '__main__':
	testlog = Mylog().getlogger()
	testlog.info('info log')
	testlog.debug('debug log')
	testlog.error('error log')
