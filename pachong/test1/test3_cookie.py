#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
Created on 16:30 2017/10/17 

@author: acer
'''

import urllib2
import cookielib

cookie = cookielib.CookieJar()
handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)
response = opener.open('http://www.baidu.com')
for item in cookie:
    print 'Name = ' + item.name
    print 'Value = '+ item.value