#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
Created on 0:31 2017/10/19 

@author: acer
'''
import urllib2
def download(url,user_agent='wswp',num_retries=2):
    print 'Downloading:',url
    headers = {'User-agent' : user_agent}
    request = urllib2.Request(url,hreaders=headers)
    try:
        html = urllib2.urlopen(request).read()
    except urllib2.URLError as e:
        print 'Download erro:',e.reason
        html = None
        if num_retries>0:
            if hasattr(e,'code') and 500 <=e.code <600:
                # num_retries=num_retries-1
                return download(url,user_agent='wswp',num_retries-1)

    return html


if __name__ == '__main__':
    download('http://httpstat.us/500')