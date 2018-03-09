#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
Created on 22:05 2017/10/17 

@author: acer
'''

import cookielib

import urllib2

filename = 'cookie.txt'

cookie = cookielib.MozillaCookieJar(filename)

handler = urllib2.HTTPCookieProcessor(cookie)

opener = urllib2.build_opener(handler)
response = opener.open('http://www.baidu.com')
cookie.save(ignore_discard=True, ignore_expires=True)


