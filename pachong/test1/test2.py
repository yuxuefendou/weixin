#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
Created on 15:17 2017/10/17 

@author: acer
'''
import urllib
import urllib2

url = 'http://blog.yuxuefendou.cn/admin'
user_agent = 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Mobile Safari/537.36'
values = {'username':'admin','password':'xukang1993'}
headers = {'User-Agent':user_agent}

data = urllib.urlencode(values)
request = urllib2.Request(url,data,headers)
response = urllib2.urlopen(request)
page = response.read()
print page