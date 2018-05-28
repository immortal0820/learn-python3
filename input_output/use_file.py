#!/usr/bin/env python3
# Filename: use_file.py

poem = '''\
Programming is fun
When the work is done
if you wanna make your work also fun:
	use Python!
'''

fp = open('poem.txt', 'w')
fp.write(poem)
fp.close()

fp = open('poem.txt')	# 'r' default mode

while True:
	line = fp.readline()
	if len(line) == 0:
		break
	print(line, end='')

fp.close()
