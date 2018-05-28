#!/usr/bin/env python3
# Filename: try_except.py

try:
	text = input('Enter something --> ')
except EOFError:
	print('Why did you do an EOF on me?')
except KeyboardInterrupt:
	print('You cancelled the operation')
else:
	print('You enter {0}'.format(text))
