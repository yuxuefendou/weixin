#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
Created on 14:44 2017/10/18 

@author: acer
'''
import requests
r= requests.get('http://blog.yuxuefendou.cn')
print type(r)
print r
print r.status_code
print r.encoding
print r.cookies
payload = {'key1':'value1','key2':'value2'}
r = requests.get("http://httpbin.org/get",params=payload)
print r.url