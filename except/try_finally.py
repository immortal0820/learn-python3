#!/usr/bin/env python3
#Filename: try_finally.py

import time

try:
	f = open('poem.txt')
	while True:
		line = f.readline()
		if len(line) == 0:
			break
		print(line, end = '')
		time.sleep(2)
except KeyboardInterrupt:
	print('!! You cancelled the reading from file')
finally:
	f.close()
	print('(Cleanning up: close the file)')
