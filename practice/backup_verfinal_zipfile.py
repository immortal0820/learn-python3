#!/usr/bin/env python3
#Filename: backup_verfinal_zipfile.py

import os, time, sys, zipfile

def compress_file (zipfilename, sourcefile):
	z = zipfile.ZipFile(zipfilename, 'w')
	for i in sourcefile:
		if os.path.isfile(i):
			z.write(i)
		else:
			for root, dirs, files in os.walk(i):
				for single_file in files:
					filepath = os.path.join(root, single_file)
					z.write(filepath)
	
	z.close()


def addfile (zipfilename, sourcefile):
	z = zipfile.ZipFile(zipfilename, 'a')
	for i in sourcefile:
		if os.path.isfile(i):
			z.write(i)
		else:
			for root, dirs, files in os.walk(i):
				for single_file in files:
					filepath = os.path.join(root, single_file)
					z.write(filepath)

	z.close()

def viewfile(zipfilename):
	with zipfile.ZipFile(zipfilename, 'r') as z:
		print(z.namelist())

def main():
	source = sys.argv[1:]
	target_dir = '/root/Desktop'
	
	today = target_dir + os.sep + time.strftime('%Y%m%d')
	now = time.strftime('%H%M%S')

	comment = input('Enter comment--> ')
	if len(comment) == 0:
		target = today + os.sep + now + '.zip'
	else:
		target = today + os.sep + now + '_' \
				+ comment.replace(' ', '_') + '.zip'

	if not os.path.exists(today):
		os.mkdir(today)
	
	if os.path.exists(target):
		addfile(target, source)      # no exec forever(time is change), unless specifiy zip name and path
	else:
		compress_file(target, source)
		viewfile(target)

if __name__ == '__main__':
	main()
