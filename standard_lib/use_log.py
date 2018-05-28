#!/usr/bin/env python3
#Filename: use_log.py

import os, platform, logging

'''
if platform.platform().startswith('Windows'):
	logging_file = os.path.join(os.getenv('HOMEDRIVE'), 'test.log')
else:
	logging_file = os.path.join(os.getenv('HOME'), 'test.log')

logging.basicConfig(
		level = logging.DEBUG,
		format = '%(asctime)s : %(levelname)s : %(message)s',
		filename = logging_file,
		filemode = 'a+',)

logging.debug('Start of the program.')
logging.info('Dong something.')
logging.warning('Dying now.')
'''

class Myloger(logging.Logger):
	def __init__(self):
		
		log_file = ('test.log')
		fmt = '%(asctime)s-%(filename)s : %(levelname)s : %(message)s'
		dfmt = '%Y-%m-%d %H:%M:%S'

		logging.Logger.__init__(self, log_file)

		logger = logging.getLogger('test')
		self.setLevel(logging.DEBUG)

		handler = logging.FileHandler(log_file)
		handler.setLevel(logging.DEBUG)

		formatter = logging.Formatter(fmt, dfmt)
		handler.setFormatter(formatter)

		self.addHandler(handler)

if __name__ == '__main__':
	log = Myloger()
	log.debug('Start of the program.')
	log.info('Ding something.')
