#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
Created on 10:14 2018/1/26 

@author: acer
'''

import urllib2
import urllib
import cookielib
filename = 'cookie.txt'
url = "http://202.195.128.88:60080/120Manage/login.action"
cookie = cookielib.MozillaCookieJar(filename)
data ={'username':'admin'}
handler = urllib2.HTTPCookieProcessor(cookie)

opener = urllib2.build_opener(handler)

response = opener.open('http://www.baidu.com')
cookie.save(ignore_discard=True, ignore_expires=True)