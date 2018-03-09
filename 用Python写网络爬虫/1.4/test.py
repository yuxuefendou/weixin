#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
Created on 0:20 2017/10/19 

@author: acer
'''
import urllib2
def download(url):
    print 'Downloading:',url
    try:
        html = urllib2.urlopen(url).read()
    except urllib2.URLError as e:
        print 'Download erro:',e.reason
        html = None
    return html