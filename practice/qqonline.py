#!/usr/bin/env python3
#coding: utf-8
#Filename: qqonline.py

import requests
from xml.etree import ElementTree as ET

qq_url = 'http://www.webxml.com.cn//webservices/qqOnlineWebService.asmx/qqCheckOnline?qqCode=1123891726'

r = requests.get(qq_url)

result = r.text
print(result)

node = ET.XML(result)
if node.text == 'Y':
	print('online')
else:
	print('offline')
