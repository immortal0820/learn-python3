#!/usr/bin/env python3
#Filename: backup_verfinal_tarfile.py

import os, sys, time, tarfile

def compress_file (tarfilename, sourcefile):
	with tarfile.open(tarfilename, 'w') as tar:
		for i in sourcefile:
			if os.path.isfile(i):
				tar.add(i)
			else:
				for root, dirs, files in os.walk(i):
					for single_file in files:
						filepath = os.path.join(root, single_file)
						tar.add(filepath)

def viewfile (tarfilename):
	with tarfile.open(tarfilename, 'r') as tar:
		print(tar.getmembers())

def main():
	source = sys.argv[1:]
	target_dir = '/root/Desktop'

	today = target_dir + os.sep + time.strftime('%Y%m%d')

	if not os.path.exists(today):
		os.mkdir(today)

	now = time.strftime('%H%M%S')

	commit = input('Enter commit--> ')
	if len(commit) == 0:
		target = today + os.sep + now + '.tar'
	else:
		target = today + os.sep + now + '_' \
				+ commit.replace(' ', '_') + '.tar'

	compress_file(target, source)

if __name__ == '__main__':
	#main()
	viewfile('/root/Desktop/20180510/172730_test.tar')
