#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
Created on 15:04 2017/10/18 

@author: acer
'''

import requests
# r = requests.get('a.json')
# print r.text
# print r.json()
r = requests.get('https://github.com/timeline.json', stream=True)
print r.raw
print r.raw.read()

print '------'*50

payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.post("http://httpbin.org/post", data=payload)
print r.text
