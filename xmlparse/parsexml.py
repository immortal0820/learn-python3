#!/usr/bin/env python3
#coding: utf-8
#Filename: parsexml.py

from xml.dom import minidom

def getxmlinfo(xmlfile):
	xmldoc = minidom.parse(xmlfile)
	root = xmldoc.documentElement
	
	oracle = root.getElementsByTagName("Oracle")[0]
	clientId = str(oracle.getAttribute('ClientId'))
	dbname = str(oracle.getAttribute('Name'))
	status = int(oracle.getAttribute('status'))
	print('clientId: {0}, dbname: {1}, status: {2}'.format(clientId, dbname, status))
	
	'''
	oracle = root.getElementsByTagName("Oracle")
	for os in oracle:
		clientId = str(os.getAttribute('ClientId'))
		dbname = str(os.getAttribute('Name'))
		status = int(os.getAttribute('status'))
		print('clientId: {0}, dbname: {1}, status: {2}'.format(clientId, dbname, status))
		#return (clientId, dbname, status)
	'''
	'''
	oracle = root.getElementsByTagName("Oracle")
	oral = oracle[0]
	clientId = str(oral.getAttribute('ClientId'))
	dbname = str(oral.getAttribute('Name'))
	status = int(oral.getAttribute('status'))
	print('clientId: {0}, dbname: {1}, status: {2}'.format(clientId, dbname, status))
	'''

if __name__ == '__main__':
	getxmlinfo('test.xml')
