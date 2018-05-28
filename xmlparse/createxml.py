#!/usr/bin/env python3
#coding: utf-8
#Filename: createxml.py

from xml.dom import minidom

clientId = 'diiekke-eeeie-ddeee'
dbname = 'ORCL'
status = 1

def createxml(clientId, dbnae, status):
	impl = minidom.getDOMImplementation()
	resultdom = impl.createDocument(None, 'Stremer', None)
	root = resultdom.documentElement
	client = resultdom.createElement('Oracle')
	client.setAttribute('Name', dbname)
	client.setAttribute('status', str(status))
	client.setAttribute('ClientId', clientId)
	root.appendChild(client)

	with open('test.xml', 'w') as fp:
		resultdom.writexml(fp, indent = '', newl = '\n', addindent = '  ', encoding = 'utf-8')		# tree形式
		#resultdom.writexml(fp)		# string形式
	#return resultdom.toxml()		# string形式
if __name__ == '__main__':
	createxml(clientId, dbname, status)
	#print(xml)
