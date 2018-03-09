#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
Created on 2:08 2017/11/5 

@author: acer
'''
import urllib2
import json

from basic import Basic

class Material(object):
    #上传图文
    def add_news(self, accessToken, news):
        postUrl = "https://api.weixin.qq.com/cgi-bin/material/add_news?access_token=%s" % accessToken
        urlResp = urllib2.urlopen(postUrl, news)
        print urlResp.read()

if __name__ == '__main__':
    myMaterial = Material()
    accessToken = Basic().get_access_token()
    news =(
    {
        "articles":
        [
            {
            "title": "test",
            "thumb_media_id": "88PMwxDJTMTgLCqO4NhND2-hQb2Puj3D_T2JHE0SB1Q7nPZgw86lWPiTmDyC_nmG",
            "author": "vickey",
            "digest": "",
            "show_cover_pic": 1,
            "content": "abc",
            "content_source_url": "",
            }
        ]
    })
    #news 是个dict类型，可通过下面方式修改内容
    #news['articles'][0]['title'] = u"测试".encode('utf-8')
    #print news['articles'][0]['title']
    news = json.dumps(news, ensure_ascii=False)
    print news
    myMaterial.add_news(accessToken, news)