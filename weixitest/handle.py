#!/usr/bin/env python
#-*- coding:utf-8 -*-
import hashlib
import web
import os
import reply
import receive
import chardet

class Handle(object):
    def __init__(self):
        self.app_root = os.path.dirname(__file__)
        self.templates_root = os.path.join(self.app_root, 'templates')
        self.render = web.template.render(self.templates_root)
    def GET(self):
        print 'hello'
        try:
            data = web.input()
            print data
            # print data.echostr
            if len(data) == 0:
                return "hello, this is handle view"
            signature = data.signature
            timestamp = data.timestamp
            nonce = data.nonce
            echostr = data.echostr
            token = "yuxuefendou" #请按照公众平台官网\基本配置中信息填写

            list = [token, timestamp, nonce]
            list.sort()
            sha1 = hashlib.sha1()
            map(sha1.update, list)
            hashcode = sha1.hexdigest()
            print "handle/GET func: hashcode, signature: ", hashcode, signature
            if hashcode == signature:
                return echostr
            else:
                return ""
        except Exception, Argument:
            return Argument


    def POST(self):
        try:
            webData = web.data()
            print webData.decode('utf-8')# 后台打日志
            #解析xml数据
            recMsg = receive.parse_xml(webData)
            print recMsg
            print recMsg.MsgType
            print isinstance(recMsg,receive.Msg)
            print isinstance(recMsg,receive.EventMsg)
            if isinstance(recMsg, receive.Msg) or isinstance(recMsg,receive.EventMsg):
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                # print recMsg.MsgType
                print u"MsgType类型"
                # print chardet.detect(recMsg.MsgType)
                if recMsg.MsgType == 'text':
                    content = recMsg.Content
                    replyMsg = reply.TextMsg(toUser, fromUser, content)
                    return replyMsg.send()
                if recMsg.MsgType == 'image'.decode('ascii'):
                    mediaId = recMsg.MediaId
                    replyMsg = reply.ImageMsg(toUser,fromUser,mediaId)
                    return replyMsg.send()
                if recMsg.MsgType == 'event':
                    print u"接收到event信号"
                    event = recMsg.Event
                    print chardet.detect(event)
                    replyMsg = reply.EvenMsg(toUser,fromUser,event)
                    return replyMsg.send()
                else:
                    return reply.Msg().send()
            else:
                # print "暂且不处理"
                return "success"
        except Exception, Argument:
            return Argument.time()