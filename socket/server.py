#!/usr/bin/env python3
#coding: utf-8
#Filename: server.py

import socket, sys

# socket(创建socket)
servsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind(绑定端口号)
host = ''
port = 8888
servsock.bind((host, port))

# listen(设置最大连接数，超过后排队)
servsock.listen(5)
clientsock, addr = servsock.accept()

while True:
	recved = clientsock.recv(1024)

	msg = recved.decode('utf-8')
	print('Server: %s' % msg)

	if msg == 'quit' or msg == 'exit':
		break

	sended = input('Server: ')
	clientsock.send(sended.encode('utf-8'))

clientsock.close()
servsock.close()
