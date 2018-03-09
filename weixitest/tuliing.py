#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Created on 20:05 2017/11/4 

@author: acer
'''

import urllib
import json


def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def reboot(data):
    print "reboot:"+data
    key = 'f156e99bbc6a43059eafcb3b2e55482e'
    api = 'http://www.tuling123.com/openapi/api?key=' + key + '&info='
    info = data
    request = api + data
    response = getHtml(request)
    print response.decode('utf-8')
    return response
    # dic_json = json.loads(response)
    # print '机器人: '.decode('utf-8') + dic_json['text']
    # code=dic_json['code']
    # print code
    # if code == 100000:
    #     return dic_json['text'].encode('utf-8')
    # elif code ==200000:
    #     data=dic_json['text']+'\n'+dic_json['url']
    #     return data.encode('utf-8')
    # elif code ==300000:
    #     data=dic_json['text']+'\n'+dic_json['list']
    #     return data.encode('utf-8')


if __name__ == '__main__':
    reboot("你好")

