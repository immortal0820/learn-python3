#!/usr/bin/env python3
#coding: utf-8
#Filename: client.py

import socket

clsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = ''
port = 8888

clsock.connect((host, port))

while True:
	sended = input('Client: ')
	clsock.send(sended.encode('utf-8'))

	if sended == 'quit' or sended == 'exit':
		break

	recved = clsock.recv(1024)
	print('Client: {0}'.format(recved.decode('utf-8')))

clsock.close()
