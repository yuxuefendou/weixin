#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
Created on 14:56 2017/10/17 

@author: acer
'''
import urllib2
# response = urllib2.urlopen("http://blog.yuxuefendou.cn")
# print response.read()

request = urllib2.Request("http://blog.yuxuefendou.cn")
response = urllib2.urlopen(request)
print response.read()