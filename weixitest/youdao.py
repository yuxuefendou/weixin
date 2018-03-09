#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
Created on 15:16 2017/11/4 

@author: acer
'''
import json
import urllib2
def youdao(word):
    print word
    baseurl = r'http://fanyi.youdao.com/openapi.do?keyfrom=test&key=62f2ea7b85f3de48&type=data&doctype=json&version=1.1&q='
    url = baseurl+word
    print url
    resp = urllib2.urlopen(url)
    fanyi = json.load(resp.read())
    print fanyi
    #根据json 是否返回一个叫"basic" 的 key 来判读是否翻译成功
    if 'basic' in fanyi.keys():
        #下面是你自己组织的格式
        trans = u'%s:\n%s\n%s\n网络释义：\n%s' % (
        fanyi['query'], ''.join(fanyi['translation']), ''.join(fanyi['basic']['explains']),
        ''.join(fanyi['web'][0]['value']))
        print trans
        return trans
    else:
        return u'对不起，您输入的单词%s无法翻译，请检查拼写' % word