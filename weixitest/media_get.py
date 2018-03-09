#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
Created on 14:03 2017/11/4 

@author: acer
'''

from basic import Basic
import urllib2
import poster.encode
import json
from poster.streaminghttp import register_openers

class Media(object):
    def __init__(self):
        register_openers()
    #上传图片
    def uplaod(self, accessToken, filePath, mediaType):
        openFile = open(filePath, "rb")
        param = {'media': openFile}
        postData, postHeaders = poster.encode.multipart_encode(param)

        postUrl = "https://api.weixin.qq.com/cgi-bin/media/upload?access_token=%s&type=%s" % (accessToken, mediaType)
        request = urllib2.Request(postUrl, postData, postHeaders)
        urlResp = urllib2.urlopen(request)
        print urlResp.read()
    #获取图片
    def get(self, accessToken, mediaId):
        postUrl = "https://api.weixin.qq.com/cgi-bin/media/get?access_token=%s&media_id=%s" % (accessToken, mediaId)
        print postUrl
        urlResp = urllib2.urlopen(postUrl)

        headers = urlResp.info().__dict__['headers']
        if ('Content-Type: application/json\r\n' in headers) or ('Content-Type: text/plain\r\n' in headers):
            jsonDict = json.loads(urlResp.read())
            print jsonDict
        else:
            buffer = urlResp.read()  # 素材的二进制
            mediaFile = file("test_media.jpg", "wb")
            mediaFile.write(buffer)
            print "get successful"

if __name__ == '__main__':
    myMedia = Media()
    accessToken = Basic().get_access_token()
    # filePath = "D:/Pythonwork/weixin/weixitest/test.jpg"   #请安实际填写
    # mediaType = "image"
    # myMedia.uplaod(accessToken, filePath, mediaType)
    mediaId = "WALHfopNDJ7V4tzGt95Di2eMbOyWP-oAYmP6bSvYVMMdQbuag5N-O7rWIRX0gIXX"
    myMedia.get(accessToken, mediaId)