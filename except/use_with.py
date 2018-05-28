#!/usr/bin/env python3
#Filename: use_with.py

import time

def main():
	with open('poem.txt') as fp:
		for line in fp:
			print(line, end='')
			time.sleep(2)

if __name__ == '__main__':
	main()

