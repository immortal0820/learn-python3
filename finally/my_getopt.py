#!/usr/bin/python3
#Filename: getopt.py

import sys
import getopt

Info = []

def printUsage():
	print('''Usage: This is my project
	-i, --insert	insert a data
	-c, --del	delete a data
	-s, --search	search a data
	-l, --list	list data
	-h, --help	show help info''')

def list_insert(Info, value):
	Info.append(value)

def list_del(Info, value):
	Info.remove(value)

def list_view(Info):
	for i in Info:
		print(i)

def main():
	try:
		opts, args = getopt.getopt(sys.argv[1:], "hi:d:s:l", ["help", "insert=", "del=", "search=", "list"])
	except getopt.GetoptError:
		printUsage()
		exit()
	for opt_name, opt_value in opts:
		if opt_name in ('-h', '--help'):
			printUsage()
			exit()
		elif opt_name in ('-i', '--insert'):
			list_insert(Info, opt_value)
			print(Info)
		elif opt_name in ('-d', '--del'):
			list_del(Info, opt_value)
			print(Info)
			exit()
		elif opt_name in ('-l', '--list'):
			list_view(Info)
			exit()

if __name__ == '__main__':
	main()


