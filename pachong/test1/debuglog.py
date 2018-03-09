#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
Created on 15:37 2017/10/17 

@author: acer
'''

import urllib2
httpHandler = urllib2.HTTPHandler(debuglevel=1)
htttpsHamdler = urllib2.HTTPSHandler(debuglevel=1)
opener = urllib2.build_opener(httpHandler,htttpsHamdler)
urllib2.install_opener(opener)
response = urllib2.urlopen('http://www.baidu.com')
print response.read()